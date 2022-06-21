from django.urls import path
from . import views
app_name='stock'
urlpatterns=[
    path('',views.home,name='home'),
    path('articleform',views.articleform ,name='articleform'),
    path('commandeform',views.commandeform ,name='commandeform'),
    path('table_users',views.tableuser,name='table_users'),
    path('table_article',views.tarticle,name='table_article'),
    path('table_commande',views.tcommande,name='table_commande'),
    path('update_article/<int:id>',views.update_article,name='update_article'),
    path('delete_article/<int:id>',views.delete_article,name='delete_article'),

]