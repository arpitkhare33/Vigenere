from django.urls import path
from . import views
urlpatterns =[
    path('',views.home,name='home'),#for getting home page, call the function home
    # path('add',views.add,name='add'),
    path('encrypt',views.encrypt,name='encrypt'),
    path('decrypt',views.decrypt,name='decrypt')
]

