from django.shortcuts import render,redirect
from Library_Management_App.models import Book
from Library_Management_App.forms import Book_Form,CreateUserForm
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home_view(request):
    return render(request,'accounts/base.html')

@login_required(login_url='login')
def book_view(request):
    all_books=Book.objects.all()
    return render(request,'accounts/book.html',{'all_books':all_books})

@login_required(login_url='login')
def create_book_view(request):
    book_form=Book_Form()
    if request.method == "POST":
        book_form=Book_Form(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('/allbooks/')
    else:
        return render(request,'accounts/add_book.html',{'book_form':book_form})

@login_required(login_url='login')
def update_book_view(request,pk):
    book=Book.objects.get(id=pk)
    book_form=Book_Form(instance=book)
    if request.method == "POST":
        book_form=Book_Form(request.POST,instance=book)
        if book_form.is_valid():
            book_form.save()
            return redirect('/allbooks/')
    else:
        return render(request,'accounts/update_book.html',{'book_form':book_form})

@login_required(login_url='login')
def delete_book_view(request,pk):
    book=Book.objects.get(id=pk)
    book.delete()
    return redirect('/allbooks/')

def register_page_view(request):
    if request.user.is_authenticated:
        return redirect('allbooks')
    else:
        form=CreateUserForm()
        if request.method =='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/login/')
            else:
                return redirect('/register/')

        else:
            return render(request,'accounts/register.html',{'form':form})

def login_page_view(request):
    if request.user.is_authenticated:
        return redirect('allbooks')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            email=request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request,username=username,email=email,password=password)
            if user is not None:
                login(request,user)
                #return HttpResponse('Admin successfully Login')
                return redirect('/allbooks/')
            else:
                messages.warning(request,'username or password is incorrect')
        else:
            return render(request,'accounts/login.html')

def logout_page_view(request):
    logout(request)
    return redirect('/login/')


