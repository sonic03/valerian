from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name='backsite'
urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('login/',loginPage,name='loginpage'),
    path('logout/',logoutPage,name='logoutpage'),
    path('blogs/',blog,name='blogs'),
    path('create-blog/',create_blog,name='create_blog'),
    path('update-blog/<int:id>',create_blog,name='update_blog'),
    path('delete-blog/<int:id>',delete_blog,name='delete_blog'),
    path('create_update_about/',create_update_about,name='create_about'),
    path('create_update_about/<int:id>',create_update_about,name='update_about'),
    path('settings/',settings_func,name='settings_func'),
    path('cat_type_ajax/',create_update_cat_type_ajax,name='cat_type_ajax'),
    path('del_cat_type_ajax/',del_cat_type_ajax,name='del_cat_type_ajax'),
    path('edit_cat_type_ajax/',edit_cat_type_ajax,name='edit_cat_type_ajax'),
    path('my_cats/',my_cats,name='my_cats'),
    path('create_cat/',create_cat,name='create_cat'),
    path('update_cat/<int:id>',create_cat,name='update_cat'),
    path('delete_cat/<int:id>',delete_cat,name='delete_cat'),

]
