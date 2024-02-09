from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.db.models import Q
from admin_master.models import *
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

def adminClass(request):
    msg=''
    if request.POST:
        class_name=request.POST['ClassName']
        if not class_name:
            msg='You have to fill Class name'
        elif Class_NEWdb.objects.filter(className=class_name).exists():
            msg=f'{class_name}Already Exists'
        else:
            data=Class_NEWdb(className=class_name)
            data.save()
            msg=f'{class_name} Succesfully Added'
            return redirect('adminClass')
        print(msg)
    record=Class_NEWdb.objects.all()
    a=loader.get_template('adminClass.html')
    return HttpResponse(a.render({'msg':msg,'record':record}))

def deleteClass(request):
    id=request.POST['dId']
    Class_NEWdb.objects.filter(id=id).delete()
    print('deleted')
    msg='Successfully deleted'
    return JsonResponse({'msg':msg})

def adminDepartment(request):
    if request.POST:
        Dname=request.POST['dname'].strip()
        
        Dcode=request.POST['dcode'].strip()
        print(Dname)
        print(Dcode)
        if  not Dname:
            messages.warning(request ,'you have not filled Department name') 
        else:
            if not Dcode:
                messages.warning(request ,"You have not filled Department Code")

            else:
                if Departmentdb.objects.filter(Q(departmentName=Dname) | Q(departmentCode=Dcode)).exists():
                    messages.error(request , 'Already Exists')
                else:
                    data=Departmentdb(departmentName=Dname,departmentCode=Dcode)
                    data.save()
                    messages.success(request , 'You have Succesfully Added')
    
        
    departmentData = Departmentdb.objects.all()
    a=loader.get_template('adminDepartment.html')
    return HttpResponse(a.render({'data':departmentData}))

def editDepartment(request):
    
    
    data=Departmentdb.objects.get(id=request.POST['eid'])
    response={ 'DepartmentName':data.departmentName,
              'DepartmentCode':data.departmentCode,
              'status':data.status,
              'dataid':data.id
              }

    return JsonResponse(response)

def updateDepartment(request):
    message=''
    id=request.POST['eid']
    DepartmentName=request.POST['DepartmentName']
    DepartmentCode=request.POST['DepartmentCode']
    status=request.POST['status']
    if  not DepartmentName:
        messages.warning(request ,'you have not filled Department name') 
    else:
        if not DepartmentCode:
            messages.warning(request ,"You have not filled Department Code")

        else:
            if Departmentdb.objects.filter(Q(departmentName=DepartmentName) | Q(departmentCode=DepartmentCode)).exclude(id=id).exists():
                messages.error(request , 'Already Exists')
            else:
                data=Departmentdb.objects.get(id=id)
                data.departmentName=DepartmentName
                data.departmentCode=DepartmentCode
                data.status=status
                data.save()
    return JsonResponse({"msg":message})
def deleteDipartment(request):
    id=request.POST['dId']
    Departmentdb.objects.filter(id=id).delete()
    msg='you have successfully Deleted'
    return JsonResponse({'msg':msg})
    
def editClass(request):
    id=request.POST['eid']
    data=Class_NEWdb.objects.get(id=id)
    response={'className':data.className,'status':data.status,'id':data.id}
    return JsonResponse(response)

def updateClass(request):
    msg=''
    id=request.POST['id']
    className=request.POST['classname'].strip()
    status=request.POST['status']
    if not className:
        msg='you have to fill ClassName'
    else:
        if Class_NEWdb.objects.filter(className=className).exclude(id=id).exists():
            msg='Already Exists'
        else:
            record=Class_NEWdb.objects.get(id=id)
            record.className=className
            record.status=status
            record.save()
            msg='You have Successfully updated'
    return JsonResponse({'msg':msg})


