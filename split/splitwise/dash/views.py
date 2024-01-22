from django.http import Http404
from django.shortcuts import render
from django.db.models import Q


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ExpenseForm
from .models import Expense, Group, Settlement

# @login_required
# def dashboard(request):
#     user = request.user
#     expenses = Expense.objects.filter(participants=user)
#     settlements = Settlement.objects.filter(Q(payer=user) | Q(receiver=user))
#     groups = Group.objects.all()
#     # settlements = Settlement.objects.filter(user=user)
#     context = {
#         'expenses': expenses,
#         'settlements': settlements,
#         'groups': groups
#     }
#     return render(request, 'dashboard.html', context)


@login_required
def dashboard(request):
    user = request.user
    expenses = Expense.objects.filter(participants=user)
    settlements = Settlement.objects.filter(Q(payer=user) | Q(receiver=user))
    groups = Group.objects.all()
    group_id = request.GET.get('group_id')
    context = {
        'expenses': expenses,
        'settlements': settlements,
        'groups': groups,
        'group_id': group_id,  # Pass the group_id to the template context
    }
    return render(request, 'dashboard.html', context)

@login_required
def create_expense(request):
    user = request.user
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.paid_by = user
            expense.save()
            form.save_m2m()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    context = {
        'form': form
    }
    return render(request, 'create_expense.html', context)

@login_required
def create_group(request):
    user = request.user
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group = Group.objects.create(name=group_name)
        group.members.add(user)
        group.save()
        return redirect('dashboard')
    return render(request, 'create_group.html')


@login_required
def add_group_member(request, group_id):
    try:
        group = Group.objects.get(id=group_id)
    except Group.DoesNotExist:
        raise Http404("Group does not exist")

    if request.method == 'POST':
        member_email = request.POST.get('member_email')
        # Check if the member email is valid and exists in the system
        # Add the member to the group if valid
        # Example: group.members.add(member)
        return redirect('group_details', group_id=group_id)

    context = {
        'group': group
    }
    return render(request, 'add_group_member.html', context)
# @login_required
# def add_group_member(request,group_id):
#     group = Group.objects.get(id=group_id)
#     if request.method == 'POST':
#         member_email = request.POST.get('member_email')
#         # Check if the member email is valid and exists in the system
#         # Add the member to the group if valid
#         # Example: group.members.add(member)
#         return redirect('group_details',group_id)
#     return render(request, 'add_group_member.html', {'group': group})

# @login_required
# def group_details(request, group_id):
#     group = Group.objects.get(id=group_id)
#     expenses = Expense.objects.filter(group=group)
#     context = {
#         'group': group,
#         'expenses': expenses
#     }
#     return render(request, 'group_details.html', context)
@login_required
def group_details(request,group_id):
    try:
        group = Group.objects.get(id=group_id)
    except Group.DoesNotExist:
        raise Http404("Group does not exist")

    expenses = Expense.objects.filter(group=group)
    context = {
        'group': group,
        'expenses': expenses
    }
    return render(request, 'group_details.html', context)

@login_required
def settle_expense(request, expense_id):
    
    expense = Expense.objects.get(id=expense_id)
   
    return redirect('dashboard')
