from django.conf import settings
from django.db import models
from django.utils.functional import cached_property
from mainapp.models import Product


class BasketQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    objects = BasketQuerySet.as_manager()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0,
    )
    add_datetime = models.DateTimeField(
        verbose_name='время добавления',
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.quantity} - {self.add_datetime}'

    @cached_property
    def get_items_cached(self):
        return self.user.basket.select_related()

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        _items = self.get_items_cached
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity

    @property
    def total_cost(self):
        _items = self.get_items_cached
        _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return _totalcost
