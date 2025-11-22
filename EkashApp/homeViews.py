from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import BankForm, CardForm, SignUpForm, SignInForm
from .models import Bank, Card

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
    data = {
        'title': 'Add Bank',
        'subTitle': 'Add Bank',
    }
    return render(request, "home/wallets.html", data)
    