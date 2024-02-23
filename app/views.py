from django.shortcuts import render,HttpResponse

from app.models import details,fb

# Create your views here.
# def form(request):
    # print(request)    #     1.GET/URLNAME/          1. POST/URLNAME/
    # print(request.POST)      # 2.{} {KEY:VALUES}

    # if request.method=='POST':
    #     print(request.POST['name'])
    #     print(request.POST['age'])
    #     print(request.POST['psw'])
    #     print(request.POST['mobile'])
    #     print(request.POST['gender'])
    #     print(request.POST['dob'])
    #  return render(request,'form.html')

def form(request):
    if request.method=="GET":
        return render(request,'form.html')
    elif request.method=='POST':
        nam=request.POST['name']
        ag=request.POST['age']
        mob=request.POST['mob']
        fb.objects.create(name=nam,ag=ag,phno=mob)
        return HttpResponse('data is stored')
    
    
    

