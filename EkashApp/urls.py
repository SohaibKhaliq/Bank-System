"""
URL configuration for Ekash project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from EkashApp import homeViews

urlpatterns = [

    # Home
    path('', homeViews.index, name ='index'),
    path('add-bank', homeViews.addBank, name ='addBank'),
    path('add-card', homeViews.addCard, name ='addCard'),
    path('add-new-account', homeViews.addNewAccount, name ='addNewAccount'),
    path('affiliates', homeViews.affiliates, name ='affiliates'),
    path('analytics', homeViews.analytics, name ='analytics'),
    path('analytics-balance', homeViews.analyticsBalance, name ='analyticsBalance'),
    path('analytics-expenses', homeViews.analyticsExpenses, name ='analyticsExpenses'),
    path('analytics-income', homeViews.analyticsIncome, name ='analyticsIncome'),
    path('analytics-income-vs-expenses', homeViews.analyticsIncomeVsExpenses, name ='analyticsIncomeVsExpenses'),
    path('analytics-transaction-history', homeViews.analyticsTransactionHistory, name ='analyticsTransactionHistory'),
    path('bank-add-successful', homeViews.bankAddSuccessful, name ='bankAddSuccessful'),
    path('blank', homeViews.blank, name ='blank'),
    path('budgets', homeViews.budgets, name ='budgets'),
    path('chart', homeViews.chart, name ='chart'),
    path('demo', homeViews.demo, name ='demo'),
    path('goals', homeViews.goals, name ='goals'),
    path('id-front-and-back-upload', homeViews.idFrontAndBackUpload, name ='idFrontAndBackUpload'),
    path('index', homeViews.index, name ='index'),
    path('locked', homeViews.locked, name ='locked'),
    path('notifications', homeViews.notifications, name ='notifications'),
    path('otp-code', homeViews.otpCode, name ='otpCode'),
    path('otp-phone', homeViews.otpPhone, name ='otpPhone'),
    path('page-error', homeViews.pageError, name ='pageError'),
    path('privacy', homeViews.privacy, name ='privacy'),
    path('profile', homeViews.profile, name ='profile'),
    path('reset', homeViews.reset, name ='reset'),
    path('settings', homeViews.settings, name ='settings'),
    path('settings-api', homeViews.settingsApi, name ='settingsApi'),
    path('settings-bank', homeViews.settingsBank, name ='settingsBank'),
    path('settings-categories', homeViews.settingsCategories, name ='settingsCategories'),
    path('settings-currencies', homeViews.settingsCurrencies, name ='settingsCurrencies'),
    path('settings-general', homeViews.settingsGeneral, name ='settingsGeneral'),
    path('settings-profile', homeViews.settingsProfile, name ='settingsProfile'),
    path('settings-security', homeViews.settingsSecurity, name ='settingsSecurity'),
    path('settings-session', homeViews.settingsSession, name ='settingsSession'),
    path('signin', homeViews.signin, name ='signin'),
    path('signup', homeViews.signup, name ='signup'),
    path('support', homeViews.support, name ='support'),
    path('support-create-ticket', homeViews.supportCreateTicket, name ='supportCreateTicket'),
    path('support-ticket-details', homeViews.supportTicketDetails, name ='supportTicketDetails'),
    path('support-tickets', homeViews.supportTickets, name ='supportTickets'),
    path('verified-id', homeViews.verifiedId, name ='verifiedId'),
    path('verify-email', homeViews.verifyEmail, name ='verifyEmail'),
    path('verify-id', homeViews.verifyId, name ='verifyId'),
    path('verifying-id', homeViews.verifyingId, name ='verifyingId'),
    path('wallets', homeViews.wallets, name ='wallets'),
    # Banks CRUD
    path('banks', homeViews.bank_list, name='bank_list'),
    path('banks/<int:pk>/edit', homeViews.bank_edit, name='bank_edit'),
    path('banks/<int:pk>/delete', homeViews.bank_delete, name='bank_delete'),
    # Cards CRUD
    path('cards', homeViews.card_list, name='card_list'),
    path('cards/<int:pk>/edit', homeViews.card_edit, name='card_edit'),
    path('cards/<int:pk>/delete', homeViews.card_delete, name='card_delete'),
    # Wallets & Transactions
    path('wallets', homeViews.wallet_list, name='wallet_list'),
    path('wallets/add', homeViews.wallet_edit, name='wallet_add'),
    path('wallets/<int:pk>/edit', homeViews.wallet_edit, name='wallet_edit'),
    path('wallets/<int:pk>/delete', homeViews.wallet_delete, name='wallet_delete'),
    path('transactions', homeViews.transaction_list, name='transaction_list'),
    path('transactions/add', homeViews.transaction_create, name='transaction_add'),

    # Support tickets
    path('support-tickets', homeViews.support_tickets_list, name='support_tickets_list'),
    path('support-tickets/add', homeViews.support_ticket_create, name='support_ticket_add'),
]
