from django.shortcuts import render,get_object_or_404
from core.decorators import is_panel,is_login
from core.models import About
from backsite.models import Blog,Cats
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse

def index(request):
    blogs=Blog.objects.all()[0:3]
    cats=Cats.objects.all()[0:3]
    context={'blogs':blogs,'cats':cats}
    return render(request,'index.html',context)

def blogs(request):
    blogs=Blog.objects.filter(is_active=True)
    return render(request,'blogs.html',{'blogs':blogs})

def blog_page(request,slug):
    blog=get_object_or_404(Blog,url=slug)
    return render(request,'blog-page.html',{'blog':blog})

def about(request):
    about=About.objects.first()
    return render(request,'about_us.html',{'about':about})

def cats_blog(request):
    cats=Cats.objects.all()
    return render(request,'cats.html',{'cats':cats})

def cat_info(request,id):
    cat=get_object_or_404(Cats,id=id)
    return render(request,'cat_info.html',{'cat':cat})

def contact_func(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if request.method == 'GET':
        return render(request,'contact.html')
    if is_ajax:
        if request.method=='POST':
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            email=request.POST.get('email')
            tel=request.POST.get('tel')
            message=request.POST.get('message')
            subject = 'Site Mesaji'
            message = """
                Site üzerinden gelen mesaj detayı ;

                İsim: {},

                Soyisim : {},

                Email : {},

                Telefon : {} ,

                Mesaj : {}

            """.format(firstname,lastname,email,tel,message)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = settings.RECIPIENT_LIST
            send_mail( subject, message, email_from, recipient_list )
            return JsonResponse({'msg':'Mesajınız İletilmiştir'})

# Create your views here.
