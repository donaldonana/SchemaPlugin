"""Urls for bd_schema_plugin."""

from django.urls import path

from bd_schema_plugin import views

urlpatterns = [
    path('<int:page>/', views.RandomNodeView.as_view(), name='index'),
    path('', views.RandomNodeView.as_view(), name='index'),
    path('create', views.create_node, name = 'create_node'),
    path('delete/<id>/', views.delete_node, name = 'delete_node'),
    path('details/<id>/', views.details_node, name = 'details_node'),
    path('edit/<id>/', views.node_edit, name = 'node_edit'),
    path('relation', views.RandomRelationView.as_view(), name='relation'),
    path('relation/create', views.create_relation, name = 'create_relation'),
    path('relation/delete/<id>/', views.delete_relation, name = 'delete_relation'),
    path('relation/details/<id>/', views.details_relation, name = 'details_relation'),
    path('relation/edit/<id>/', views.relation_edit, name = 'relation_edit'),
]

