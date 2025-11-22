from django.contrib import admin
from .models import Bank, Card, Wallet, Transaction, Category, SupportTicket


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'account_number', 'routing_number', 'user', 'created_at')
    search_fields = ('full_name', 'account_number', 'routing_number')


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name_on_card', 'card_number', 'user', 'created_at')
    search_fields = ('name_on_card', 'card_number')


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'balance')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'amount', 'type', 'date')
    list_filter = ('type',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user', 'status', 'created_at')
    list_filter = ('status',)
