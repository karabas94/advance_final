from store.models import Order


def delete_related_book_items(sender, instance, created, **kwargs):
    if instance.status == Order.OrderStatus.SUCCESS:
        order_items = instance.orderitem_set.all()
        for order_item in order_items:
            book_items = order_item.book_item.all()
            for book_item in book_items:
                book_item.delete()


