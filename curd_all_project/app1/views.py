from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from app1.models import student_model
from app1.forms1 import student_update_form
from app1.forms import student_forms
def details(request):
    data=student_model.objects.all()
    content={
        "data":data
    }
    return render(request,'frontend_app1/table.html',content)
def details_form(request):
    form=student_forms()
    if request.method=="POST":
        form=student_forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tablename")
        else:
           return HttpResponse("Invalid Email_Id")
    else:
     form=student_forms()
     content={
        "form":form}
     return render(request,'frontend_app1/forms.html',content)
    
def details_update_form(request,id):
   data=student_model.objects.get(id=id)
   if request.method=="POST":
      form=student_update_form(request.POST,instance=data)
      if form.is_valid():
             form.save()
             return redirect("tablename")
   else:
     
      form=student_update_form(instance=data)
      content={
         "form":form
      }
      return render(request,'frontend_app1/update_form.html',content)

def delete(request,id):
    data=student_model.objects.get(id=id)
    data.delete()
    return redirect("tablename")