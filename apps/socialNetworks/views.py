from django.shortcuts import render, redirect, get_object_or_404

from .forms import SocialNetworkForm
from .models import SocialNetwork

# Create your views here.

def add_socialNetwork(request):
    template_name = 'socialNetworks/add_socialNetwork.html'
    context = {}
    if request.method == 'POST':
        form = SocialNetworkForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('socialNetworks:list_socialNetworks')
    form = SocialNetworkForm()
    context['form'] = form
    return render(request, template_name, context)

def list_socialNetworks(request):
    template_name = 'socialNetworks/list_socialNetworks.html'
    socialNetworks = SocialNetwork.objects.filter()
    context = {
        'socialNetworks': socialNetworks
    }
    return render(request, template_name, context)

def edit_socialNetwork(request, id_socialNetwork):
    template_name = 'socialNetworks/add_socialNetwork.html'
    context ={}
    socialNetwork = get_object_or_404(SocialNetwork, id=id_socialNetwork)
    if request.method == 'POST':
        form = SocialNetworkForm(request.POST, instance=socialNetwork)
        if form.is_valid():
            form.save()
            return redirect('socialNetworks:list_socialNetworks')
    form = SocialNetworkForm(instance=socialNetwork)
    context['form'] = form
    return render(request, template_name, context)

def delete_socialNetwork(request, id_socialNetwork):
    socialNetwork = SocialNetwork.objects.get(id=id_socialNetwork)
    socialNetwork.delete()
    return redirect('socialNetworks:list_socialNetworks')