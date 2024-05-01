"""Views for bd_schema_plugin."""

from django.shortcuts import render
from nautobot.core.views import generic
from django.views.generic import View
from bd_schema_plugin import models
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Node, Relationship
from .forms import NodeForm
import json




class RandomNodeView(View):
    """Display a selected Node."""

    def get(self, request, page = 1):                                                            
        data = Node.objects.order_by('id')
        paginator = Paginator(data, per_page=6)
        page_object = paginator.get_page(page)
        context = {"page_obj": page_object}
        return render(request, 'bd_schema_plugin/node.html', context)

class RandomRelationView(View):
    """Display a selected Relation."""

    def get(self, request, page = 1):                                                            
        data = Relationship.objects.order_by('id')
        paginator = Paginator(data, per_page=6)
        page_object = paginator.get_page(page)
        context = {"page_obj": page_object}
        return render(request, 'bd_schema_plugin/relation.html', context)


def create_node(request):
    if request.method == 'POST':
        context = {'data': request.POST}
        types = request.POST.get('types')
        label = request.POST.get('labels')
        properties = request.POST.get('properties')
        try:
            properties = json.loads(str(properties))
        except json.JSONDecodeError as e:
            error = "Enter a valide JSON for field properties."
            context["error"] = error
            return render(request, 'bd_schema_plugin/create_node.html', context)
        if len(properties) == 0:
            error = "A node should have at least one Properties"
            context["error"] = error
            return render(request, 'bd_schema_plugin/create_node.html', context)
        node = Node()
        node.types = types
        node.properties = properties
        if len(label) > 0:
            node.labels = label.replace(" ", "").split(',')
        node.save()
        messages.add_message(request, messages.SUCCESS, "Node Create successfuly")
        return HttpResponseRedirect('/plugins/bd_schema_plugin/')

    return render(request, 'bd_schema_plugin/create_node.html')


def create_relation(request):
    context = {'nodes': Node.objects.order_by('id')}
    if request.method == 'POST':
        context['data'] = request.POST
        types = request.POST.get('types')
        target = request.POST.get('target')
        source = request.POST.get('source')
        properties = request.POST.get('properties')
        try:
            properties = json.loads(str(properties))
        except json.JSONDecodeError as e:
            error = "Enter a valide JSON for field properties."
            context["error"] = error
            return render(request, 'bd_schema_plugin/create_relation.html', context)
            # print(f"Error decoding JSON: {e}")
        if len(properties) == 0:
            error = "A Relation should have at least one Properties"
            context["error"] = error
            return render(request, 'bd_schema_plugin/create_relation.html', context)
        r = Relationship()
        r.relation_type = types
        r.properties = properties
        r.from_node = get_object_or_404(Node, pk=int(source)) 
        r.to_node =  get_object_or_404(Node, pk=int(target)) 
        r.save()
        messages.add_message(request, messages.SUCCESS, "Relationship Create successfuly")
        return HttpResponseRedirect('/plugins/bd_schema_plugin/relation')

    return render(request, 'bd_schema_plugin/create_relation.html', context)


def delete_node(request, id):
    node = get_object_or_404(Node, pk=id)
    node.delete()
    messages.add_message(request, messages.WARNING, "Node Delete successfuly")
    return HttpResponseRedirect('/plugins/bd_schema_plugin/')


def delete_relation(request, id):
    r = get_object_or_404(Relationship, pk=id)
    r.delete()
    messages.add_message(request, messages.WARNING, "Node Delete successfuly")
    return HttpResponseRedirect('/plugins/bd_schema_plugin/relation')


def details_node(request, id):
    node = get_object_or_404(Node, pk=id)
    context = {'node': node}
    return render(request,  'bd_schema_plugin/node_details.html', context)


def details_relation(request, id):
    r = get_object_or_404(Relationship, pk=id)
    context = {'r': r}
    return render(request,  'bd_schema_plugin/relation_details.html', context)


def node_edit(request, id):
    node = get_object_or_404(Node, pk=id)
    context = {'node': node}
    context["node"].properties = json.dumps(context["node"].properties, ensure_ascii=False)
    if request.method == 'POST':
        types = request.POST.get('types')
        label = request.POST.get('labels')
        properties = request.POST.get('properties')
        try:
            properties = json.loads(str(properties))
        except json.JSONDecodeError as e:
            error = "Enter a valide JSON for field properties."
            context["error"] = error
            return render(request, 'bd_schema_plugin/edit_node.html', context)
        if len(properties) == 0:
            error = "A node should have at least one prop"
            context["error"] = error
            return render(request, 'bd_schema_plugin/edit_node.html', context)
        node.types = types
        node.properties = properties
        if len(label) > 0:
            node.labels = label.replace(" ", "").split(',')
        else:
            node.labels = list()
        node.save()
        messages.add_message(request, messages.INFO, "Node Edit successfuly")
        return HttpResponseRedirect('/plugins/bd_schema_plugin/')

    return render(request, 'bd_schema_plugin/edit_node.html', context)


def relation_edit(request, id):
    r = get_object_or_404(Relationship, pk=id)
    context = {'r': r, 'nodes': Node.objects.order_by('id')}
    context["r"].properties = json.dumps(context["r"].properties, ensure_ascii=False)
    if request.method == 'POST':
        types = request.POST.get('types')
        source = request.POST.get('source')
        target = request.POST.get('target')
        properties = request.POST.get('properties')
        try:
            properties = json.loads(str(properties))
        except json.JSONDecodeError as e:
            error = "Enter a valide JSON for field properties."
            context["error"] = error
            return render(request, 'bd_schema_plugin/edit_relation.html', context)
        if len(properties) == 0:
            error = "A Relation should have at least one Properties"
            context["error"] = error
            return render(request, 'bd_schema_plugin/create_relation.html', context)
        r.relation_type = types
        r.properties = properties
        r.from_node = get_object_or_404(Node, pk=int(source))
        r.to_node = get_object_or_404(Node, pk=int(target))
        r.save()
        messages.add_message(request, messages.INFO, "Node Edit successfuly")
        return HttpResponseRedirect('/plugins/bd_schema_plugin/relation')

    return render(request, 'bd_schema_plugin/edit_relation.html', context)

