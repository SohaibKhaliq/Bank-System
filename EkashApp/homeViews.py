from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import BankForm, CardForm, SignUpForm, SignInForm
from .models import Bank, Card
from django.shortcuts import get_object_or_404
from .forms import WalletForm, TransactionForm, SupportTicketForm
from .models import Wallet, Transaction, SupportTicket
from django.db import transaction as db_transaction
from django.db import models
from datetime import timedelta

def index2(request):
    data = {
        'title':'About Us',
        'subTitle':'About Us',
    }
    return render(request,"home/index2.html",data)

def addBank(request):
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            bank = form.save(commit=False)
            if request.user.is_authenticated:
                bank.user = request.user
            bank.save()
            messages.success(request, 'Bank added successfully.')
            return redirect(reverse('bankAddSuccessful'))
    else:
        form = BankForm()

    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
        'form': form,
    }
    return render(request, "home/addBank.html", data)
    
def addCard(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            if request.user.is_authenticated:
                card.user = request.user
            card.save()
            messages.success(request, 'Card added successfully.')
            return redirect(reverse('bankAddSuccessful'))
    else:
        form = CardForm()

    data = {
        'title': 'Add Card',
        'subTitle': 'Add Card',
        'form': form,
    }
    return render(request, "home/addCard.html", data)
    
def addNewAccount(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/addNewAccount.html", data)
    
def affiliates(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/affiliates.html", data)
    
def analytics(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/analytics.html", data)
    
def analyticsBalance(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/analyticsBalance.html", data)
    
def analyticsExpenses(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/analyticsExpenses.html", data)
    
def analyticsIncome(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/analyticsIncome.html", data)
    
def analyticsIncomeVsExpenses(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/analyticsIncomeVsExpenses.html", data)
    
def analyticsTransactionHistory(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/analyticsTransactionHistory.html", data)
    
def bankAddSuccessful(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/bankAddSuccessful.html", data)


def bank_list(request):
    # show banks for the logged-in user; staff see all
    if request.user.is_authenticated and request.user.is_staff:
        banks = Bank.objects.all().order_by('-created_at')
    elif request.user.is_authenticated:
        banks = Bank.objects.filter(user=request.user).order_by('-created_at')
    else:
        banks = Bank.objects.none()

    return render(request, 'home/banks_list.html', {'banks': banks, 'title': 'My Banks'})


def bank_edit(request, pk=None):
    if pk:
        bank = get_object_or_404(Bank, pk=pk)
        if request.method == 'POST':
            form = BankForm(request.POST, instance=bank)
            if form.is_valid():
                form.save()
                messages.success(request, 'Bank updated.')
                return redirect(reverse('bank_list'))
        else:
            form = BankForm(instance=bank)
    else:
        if request.method == 'POST':
            form = BankForm(request.POST)
            if form.is_valid():
                bank = form.save(commit=False)
                if request.user.is_authenticated:
                    bank.user = request.user
                bank.save()
                messages.success(request, 'Bank created.')
                return redirect(reverse('bank_list'))
        else:
            form = BankForm()

    return render(request, 'home/bank_form.html', {'form': form})


def bank_delete(request, pk):
    bank = get_object_or_404(Bank, pk=pk)
    if request.method == 'POST':
        bank.delete()
        messages.success(request, 'Bank deleted.')
        return redirect(reverse('bank_list'))
    return render(request, 'home/bank_confirm_delete.html', {'bank': bank})


def card_list(request):
    if request.user.is_authenticated and request.user.is_staff:
        cards = Card.objects.all().order_by('-created_at')
    elif request.user.is_authenticated:
        cards = Card.objects.filter(user=request.user).order_by('-created_at')
    else:
        cards = Card.objects.none()
    return render(request, 'home/cards_list.html', {'cards': cards, 'title': 'My Cards'})


def card_edit(request, pk=None):
    if pk:
        card = get_object_or_404(Card, pk=pk)
        if request.method == 'POST':
            form = CardForm(request.POST, instance=card)
            if form.is_valid():
                form.save()
                messages.success(request, 'Card updated.')
                return redirect(reverse('card_list'))
        else:
            form = CardForm(instance=card)
    else:
        if request.method == 'POST':
            form = CardForm(request.POST)
            if form.is_valid():
                card = form.save(commit=False)
                if request.user.is_authenticated:
                    card.user = request.user
                card.save()
                messages.success(request, 'Card created.')
                return redirect(reverse('card_list'))
        else:
            form = CardForm()

    return render(request, 'home/card_form.html', {'form': form})


def card_delete(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        card.delete()
        messages.success(request, 'Card deleted.')
        return redirect(reverse('card_list'))
    return render(request, 'home/card_confirm_delete.html', {'card': card})


def wallet_list(request):
    if request.user.is_authenticated and request.user.is_staff:
        wallets = Wallet.objects.all().order_by('-id')
    elif request.user.is_authenticated:
        wallets = Wallet.objects.filter(user=request.user).order_by('-id')
    else:
        wallets = Wallet.objects.none()
    return render(request, 'home/wallets_list.html', {'wallets': wallets, 'title': 'Wallets'})


def wallet_edit(request, pk=None):
    if pk:
        wallet = get_object_or_404(Wallet, pk=pk)
        if request.method == 'POST':
            form = WalletForm(request.POST, instance=wallet)
            if form.is_valid():
                form.save()
                messages.success(request, 'Wallet updated.')
                return redirect(reverse('wallet_list'))
        else:
            form = WalletForm(instance=wallet)
    else:
        # creating a new wallet requires an authenticated user
        if not request.user.is_authenticated:
            messages.error(request, 'You must be signed in to create a wallet.')
            return redirect(reverse('signin'))

        if request.method == 'POST':
            form = WalletForm(request.POST)
            if form.is_valid():
                wallet = form.save(commit=False)
                # At this point request.user is authenticated (checked above)
                wallet.user = request.user
                wallet.save()
                messages.success(request, 'Wallet created.')
                return redirect(reverse('wallet_list'))
        else:
            form = WalletForm()

    return render(request, 'home/wallet_form.html', {'form': form})


def wallet_delete(request, pk):
    wallet = get_object_or_404(Wallet, pk=pk)
    if request.method == 'POST':
        wallet.delete()
        messages.success(request, 'Wallet deleted.')
        return redirect(reverse('wallet_list'))
    return render(request, 'home/wallet_confirm_delete.html', {'wallet': wallet})


def transaction_list(request):
    if request.user.is_authenticated and request.user.is_staff:
        transactions = Transaction.objects.select_related('wallet', 'category').all().order_by('-date')
    elif request.user.is_authenticated:
        transactions = Transaction.objects.select_related('wallet', 'category').filter(wallet__user=request.user).order_by('-date')
    else:
        transactions = Transaction.objects.none()
    return render(request, 'home/transactions_list.html', {'transactions': transactions})


def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            with db_transaction.atomic():
                tx = form.save()
                # adjust wallet balance
                wallet = tx.wallet
                if tx.type == 'income':
                    wallet.balance = wallet.balance + tx.amount
                elif tx.type == 'expense':
                    wallet.balance = wallet.balance - tx.amount
                # transfer logic can be added later
                wallet.save()
            messages.success(request, 'Transaction recorded.')
            return redirect(reverse('transaction_list'))
    else:
        # restrict wallet choices to user's wallets
        form = TransactionForm()
        if request.user.is_authenticated and not request.user.is_staff:
            form.fields['wallet'].queryset = Wallet.objects.filter(user=request.user)

    return render(request, 'home/transaction_form.html', {'form': form})


def support_tickets_list(request):
    if request.user.is_authenticated and request.user.is_staff:
        tickets = SupportTicket.objects.all().order_by('-created_at')
    elif request.user.is_authenticated:
        tickets = SupportTicket.objects.filter(user=request.user).order_by('-created_at')
    else:
        tickets = SupportTicket.objects.none()
    return render(request, 'home/support_tickets_list.html', {'tickets': tickets})


def support_ticket_create(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            if request.user.is_authenticated:
                ticket.user = request.user
            ticket.save()
            messages.success(request, 'Support ticket submitted.')
            return redirect(reverse('support_tickets_list'))
    else:
        form = SupportTicketForm()
    return render(request, 'home/support_ticket_form.html', {'form': form})
    
def blank(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/blank.html", data)
    
def budgets(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/budgets.html", data)
    
def chart(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/chart.html", data)
    
def demo(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/demo.html", data)
    
def goals(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/goals.html", data)
    
def idFrontAndBackUpload(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/idFrontAndBackUpload.html", data)
    
def index(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/index.html", data)
    
def locked(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/locked.html", data)
    
def notifications(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/notifications.html", data)
    
def otpCode(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/otpCode.html", data)
    
def otpPhone(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/otpPhone.html", data)
    
def pageError(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/pageError.html", data)
    
def privacy(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/privacy.html", data)
    
def profile(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/profile.html", data)
    
def reset(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/reset.html", data)
    
def settings(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/settings.html", data)
    
def settingsApi(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/settingsApi.html", data)
    
def settingsBank(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/settingsBank.html", data)
    
def settingsCategories(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/settingsCategories.html", data)
    
def settingsCurrencies(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/settingsCurrencies.html", data)
    
def settingsGeneral(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/settingsGeneral.html", data)
    
def settingsProfile(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/settingsProfile.html", data)
    
def settingsSecurity(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/settingsSecurity.html", data)
    
def settingsSession(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/settingsSession.html", data)
    
def signin(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = SignInForm()

    data = {
        'title': 'Sign In',
        'subTitle': 'Sign In',
        'form': form,
    }
    return render(request, "home/signin.html", data)
    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            # auto-login
            user = authenticate(username=user.username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('index'))
            return redirect(reverse('signin'))
    else:
        form = SignUpForm()

    data = {
        'title': 'Sign Up',
        'subTitle': 'Sign Up',
        'form': form,
    }
    return render(request, "home/signup.html", data)
    
def support(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/support.html", data)
    
def supportCreateTicket(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/supportCreateTicket.html", data)
    
def supportTicketDetails(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/supportTicketDetails.html", data)
    
def supportTickets(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/supportTickets.html", data)
    
def verifiedId(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/verifiedId.html", data)
    
def verifyEmail(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/verifyEmail.html", data)
    
def verifyId(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/verifyId.html", data)
    
def verifyingId(request):
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/verifyingId.html", data)
    
def wallets(request):
    # Prepare dynamic data for wallets page
    user = request.user if request.user.is_authenticated else None
    if user and user.is_staff:
        wallets_qs = Wallet.objects.all().order_by('-id')
    elif user:
        wallets_qs = Wallet.objects.filter(user=user).order_by('-id')
    else:
        wallets_qs = Wallet.objects.none()

    # selected wallet via GET param or first wallet
    selected_wallet_id = request.GET.get('wallet')
    selected_wallet = None
    if selected_wallet_id:
        try:
            selected_wallet = wallets_qs.get(pk=int(selected_wallet_id))
        except Exception:
            selected_wallet = None
    if not selected_wallet:
        selected_wallet = wallets_qs.first()

    # transactions for selected wallet
    transactions = Transaction.objects.filter(wallet=selected_wallet).order_by('-date') if selected_wallet else []

    # totals
    total_balance = wallets_qs.aggregate(models.Sum('balance'))['balance__sum'] or 0
    personal_funds = selected_wallet.balance if selected_wallet else 0
    # credit limits: sum placeholder (no credit_limit field on Card model)
    credit_limits = 0

    # monthly expenses (current month) for selected wallet
    from django.utils import timezone
    now = timezone.now()
    start_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    monthly_expenses = Transaction.objects.filter(wallet=selected_wallet, type='expense', date__gte=start_month).aggregate(models.Sum('amount'))['amount__sum'] or 0

    # balance overtime data (last 6 months): compute cumulative net per month
    from django.db.models import Sum
    labels = []
    data_points = []
    # start 5 months ago
    months = []
    for i in range(5, -1, -1):
        m = (now.replace(day=1) - timedelta(days=30*i))
        months.append(m)
    cumulative = 0
    for m in months:
        month_start = m.replace(day=1)
        # month end: next month start
        if m.month == 12:
            next_month = m.replace(year=m.year+1, month=1, day=1)
        else:
            next_month = m.replace(month=m.month+1, day=1)
        net = Transaction.objects.filter(wallet=selected_wallet, date__gte=month_start, date__lt=next_month).aggregate(Sum('amount'))['amount__sum'] or 0
        cumulative += net
        labels.append(month_start.strftime('%b %Y'))
        data_points.append(float(cumulative))

    context = {
        'title': 'Wallets',
        'wallets': wallets_qs,
        'selected_wallet': selected_wallet,
        'transactions': transactions,
        'total_balance': total_balance,
        'personal_funds': personal_funds,
        'credit_limits': credit_limits,
        'monthly_expenses': monthly_expenses,
        'chart_labels': labels,
        'chart_data': data_points,
    }
    return render(request, "home/wallets.html", context)
    