def adminDesignation(request):
    msg=''
    if request.POST:
        designation_name=request.POST['DesignationName']
        designation_code=request.POST['DesignationCode']
        if not designation_name and not designation_code:
            msg='you have to fill both Designation Name and Designation code'
        elif not designation_name:
            msg='You have to fill Designation Name'
        elif not designation_code:
            msg='you have to fill Designation Code'
        elif Designationdb.objects.filter(Q(designationName=designation_name) | Q(designationCode=designation_code)).exists():
            msg="Already Exists"
        else:
            data=Designationdb(designationName=designation_name,designationCode=designation_code)
            data.save()
            msg="You have successfully added"
    record=Designationdb.objects.all()
    a=loader.get_template('adminDesignation.html')
    return HttpResponse(a.render({'msg':msg,'record':record}))

def adminDivision(request):
    msg=''
    if request.POST:
        division_name=request.POST['DivisionName']
        if not division_name:
            msg='You have to fill Division name'
        elif Divisiondb.objects.filter(divisionName=division_name).exists():
            msg=f'{division_name}Already Exists'
        else:
            data=Divisiondb(divisionName=division_name)
            data.save()
            msg=f'{division_name} Succesfully Added'
    record=Divisiondb.objects.all()
    a=loader.get_template('adminDivision.html')
    return HttpResponse(a.render({'msg':msg,'record':record}))

def adminEmployeeCatagory(request):
    msg=''
    if request.POST:
        employee_catagory=request.POST['EmployeeCatagory']
        employee_area=request.POST['EmployeeArea']
        EmpCat=EmployeeCatagorydb.objects.filter(employeeCatagory=employee_catagory).exists()
        EmpArea=EmployeeCatagorydb.objects.filter(employeeArea=employee_area).exclude(employeeArea=5).exists()
        if not employee_catagory or not employee_area:
            msg='you have to fill both Employee Catagory and Employee Area'
        
        elif not EmpCat and not EmpArea:
            data=EmployeeCatagorydb(employeeCatagory=employee_catagory,employeeArea=employee_area)
            data.save()
            msg="You have successfully added"
            
        else:
            
            msg="Already Exists"
    record=EmployeeCatagorydb.objects.all()
    a=loader.get_template('adminEmployeeCatagory.html')
    return HttpResponse(a.render({'msg':msg,'record':record}))

def adminQualification(request):
    msg=''
    if request.POST:
        qualification_name=request.POST['QualificationName']
        if not qualification_name:
            msg='You have to fill Class name'
        elif Qualificationdb.objects.filter(qualificationName=qualification_name).exists():
            msg=f'{qualification_name}Already Exists'
        else:
            data=Qualificationdb(qualificationName=qualification_name)
            data.save()
            msg=f'{qualification_name} Succesfully Added'
    record=Qualificationdb.objects.all()
    a=loader.get_template('adminQualification.html')
    return HttpResponse(a.render({'msg':msg,'record':record}))


def adminSubject(request):
    msg=''
    if request.POST:
        subject_name=request.POST['SubjectName'].strip()
        class_id=request.POST.getlist('subCheckbox')
        if  not subject_name:
            msg='You have to fill Subject Name'
        elif Subjects.objects.filter(subjectName=subject_name).exists():
            msg=f'{subject_name} Alredy Exists'
        else:
            subjectid,SubjectData=Subjects.objects.get_or_create(subjectName=subject_name)
            
            for i in class_id:
                clss=Class_NEWdb.objects.get(id=int(i))
                Fdata=ClassSubject(SID=subjectid,CID=clss)
                Fdata.save()
                msg='Successfully Added'
          
            print(SubjectData)

    record=Class_NEWdb.objects.filter(status=1)
    data=Subjects.objects.all()
    a=loader.get_template('adminSubject.html')
    return HttpResponse(a.render({'record':record,'msg':msg, 'data':data}))

def editSubject(request):
    id=request.POST['eid']
    print(id)
    data=Subjects.objects.get(id=id)
    Classes=Class_NEWdb.objects.all()

    Checkedkey=ClassSubject.objects.filter(SID=id)

    response={'subject':data,'checkedkey':Checkedkey,'classes':Classes}
    return JsonResponse(response,safe=False, encoder=DjangoJSONEncoder)