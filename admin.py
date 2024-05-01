from django.contrib import admin
from .models import Node, Relationship




@admin.register(Node, Relationship)
class NodeAdmin(admin.ModelAdmin):
    pass
