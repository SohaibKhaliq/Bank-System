from django.db import models
from django.conf import settings


class Bank(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    routing_number = models.CharField(max_length=64)
    account_number = models.CharField(max_length=64)
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.account_number[-4:]}"


class Card(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    name_on_card = models.CharField(max_length=255)
    card_number = models.CharField(max_length=32)
    expiration = models.CharField(max_length=8)
    cvc = models.CharField(max_length=8)
    postal_code = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name_on_card} - ****{self.card_number[-4:]}"


class Wallet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name} ({self.balance})"


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_TYPES = (('income', 'Income'), ('expense', 'Expense'), ('transfer', 'Transfer'))
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} {self.amount}"


class SupportTicket(models.Model):
    STATUS = (('open', 'Open'), ('in_progress', 'In Progress'), ('closed', 'Closed'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.status}"
