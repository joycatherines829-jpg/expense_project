from django.shortcuts import render, redirect
from .models import Expense


def home(request):
    expenses = Expense.objects.all()
    total = sum(expense.amount for expense in expenses)

    if request.method == 'POST':
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        Expense.objects.create(title=title, amount=amount)
        return redirect('home')

    return render(request, 'home.html', {
        'expenses': expenses,
        'total': total
    })


def delete_expense(request, id):
    expense = Expense.objects.get(id=id)
    expense.delete()
    return redirect('home')


def edit_expense(request, id):
    expense = Expense.objects.get(id=id)

    if request.method == 'POST':
        expense.title = request.POST.get('title')
        expense.amount = request.POST.get('amount')
        expense.save()
        return redirect('home')

    return render(request, 'edit.html', {'expense': expense})