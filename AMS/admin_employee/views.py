from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse ,JsonResponse
from django.template import loader
from admin_master.models import *
from admin_employee.models import *
from django.db.models import Q
import qrcode
from django.core.files.base import ContentFile
from io import BytesIO 


# Create your views here.

def employeeRegistration(request):
    msg = ''

    if request.method == 'POST':
        employeeCatagory = request.POST.get('Employee_Catagory')
        print(employeeCatagory)
        employeeCatagoryId = get_object_or_404(EmployeeCatagorydb, id=employeeCatagory.split('+')[0])
        name = request.POST['EmployeeName']
        gender = request.POST['EmployeeGender']
        dateOfBirth = request.POST['DOB']
        mobile = request.POST['MobileNo']
        email = request.POST["EmployeeEmail"]
        address = request.POST['EmployeeAddress']
        employeeQualification = request.POST['EmployeeQualification']
        employeeQualificationId = get_object_or_404(Qualificationdb, id=employeeQualification)
        employeeDesignation = request.POST['EmployeeDesignation']
        employeeDesignationId = get_object_or_404(Designationdb, id=employeeDesignation)
        employeeDepartment = request.POST['EmployeeDepartment']
        employeeDepartmentId = get_object_or_404(Departmentdb, id=employeeDepartment)
        salary = request.POST['EmployeeSalary']
        joiningDate = request.POST['EmployeeJoiningDate']
        photo = request.FILES['EmployeeImage']

        # qr making
        gend = {0: 'Male', 1: 'Female', 2: 'Other'}
        qr_data = f"Name: {name}\nDOB: {dateOfBirth}\nEmail: {email}\nDepartment: {employeeDepartmentId.departmentName}\nGender: {gend[int(gender)]}"

        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Add data to the QR code
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a buffer
        buffer = BytesIO()
        img.save(buffer, format="PNG")

        # Create or update the QRCodeData instance in the database
        if not name or not email or not employeeCatagory or not dateOfBirth or not address or not mobile:
            msg = 'You have to fill all the details'
        elif EmployeeRegistrationTB.objects.filter(Q(Mobile=mobile) | Q(Email=email)).exists():
            msg = 'Mobile no or Email already exists'
        else:
            # Corrected ContentFile usage
            Employee_data, created = EmployeeRegistrationTB.objects.get_or_create(
                Name=name,
                Gender=gender,
                DateOfBirth=dateOfBirth,
                Mobile=mobile,
                Email=email,
                Address=address,
                EmployeeCatagory=employeeCatagoryId,
                EmployeeQualification=employeeQualificationId,
                EmployeeDesignation=employeeDesignationId,
                EmployeeDepartment=employeeDepartmentId,
                Salary=salary,
                JoiningDate=joiningDate,
                Image=photo
            )

            # Provide the content of the buffer when creating ContentFile
            Employee_data.QRcode.save(f"{name}_qrcode.png", ContentFile(buffer.getvalue()), save=True)

            msg = 'You have successfully added'
            deprt = EmpDepartment(Employee_id=Employee_data, Department_id=employeeDepartmentId, FromDate=joiningDate)
            deprt.save()
            design = EmpDesignation(Employee_id=Employee_data, Designation_id=employeeDesignationId, FromDate=joiningDate)
            design.save()
            empsal = EmpSalary(Employee_id=Employee_data, Employee_Salary=salary, FromDate=joiningDate)
            empsal.save()

            if employeeCatagoryId.employeeArea == 2:

                print('hi midlaj kk')
                Eclass = request.POST.getlist('Eclass')
                Edivi = request.POST.getlist('Edivision')
                ESub = request.POST.getlist('Esubject')
                print('Eclass=',Eclass)
                print('Edivi=',Edivi)
                print('Esub=',ESub)

                for class_val, divi_val, sub_val in zip(Eclass, Edivi, ESub):
                    class_id = get_object_or_404(Class_NEWdb, id=class_val)
                    division_id = get_object_or_404(Divisiondb, id=divi_val)
                    subject_id = get_object_or_404(Subjects, id=sub_val)
                    subR=SubjectClassDivision(Emp_id=Employee_data, class_id=class_id, Division_id=division_id,
                                                       Subject_id=subject_id)
                    subR.save()
                msg += ' You have submitted all subjects'

            



    empcat=EmployeeCatagorydb.objects.all()
    quali=Qualificationdb.objects.all()
    desig=Designationdb.objects.all()
    depart=Departmentdb.objects.all()
    clas=Class_NEWdb.objects.all()
    divi=Divisiondb.objects.all()
    a=loader.get_template('EmployeeRegistrationForm.html')
    return HttpResponse(a.render({'msg':msg,'empcat':empcat,'quali':quali,'desig':desig,'depart':depart,'clas':clas,'divi':divi}))

def selectSubject(request):
    cid=request.POST.get('sid')
    print(cid)
    subjects=ClassSubject.objects.filter(CID=cid)
    if subjects.exists():
        # Assuming you want to handle multiple subjects, you can loop through them or choose a specific one.
        subject_data = [{'subname': subject.SID.subjectName, 'subid': subject.SID.pk} for subject in subjects]

        return JsonResponse({'subjects': subject_data})
    else:
        return JsonResponse({'error': 'No subjects found for the given CID'})
    

def ListEmployee(request):
    record=EmployeeRegistrationTB.objects.all()
    return render(request, 'EmployeeRegistrationData.html',{'record':record})
