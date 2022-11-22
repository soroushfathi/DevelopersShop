from home.models import Variant

CART_SESSION_ID = 'cart'


class Carts:
    def __init__(self, request):
        """
        :param self.cart: json file contains all sessions
        :param request:
        """
        self.session = request.session  # get all sessions
        cart = request.session.get(CART_SESSION_ID)
        if not cart:  # if still have not created cart session
            # create 'cart' session in all sessions
            self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, variant, quan):
        variant_id = str(variant.id)
        if variant_id not in self.cart:
            self.cart[variant_id] = {'quantity': quan, 'price': str(variant.unit_price)}
        self.cart[variant_id]['quantity'] += quan
        self.save()

    def remove(self):
        variant_id = str(variant.id)
        if variant_id in self.cart:
            del self.cart[variant_id]
        self.save()

    def remove_all(self):
        self.session[CART_SESSION_ID] = {}

    def save(self):
        self.session.modified = True

    def total_price(self):
        return sum([int(v['price']) * int(v['quantity']) for v in self.cart.values()])

    def __iter__(self):
        variant_ids = self.cart.keys()
        variants = Variant.objects.filter(id__in=variant_ids)
        for variant in variants:
            self.cart[str(variant.id)]['variant'] = variant

        for v in self.cart.values():
            yield int(v['price']) * int(v['quantity'])
