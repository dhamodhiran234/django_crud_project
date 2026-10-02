from django.shortcuts import render,redirect
from .models import Sign,Adddata

# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html",{'name':'dhamu'})
def sign(request):
    return render(request,"sign.html")
def login(request):
    return render(request,"login.html")
def sign_vad(request):
    name=request.POST['name']
    email=request.POST['email']
    password=request.POST['password']
    phone=request.POST['phone']
    if Sign.objects.filter(email=email).exists():
        return render(request,"sign.html",{'error':'user already exists'})
    else:
        ex1=Sign(name=name,password=password,email=email,phone=phone)
        ex1.save()
        
        print(name,email,password,phone)
        return render(request,"login.html")
def login_vad(request):
    
    email=request.POST['email']
    password=request.POST['password']
    print(email,password)
    if Sign.objects.filter(email=email,password=password).exists():
        h=Sign.objects.filter(email=email)
        for i in h:
            request.session['user_name']=i.name
            f=request.session.get('user_name')
            return render(request,"home.html",{"name":f})
    else:
        return render(request,"login.html",{'error':'No users can exists,please signup'})


def home(request):
    f=Adddata.objects.all()
    for i in f:
        print(i)
    return render(request,"home.html",{"data":f})


def adddata(request):

    roll=request.POST['roll']
    name=request.POST['name']
    age=request.POST['age']
    gender=request.POST['gen']
    address=request.POST['address']
    ex1=Adddata(roll=roll,name=name,age=age,gender=gender,address=address)
    ex1.save()
    print(roll,name,age,gender,address)
    return render(request,"home.html",{"error":"add data successfully"})


def log_out(request):
    request.session.flush()
    return render(request,"login.html")

def singledataget(request):
    roll=request.POST['roll']
    if (Adddata.objects.filter(roll=roll).exists()):
        f=Adddata.objects.filter(roll=roll)
        return render(request,"display.html",{"data":f})
    else:
        return render(request,"home.html",{"error":"user not found"})

def deletedataget(request):
    roll=request.POST['roll']
    f=Adddata.objects.filter(roll=roll)
    if (f.exists()):
        f.delete()
        f1=Adddata.objects.all()
        return render(request,"display.html",{"data":f1})
    else:
        return render(request,"home.html",{"error":"user not found"})


def updatestudata(request):
    chroll=request.POST['chroll']
    roll=request.POST['roll']
    name=request.POST['name']
    age=request.POST['age']
    gender=request.POST['gen']
    address=request.POST['address']
    k=Adddata.objects.filter(roll=chroll)
    if k.exists():
        k.update(
            roll=roll,
            name=name,
            age=age,
            gender=gender,
            address=address
        )
        f=Adddata.objects.all()
        return render(request,"display.html",{"data":f})
    else:
        return render(request,"home.html",{"error":"user not exists"})

def alldataget(request):
    f=Adddata.objects.all()
    return render(request,"display.html",{"data":f})