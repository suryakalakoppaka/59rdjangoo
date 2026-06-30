from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
# from app1.

from app1.forms import std_form
from app1.models import students

def show_form(request):
    form=std_form()
    data=students.objects.all()
    if request.method=='POST':
        form=std_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        context={
            'form':form,
            'data':data
        }
        return render(request,'frontend1/home.html',context)
    
    
def homework(request):
    name=request.GET.get("name","kala")
    movie=request.GET.get("movie","hanuman")
    showtime=request.GET.get("showtime","6pm")
    cost=request.GET.get("total_no.of_tickets",2)
    price=request.GET.get("total_price","600")
    info={"name":name,"movie":movie,"show_time":showtime,"total_cost":cost,"total_price":price}
    return JsonResponse({"status":"success","data":info})

def temp1(request):
    return render(request,"./simple.html")

def temp2(request):
    return render(request,"./second.html")



