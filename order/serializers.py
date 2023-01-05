from rest_framework import serializers
from django.db.models import Sum
from django.db.models import FloatField, F
from django.db.models.functions import Coalesce
from .models import Order, UserProfile
from order.functions import crypto_price, buy_from_exchange


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'user', 'crypto_name', 'crypto_volume',)

    def create(self, validated_data):
        # order price
        crypto_name = validated_data['crypto_name']
        crypto_volume = validated_data['crypto_volume']
        unit_price = crypto_price(crypto_name)
        price = crypto_volume * unit_price
        # create order
        order = Order.objects.create(**validated_data)
        order.save()
        # user wallet
        new_amount = order.user.wallet_amount - price
        UserProfile.objects.filter(id=order.user.id).update(wallet_amount=new_amount)
        # buy_from_exchange
        if price >= 10:
            buy_from_exchange(crypto_name, price)
            order.is_bought = True
            order.save()
        else:
            not_purchased_order = Order.objects.filter(is_bought=False)
            orders_price = not_purchased_order.aggregate(
                total_price=Sum(F('crypto_volume')*unit_price, output_field=FloatField()))['total_price']
            if orders_price >= 10:
                buy_from_exchange(crypto_name, orders_price)
                not_purchased_order.update(is_bought=True)

        return order
