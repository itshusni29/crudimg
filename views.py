#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse  # Import reverse for redirecting
from .models import Kegiatan
from .forms import KegiatanForm
import os

#@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    return render(request, 'home/index.html', context)

#@login_required(login_url="/login/")
def pages(request):
    context = {}
    load_template = request.path.split('/')[-1]

    if load_template == 'admin':
        return HttpResponseRedirect(reverse('admin:index'))

    context['segment'] = load_template
    return render(request, 'home/' + load_template, context)




''' Kegiatan '''

def kegiatan_list(request):
    kegiatan = Kegiatan.objects.all()
    return render(request, 'home/kegiatan_list.html', {'kegiatan': kegiatan})

def kegiatan_create(request):
    if request.method == 'POST':
        form = KegiatanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('kegiatan_list')
    else:
        form = KegiatanForm()
    return render(request, 'home/kegiatan_form.html', {'form': form})

def kegiatan_update(request, pk):
    kegiatan = Kegiatan.objects.get(pk=pk)
    if request.method == 'POST':
        form = KegiatanForm(request.POST, request.FILES, instance=kegiatan)
        if form.is_valid():
            form.save()
            return redirect('kegiatan_list')
    else:
        form = KegiatanForm(instance=kegiatan)
    return render(request, 'home/kegiatan_form.html', {'form': form})

def kegiatan_delete(request, pk):
    kegiatan = Kegiatan.objects.get(pk=pk)
    if request.method == 'POST':
        kegiatan.delete()
        return redirect('kegiatan_list')
    return render(request, 'home/kegiatan_confirm_delete.html', {'kegiatan': kegiatan})
''' end Kegiatan '''