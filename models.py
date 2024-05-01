"""Model definition for bd_schema_plugin."""

from django.db import models

from nautobot.core.models import BaseModel
from nautobot.extras.utils import extras_features
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField


# Create your models here. Models should inherit from BaseModel.

@extras_features("graphql")
class Node(models.Model):
    """Base model for Node."""

    types = models.CharField(max_length=255, default="Type")
    properties = models.JSONField(default=dict, blank=True) 
    labels = ArrayField(models.CharField(max_length=255), default=list, blank=True)
    
    def __str__(self):
        return str(self.id)


@extras_features("graphql")
class Relationship(models.Model):
    """Base model for Relationship between Node."""

    relation_type = models.CharField(max_length=255, default="Type")
    properties = models.JSONField(default=dict)
    from_node = models.ForeignKey(Node, related_name='from_node', on_delete=models.CASCADE)
    to_node = models.ForeignKey(Node, related_name='to_node', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    