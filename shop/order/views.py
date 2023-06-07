from django.shortcuts import render, redirect
from book.models import Book
from order.forms import OrderAddressForm
from order.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from order.tasks import send_order_confirmation_email


@login_required(login_url="/account/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Book.objects.get(id=id)
    cart.add(product=product)
    return redirect("order:cart_detail")


@login_required(login_url="/account/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Book.objects.get(id=id)
    cart.remove(product)
    return redirect("order:cart_detail")


@login_required(login_url="/account/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Book.objects.get(id=id)
    cart.add(product=product)
    return redirect("order:cart_detail")


@login_required(login_url="/account/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Book.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("order:cart_detail")


@login_required(login_url="/account/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("order:cart_detail")


@login_required(login_url="/account/login")
def cart_detail(request):
    return render(request, 'order/cart_detail.html')


@login_required(login_url="/account/login")
def address_confirmation(request):
    if request.method == 'POST':
        form = OrderAddressForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(user=request.user, status=Order.OrderStatus.ORDER,
                                         delivery_address=form.cleaned_data.get('delivery_address'))
            cart = request.session.get('cart', None)
            for key, value in cart.items():
                book = Book.objects.get(id=value.get('product_id'))
                OrderItem.objects.create(order=order, book=book, quantity=value.get('quantity'))
            cart = Cart(request)
            cart.clear()
            send_order_confirmation_email.delay(order.user.email)
            return redirect('book:book_list')
    else:
        form = OrderAddressForm()
    return render(request, 'order/order_address.html', {'form': form})
