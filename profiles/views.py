from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

def profile(request):
    
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your personal profile has successfully changed')
        else:
            messages.error(request, 'There is a problem. Please make sure it is done properly')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'upgraded_page': True
    }

    return render(request, template, context)

def product_history(request, product_number):
    order = get_object_or_404(Order, product_number=product_number)

    messages.info(request, (
        f'This is the old product number confirmation{product_number}.'
        'A message will be sent to you on your email confirming the purchase'
    ))

    template = 'checkout/purchase_success.html'
    context = {
        'order': order,
        'sent_profile': True,
    }

    return render(request, template, context)