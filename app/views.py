from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
import datetime
# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/dashboard.html',{})


def patient(request):
    ptn = Patient.objects.filter(date=datetime.datetime.today()).order_by("-id")
    return render(request, 'newPatient/patient.html',{"ptn":ptn})

def newPatient(request):  
    if request.method == "POST":
        if "SavePatient" in request.POST:
            print("hello patient")
            p = Patient()
            p.name = request.POST["name"]
            p.adrs = request.POST["adrs"]
            p.email = request.POST["email"]
            p.mobileNo = request.POST["mobileNo"]
            p.referedBy = request.POST["referedBy"]
            p.remark = request.POST["remark"]
            p.method = request.POST["cashOnline"]
            p.trId = request.POST["TrId"]
            p.total = request.POST["t_total"]
            p.date = datetime.datetime.today()
            p.save()
            for i in range(1,11):
                if request.POST[f'tname{i}']:
                    t=Tests()
                    t.Patient = p
                    t.Test_name = request.POST[f"tname{i}"]
                    t.qty = request.POST[f"tqty{i}"]
                    t.t_price = request.POST[f"tprice{i}"]
                    t.save()
            return redirect("patient")

    dc = Doctor.objects.all()
    return render(request, 'newPatient/newPatient.html',{'dc':dc})

def viewPatient(request,id):
    p = Patient.objects.get(id=id)
    t = Tests.objects.filter(Patient=p)
    return render(request,"newPatient/viewPatient.html",{"p":p,"t":t})

def existingPatient(request):
    if request.method =="POST":
        if "searchbtn" in request.POST :
            if request.POST['name'] or request.POST['id'] or request.POST['mobileNo']:
                ptn = Patient.objects.filter(Q(name__icontains=request.POST["name"]) & Q(mobileNo__icontains=request.POST["mobileNo"]) & Q(id__icontains=request.POST['id']) )
                print(ptn)
                return render(request, 'existing/existing.html',{"ptn":ptn})
            
    return render(request, 'existing/existing.html')