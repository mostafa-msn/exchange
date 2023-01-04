from django.db import models
from django.utils.translation import gettext_lazy as _
from lib.common_model import BaseModel
from exchange.enums import CryptoChoices


class UserProfile(BaseModel):
    username = models.CharField(
        _("username"), unique=True, max_length=32)
    wallet_amount = models.FloatField(_("wallet_amount"),)

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")


class Order(BaseModel):
    user = models.ForeignKey(
        UserProfile, verbose_name=_("user"), on_delete=models.CASCADE,
        related_name="user_profile"
    )
    crypto_name = models.CharField(
        _("sum_label"), choices=CryptoChoices.choices, max_length=10
    )
    crypto_volume = models.FloatField(_("crypto_volume"),)
    is_bought = models.BooleanField(_("is_bought"), default=False)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
