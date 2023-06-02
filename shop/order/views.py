from django.shortcuts import render, redirect
from book.models import Book
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

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
