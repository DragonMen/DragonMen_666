from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def register(request):
    if request.method=='POST':

        #第一步:
        print(request.POST)
        user = request.POST.get('username')
        pwd = request.POST.get('passwd')
        return redirect('/index.html/')

        # if user=='ff'  and pwd =='123':


    else:
        # 注册跳转到登录,登录跳转到个人首页.
        return render('/register.html/')


def login(request):
    print('met11hod :',request.method)
    print('pa11th : ',request.path)

    if request.method=='POST':
        print(request.POST)
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        if user=='ff' and pwd=='123':
            return redirect('/index.html/')

    return render(request,'/login.html/')

def index(request):
    return render(request,'/index.html/')
