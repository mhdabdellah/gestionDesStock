from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.utils.html import format_html
# from django
import datetime
# from xhtml2pdf import pisa
from django.contrib import messages
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# from django.db.models import Sum,Q
from accounts.models import *
from accounts.forms import SignupForm
from django.contrib.auth.models import User
from accounts.decorators import admin_only, in_fix, admin_and_manager_only

@login_required(login_url='accounts/login')
def home(request):
    user = User.objects.all()
    # client = User.objects.all()
    article=Article.objects.all()
    commande = Commande.objects.all()
    context={'user':user,'article':article,'commande':commande}
    return render(request,'stock/index.html',context)
  


@login_required(login_url='accounts/login') 
def articleform(request):
    if request.method == 'POST':
        article_Form = NewArticle(request.POST)
        if article_Form.is_valid():
            # article_Form= article_Form.save(commit=False)
            # article_Form.user = User.objects.get(id=request.user.pk)
            article_Form.save()
            msg=(f"""<p>Felicitations l'article  \'{article_Form.nom}\'  est bien ajoute vous pouvez imprimer le barcode <a href=\'{article_Form.barcode.url}\'>imprimer</a></p>""")
            messages.success(
                request,format_html(msg))
            return redirect(reverse('stock:articleform'))
    else:
    
        article_Form = NewArticle()
        context={ 
           
            'article_Form' : article_Form,

        }
        return render(request,'stock/articleform.html',context)

@login_required(login_url='accounts/login')
def tarticle(request):
    article = Article.objects.all()

    context={

        'title': 'les article',
        'tarticle':article,

    }
    return render(request,'stock/table_article.html',context)

@login_required(login_url='accounts/login')
def update_article(request, id):
    article = Article.objects.get(id=id)
    form = NewArticle(request.user,request.POST or None, instance=article )
    if form.is_valid():
        myform = form.save()
        return redirect(reverse('stock:table_article'))

    return render(request,'stock/update_article.html',{ 'form': form,  'article': article})

@login_required(login_url='accounts/login')
def delete_article(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST': 
        article.delete()
        return redirect(reverse('stock:table_article'))

    return render(request,'stock/delete_article.html',{'article': article})

@login_required(login_url='accounts/login')
def commandeform(request):
    if request.method == 'POST':
        commande_Form = NewCommande(request.POST)
        if commande_Form.is_valid():
            myform=commande_Form.save()
            messages.success(
                request, f"Felicitations {myform.user} votre commande est bien ajoute")
            return redirect(reverse('stock:commandeform'))
    else:
        commande_Form = NewCommande()
        context={
           
            'commande_Form' : commande_Form,

        }
        return render(request,'stock/commandeform.html',context)

@login_required(login_url='accounts/login')
def tcommande(request):
    context={

        'title': 'les article' ,
        'tcommande': Commande.objects.all()

    }
    return render(request,'stock/table_commande.html',context)

@login_required(login_url='accounts/login')
def tableuser(request):
    # message = get_notifications(request)
    profile = Profile.objects.all()
    user = User.objects.all()

    # n= Equipement.objects.all().count|sub-Installation.objects.all().count


    context={

        'profile': profile,
        'user': user,
        # 'message': message

    }
    return render(request,'stock/table_user.html',context)