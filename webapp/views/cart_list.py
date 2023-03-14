from _decimal import Decimal

from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView


from webapp.models import Product


class CartView(ListView):
    template_name = 'cart.html'
    context_object_name = 'cart_lines'

    def get_queryset(self):
        cart = self.request.session.get('cart', {})
        cart_lines = []
        cart_total = Decimal(0)
        for pk, quantity in cart.items():
            product = get_object_or_404(Product, pk=pk)
            cart_lines.append({
                'product': product,
                'quantity': quantity,
                'amount': product.cost * quantity
            })
            cart_total += product.cost * quantity
        return cart_lines

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_total'] = Decimal(0)
        for cart_line in context['cart_lines']:
            context['cart_total'] += cart_line['amount']
        return context


class CartLineDeleteView(DeleteView):
    template_name = 'cart_line_delete.html'
    model = Product
    success_url = reverse_lazy('cart')

    def post(self, request, pk):
        cart = request.session.get('cart', {})
        if str(pk) in cart:
            del cart[str(pk)]
            request.session['cart'] = cart
        return redirect('cart')