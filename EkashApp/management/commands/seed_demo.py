from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from EkashApp.models import Wallet, Card, Category, Transaction
import random
from django.utils import timezone


class Command(BaseCommand):
    help = 'Seed demo data: user, wallets, cards, categories, transactions'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='demo').exists():
            user = User.objects.create_user('demo', 'demo@example.com', 'demopassword')
            user.first_name = 'Demo'
            user.last_name = 'User'
            user.save()
            self.stdout.write(self.style.SUCCESS('Created demo user: demo / demopassword'))
        else:
            user = User.objects.get(username='demo')
            self.stdout.write('Demo user already exists')

        # wallets
        wallets = []
        for name in ['City Bank', 'Debit Card', 'Visa Card', 'Cash']:
            w, created = Wallet.objects.get_or_create(user=user, name=name, defaults={'balance': random.randint(1000, 200000)})
            wallets.append(w)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created wallet {name}'))

        # cards
        for i in range(2):
            num = ''.join(str(random.randint(0, 9)) for _ in range(16))
            Card.objects.get_or_create(user=user, card_number=num, defaults={'name_on_card': f'Demo Card {i+1}', 'expiration': '12/30', 'cvc': '123'})
        self.stdout.write(self.style.SUCCESS('Ensured demo cards exist'))

        # categories
        cat_names = ['Beauty', 'Bills & Fees', 'Car', 'Education', 'Entertainment', 'Groceries']
        categories = []
        for name in cat_names:
            c, _ = Category.objects.get_or_create(name=name)
            categories.append(c)

        # transactions
        now = timezone.now()
        for w in wallets:
            for _ in range(8):
                amt = round(random.uniform(5, 500), 2)
                t = Transaction.objects.create(
                    wallet=w,
                    amount=amt if random.choice([True, False]) else -amt,
                    type='income' if random.choice([True, False]) else 'expense',
                    category=random.choice(categories),
                    description='Demo transaction',
                )
        self.stdout.write(self.style.SUCCESS('Created demo transactions'))
