from django.urls import path
from django.http import HttpRequest
from . import views
from django.shortcuts import redirect


def redir(request):
    req = request.path
    print(req)
    if req == '/a/':
        return redirect('alogin')


urlpatterns = [
    path('', redir),
    path('login', views.login_verif, name='alogin'),
    path('forgot', views.login_forgot, name='forgot'),
    path('logout', views.logout_view, name='alogout'),
    path('dashboard', views.dashboard, name='adashboard'),
    path('sessions', views.sessions, name='asessions'),
    path('stations', views.stations, name='stations'),
    path('payments', views.history, name='apayment'),
    path('payments/input', views.payment_input, name='apaymentInput'),
    path('payments/input/submit', views.payment_submit, name='apaymentSubmit'),
    path('accounts', views.account, name='aaccount'),
    path('accounts/account', views.account_edit, name='aaccountEdit'),
    path('users/profile', views.account_edit, name='aaccountEdit'),
    path('users/add', views.add_user, name='aaccountAdd'),

    path('users/account', views.user_account, name='user_account'),
    path('users/security', views.user_security, name='user_security'),
    path('users/billing-plans', views.user_billing_plans, name='user_billing_plans'),
    path('users/notifications', views.user_notifications, name='user_notifications'),

    path('routers', views.routers, name='routers'),
    path('networking/ip_networks', views.ip_networks, name='ip_networks'),
    path('networking/ip_pools', views.ip_pools, name='ip_pools'),


    path('packages', views.packages, name='apackages'),
    path('sessions/mod', views.sessionMod, name='asessionMod'),


    # invoices
    path('invoices', views.invoices, name='invoices'),
    path('invoices/add', views.invoices_add, name='invoices_add'),
    path('invoices/edit', views.invoices_edit, name='invoices_edit'),
    path('invoices/preview', views.invoices_preview, name='invoices_preview'),
    path('invoices/print', views.invoices_print, name='invoices_print'),
    path('invoices/delete', views.invoices_delete, name='invoices_delete'),


    path('profile', views.profile, name='profile'),

    # crm
    # path('lead-sources', views.lead_sources, name='lead-sources'),
    # path('custom-fields', views.invoices_add, name='invoices_add'),
    # path('pipe-linestages', views.invoices_edit, name='invoices_edit'),
    # path('invoices/preview', views.invoices_preview, name='invoices_preview'),
    # path('invoices/print', views.invoices_print, name='invoices_print'),
    # path('invoices/delete', views.invoices_delete, name='invoices_delete'),
    # users
    path('access_roles', views.roles, name='roles'),
    path('access_permissions', views.permissions, name='permissions'),
    # path('users/add', views.invoices_add, name='ainvoices_add'),
    # path('users/edit', views.invoices_edit, name='ainvoices_edit'),
    # path('users/view', views.invoices_preview, name='ainvoices_preview'),
    # path('users/delete', views.invoices_delete, name='ainvoices_delete'),

]
