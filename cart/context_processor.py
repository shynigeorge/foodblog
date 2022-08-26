from cart.models import CartList, Items
from cart.views import cart_id


def count(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct=CartList.objects.filter(cart_id=cart_id(request))
            cti=Items.objects.all().filter(cart=ct[:1])
            for c in cti:
                item_count+=c.quantity
        except CartList.DoesNotExist:
            item_count=0
        return dict(itc=item_count)


