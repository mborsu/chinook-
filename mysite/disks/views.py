from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Album


class IndexView(generic.ListView):
    template_name = 'disks/index.html'
    context_object_name = 'album_list'

    def get_queryset(self):
        """Return all the albums"""
        return Album.objects.order_by('artist')


class DetailView(generic.DetailView):
    template_name = 'disks/detail.html'
    
    def get_queryset(self):
        """
        get details of the album
        """
        return Album.objects.order_by('title')


