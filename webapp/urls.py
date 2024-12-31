from django.urls import path
from .import views
urlpatterns=[
    path('nav/',views.web,name='web'),
    path('footer/',views.footer,name='footer'),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('cat/<str:foo>',views.category,name='category'),
    path('register/',views.register_user,name='register'),
    path('contact',views.contact,name='contact'),
    path('wishlist',views.wishlist,name='wishlist'),

]