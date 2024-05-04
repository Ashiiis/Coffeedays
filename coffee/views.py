from django.shortcuts import render, redirect
from .models import CartItem
import requests
from .payment import generate_checksum
from django.shortcuts import render


def home(request):
     products =CartItem.objects.all()
     return render(request,'coffee/home.html', {'products': products})

def add_to_cart(request, product_id):
    # Retrieve the product details based on the product_id (You'll need to implement this part)
    product_name = product_name
    product_price = product_price

    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(product_id=product_id, defaults={'product_name': product_name, 'product_price': product_price})

    # If the product is already in the cart, increase the quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    #return render(request,'coffee/home.html', {'coffee': CartItem})
    return redirect('home') 
# def view_cart(request):
#     cart_items = CartItem.objects.all()
#     total_amount = sum(item.subtotal() for item in cart_items)

#     return render(request, 'coffee/cart.html', {'cart_items': cart_items, 'total_amount': total_amount})



def initiate_payment(request):
    # Logic to initiate payment with Paytm API
    # Use your Paytm credentials and construct the payment request
    paytm_params = {
        'MID': 'your_merchant_id',
        'WEBSITE': 'WEBSTAGING',
        'INDUSTRY_TYPE_ID': 'Retail',
        'CHANNEL_ID': 'WEB',
        # ... other required parameters
    }

    paytm_params['CHECKSUMHASH'] = generate_checksum(paytm_params)  # You need to implement this function

    return render(request, 'coffee/payment.html', {'paytm_params': paytm_params})