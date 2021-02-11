from django.shortcuts import render, redirect

# Create your views here.

def view_pack(request):
    return render(request, 'pack/pack.html')

def put_to_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    pack = request.session.get('bag', {})

    if item_id in list(pack.keys()):
        pack[item_id] += quantity
    else:
        pack[item_id] = quantity

    request.session['pack'] = pack
    return redirect(redirect_url)
