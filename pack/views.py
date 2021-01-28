from django.shortcuts import render

# Create your views here.

def view_pack(request):
    return render(request, 'pack/pack.html')
