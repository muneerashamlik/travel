
from django.shortcuts import render

from demoapp.models import Health


# Create your views here.
#class22,23(class24-task thazhe)
#def home(request):
   # return render(request,"home.html")

#def about(request):
   # return render(request,"about.html")

#def  contact(request):
    #return HttpResponse("am contact page")
#def detail(request):
    #return render(request,"detail.html")
#def  thanks(request):
   # return HttpResponse("thank you")

#passing values-class25

#def demo(request):
   # name="india"
  # return render(request,"first index1.html",{'obj':name})

#passing values from one page to another page-class 26
#class27 -task(thazhe)
#def demo(request):
   # return render(request,"pagetopage.html")

#def addition(request):
   # X=int(request.GET['num1'])
  #  Y=int(request.GET['num2'])
   # res=X+Y
   # return render(request,"result.html",{'result':res})
#def difference(request):
    #X = int(request.GET['num1'])
   # Y = int(request.GET['num2'])
   # res=X-Y
    #return render(request, "result.html", {'result': res})

#def multiplication(request):
   # X = int(request.GET['num1'])
    #Y = int(request.GET['num2'])
   # res=X*Y
   # return render(request, "result.html", {'result': res})


#def division(request):
    #X = int(request.GET['num1'])
    #Y = int(request.GET['num2'])
   # res=X/Y
   # return render(request, "result.html", {'result': res})


#class 29 ( adding static file)

def demo(request):
    obj=Health.objects.all()
    return render(request,"index.html",{'result':obj})
def cutes(request):
    baby=Health.baby.all()
    return render(request,"index.html",{'babies':baby})


