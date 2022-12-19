from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from core.decorators import is_panel,is_login
from .forms import BlogForm,CatForm
from .models import Blog,CatsType,Cats
from core.models import About
from core.views import is_ajax
from core.forms import AboutForm
from django.http import JsonResponse
from django.urls import reverse




def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user

    return None


def loginPage(request):
    if is_ajax and request.method=='POST':
        email = request.POST.get('email')
        passwd = request.POST.get('password')
        user = authenticate_user(email=email,password=passwd)
        if user is None:
            result = {'success':False}
            return JsonResponse(result)
        else:
            login(request,user)
            path=reverse('backsite:dashboard')
            result = {'success':True,'path':path}
            return JsonResponse(result)
    else:
        if request.user.is_authenticated:
            return redirect('backsite:dashboard')
        else:
            return render(request,'backsite/login.html')

@is_login
def logoutPage(request):
    logout(request)
    return redirect('backsite:loginpage')

@is_login
def dashboard(request):
    active_blogs=Blog.objects.filter(is_active=1).count()
    active_cats=Cats.objects.filter(is_active=1).count()
    total_blogs=Blog.objects.all().count()
    total_cats=Cats.objects.all().count()
    context={
        'active_cats':active_cats,
        'active_blogs':active_blogs,
        'total_blogs':total_blogs,
        'total_cats':total_cats,
    }
    return render(request,'backsite/index.html',context)
# Create your views here.

# Create your views here.

@is_login
def blog(request):
    blogs=Blog.objects.all()
    context={
    'blogs':blogs
    }
    return render(request,'backsite/blog.html',context)

@is_login
def create_blog(request,id=None):
    if id:
        blog = get_object_or_404(Blog,id=id)
        form=BlogForm(request.POST or None,request.FILES or None,instance=blog)
    else:
        form=BlogForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('backsite:blogs')
    context={
        'form':form
    }
    return render(request,'backsite/create-blog.html',context)

@is_login
def delete_blog(request,id):
    blog = get_object_or_404(Blog,id=id)
    blog.delete()
    return redirect('backsite:blogs')

@is_login
def create_update_about(request,id=None):
    if id:
        about = get_object_or_404(About,id=id)
        form=AboutForm(request.POST or None,instance=about)
    else:
        form=AboutForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('backsite:settings_func')
    context={
        'form':form
    }
    return render(request,'backsite/create_about.html',context)

@is_login
def settings_func(request):
    about=About.objects.first()
    cat_types=CatsType.objects.all()
    context={'about':about,'cat_types':cat_types}
    return render(request,'backsite/settings.html',context)

@is_login
def create_update_cat_type_ajax(request,id=None):
    if is_ajax:
        if request.method == 'POST':
            id=request.POST.get('cat_type_id')
            cat_type=request.POST.get('cat_type')
            if id:
                catType=CatsType.objects.get(id=id)
                catType.title=cat_type
                catType.save()
                data={'msg':'İşlem Başarılı','success':True}
                return JsonResponse(data)
            else:
                if not CatsType.objects.filter(title=cat_type).exists():
                    obj=CatsType.objects.create(title=cat_type)
                    data={'msg':'İşlem Başarılı','success':True}
                else:
                    data={'msg':'Kedi türü daha önce eklenmiş','success':False}
                return JsonResponse(data)


@is_login
def del_cat_type_ajax(request):
    if is_ajax:
        if request.method == 'GET':
            id=request.GET.get('id')
            if CatsType.objects.filter(id=id).exists():
                CatsType.objects.get(id=id).delete()
                data={'msg':'İşlem Başarılı','success':True}
            else:
                data={'msg':'Tür Silinemiyor','success':False}
            return JsonResponse(data)

@is_login
def edit_cat_type_ajax(request):
    if is_ajax:
        if request.method == 'GET':
            id=request.GET.get('id')
            if CatsType.objects.filter(id=id).exists():
                types=CatsType.objects.get(id=id)
                data={'title':types.title,'id':types.id,'success':True}
            else:
                data={'msg':'Bir hata oluştu','success':False}
            return JsonResponse(data)

@is_login
def my_cats(request):
    cats = Cats.objects.all().order_by('-created_at')
    return render(request,'backsite/my_cats.html',{'cats':cats})

@is_login
def create_cat(request,id=None):
    if id:
        cat = get_object_or_404(Cats,id=id)
        form=CatForm(request.POST or None,request.FILES or None,instance=cat)
    else:
        form=CatForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('backsite:my_cats')
    else:
        print(form.errors)
    context={
        'form':form
    }
    return render(request,'backsite/create-cat.html',context)

@is_login
def delete_cat(request,id):
    cat = get_object_or_404(Cats,id=id)
    cat.delete()
    return redirect('backsite:my_cats')
