from django.shortcuts import get_object_or_404, redirect, render
from webapp.forms import AddToCartForm
from webapp.models import Product


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart = request.session.get('cart', {})
            if str(product.pk) in cart:
                cart[str(product.pk)] += quantity
            else:
                cart[str(product.pk)] = quantity
            request.session['cart'] = cart
            return redirect('index')
    else:
        form = AddToCartForm()

    return render(request, 'add_cart.html', {'form': form})