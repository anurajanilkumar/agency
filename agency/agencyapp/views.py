from datetime import datetime, timezone
from django.shortcuts import render,redirect
from agencyapp import views
from .models import Bookings, User, Group, Branch, Product, Bookings, Work, Service, Complaint
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse

# Create your views here.


# def Customer(request):
#     if request.method=='POST':
#         fname=request.POST['FIRSTNAME']
#         sname=request.POST['SECONDNAME']
#         mail=request.POST['EMAIL']
#         address=request.POST['ADDRESS']
#         guardian1=request.POST['GUARDIAN']
#         usrname=request.POST['USERNAME']
#         pword=request.POST['PASSWORD']

#         new_user=User.objects.create_user(first_name=fname,last_name=sname,email=mail,username=usrname,password=pword,adress=address,is_active=0)
#         new_user.save()
#         x=Student.objects.create(studentid=new_user,guardian=guardian1)
#         x.save()
#         return HttpResponse("<script>alert('register successfully');window.location.href='http://127.0.0.1:8000'</script>")
#     else:
#         return render(request,'student_reg.html')
def viewIndex(request):
    return render(request,'index.html')

def loginpage(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        userpass =  authenticate(request, username = username, password = password)
        print(userpass)
        if userpass is None:
            print('hello')
            return HttpResponse("<script> alert('Invalid cred'); window.location.href='logins'</script>")
        if userpass.is_superuser==1:
            login(request,userpass)
            request.session['user_id']=userpass.id
            return redirect("Admin Page")
        
        login(request,userpass)
        request.session['user_id'] = userpass.id
        request.session['branch_id'] = userpass.branch_id.id
        if userpass.group_id.group_name == 'CONSUMER':
            return redirect("consumer")
        if userpass.group_id.group_name == 'MANAGER':
            return redirect("manager")
        if userpass.group_id.group_name == 'STAFF':
            return redirect("staff")
    else:
        return render(request,'login.html')

def signUp(request):
    if request.method == 'POST':
        con_fname = request.POST['fname']
        con_lname = request.POST['lname']
        con_address = request.POST['address']
        con_email = request.POST['email']
        con_contact = request.POST['contact']
        con_location = request.POST['location']
        con_pass = request.POST['password']
        con_branch = Branch.objects.get(id = request.POST['branch'])
        group = Group.objects.get(group_name='CONSUMER')
        user = User.objects.create(first_name = con_fname, 
                                   last_name = con_lname, 
                                   address = con_address, 
                                   location = con_location,
                                   contact = con_contact, 
                                   email = con_email,
                                   username = con_email,
                                   group_id = group,
                                   branch_id = con_branch
                                   )
        user.set_password(con_pass)
        user.save()
        return HttpResponse("<script> alert('Successfully added'); window.location.href='logins'</script>")
    branches = Branch.objects.all()[1:]
    return render(request,'signup.html',{'branches':branches})

def logout(request):
    request.session.clear()
    return redirect("Index")

        

#______________________admin_page______________________

def viewAdmin(request):
    admin = User.objects.get(id = request.session['user_id'])
    if(admin.is_superuser == 1):
        return render(request,'admin/admin.html')
    else:
        return redirect('loginpage')
    

def viewAndGroup(request):
    
    if request.method == 'POST':
        name = request.POST['group-name']
        Group.objects.create(group_name = name)
        return HttpResponse("<script> alert('Successfullt added'); window.location.href='admin'</script>")
    return render(request, 'admin/addGroup.html')

def addBranch(request):
    if request.method == 'POST':
        br_name = request.POST['branch-name']
        br_loc = request.POST['branch-loc']
        mang_email = request.POST['email']
        mang_password = request.POST['password']
        mang_contact = request.POST['contact']
        curr_branch = Branch.objects.create(branch_name = br_name, branch_location = br_loc)
        managerGroup = Group.objects.get(group_name='MANAGER')
        manager = User.objects.create(username = mang_email, email= mang_email, contact=mang_contact, group_id=managerGroup, branch_id = curr_branch)
        manager.set_password(mang_password)
        curr_branch.save()
        manager.save()
        return HttpResponse("<script> alert('Successfullt added'); window.location.href='branches'</script>")
    return render(request, 'admin/addBranch.html')

def deleteBranch(request, id):
    branch = Branch.objects.get(id = id)
    branch.delete()
    return redirect('branches')


def viewBranch(request):

    branches = Branch.objects.all()
    return render(request, 'admin/branches.html',{'branches':branches})

def viewBooking(request):

    bookings = Bookings.objects.all()
    branches = Branch.objects.all()
    filter = None
    if request.method == 'POST' and request.POST['filter-branch'] != "":
        id = request.POST['filter-branch']
        bookings = Bookings.objects.filter(product_id__branch_id = id)
        bookings = bookings.union(Bookings.objects.filter(service_id__branch_id = id))
        filter = branches.get(id = id)
        print(filter.branch_name)
    return render(request, 'admin/bookings.html',{'bookings':bookings, 'branches':branches, 'filter': filter})

#________________________manager_page________________________

def manager(request):
    user_id = request.session['user_id']
    user = User.objects.get(id = user_id)
    return render(request, 'manager/manager.html',{'branch':user})

def staffs(request):
    branch_id = request.session['branch_id']
    staffs = User.objects.filter(branch_id = branch_id, group_id = '3')
    return render(request, 'manager/staffs.html',{'staffs':staffs})

def addStaff(request):
    branch = Branch.objects.get(id = request.session['branch_id'])
    if request.method == 'POST':
        con_fname = request.POST['fname']
        con_lname = request.POST['lname']
        con_address = request.POST['address']
        con_email = request.POST['email']
        con_contact = request.POST['contact']
        con_location = request.POST['location']
        con_pass = request.POST['password']
        group = Group.objects.get(group_name='STAFF')
        print(branch)
        user = User.objects.create(first_name = con_fname, 
                                   last_name = con_lname, 
                                   address = con_address, 
                                   location = con_location,
                                   contact = con_contact, 
                                   email = con_email,
                                   username = con_email,
                                   group_id = group,
                                   is_staff = 1,
                                   branch_id = branch
                                   )
        user.set_password(con_pass)
        user.save()
        return redirect('staffs')
    return render(request, 'manager/add-staff.html', {'branch':branch})

def products(request):
    products = Product.objects.filter(branch_id = request.session['branch_id'])
    return render(request, 'manager/products.html', {'products':products})

def addProduct(request):
    branch = Branch.objects.get(id = request.session['branch_id'])
    if request.method == 'POST':
        prod_name = request.POST['name']
        prod_desc = request.POST['desc']
        prod_rate = request.POST['rate']
        product = Product.objects.create(product_name = prod_name, product_description = prod_desc, product_rate = prod_rate, branch_id = branch)
        product.save()
        return redirect('products')
    return render(request, 'manager/add-product.html')

def updateProdStock(request, id):
    product = Product.objects.get(id = id)
    if request.method == 'POST':
        prod_stock = request.POST['stock']
        # stock_update = Product.objects.update
        product.stock = prod_stock
        product.save()
        return redirect('products')
    return render(request, 'manager/update-product-stock.html',{'product':product})

def works(request):
    branch_id = request.session['branch_id']
    print(branch_id)
    branch = Branch.objects.get(id = branch_id)
    print(branch)
    bookings = Bookings.objects.filter(user_id__branch_id = request.session['branch_id'], work_assigned = False)
    print(bookings)
    staffs = User.objects.filter(branch_id = branch_id, group_id = '3')
    works = Work.objects.filter(branch_id = branch_id)
    if request.method == 'POST':
        booking = Bookings.objects.get(id = request.POST['id'])
        staff = User.objects.get(id = request.POST['staff'])
        booking.work_assigned = True
        booking.delivery_status = 'PROCESSING'
        work = Work.objects.create(booking_id = booking, staff_id = staff, branch_id = branch)
        booking.save()
        work.save()
        return redirect('works')
    return render(request, 'manager/works.html',{'bookings': bookings, 'staffs': staffs, 'works': works})

def viewServices(request):
    services = Service.objects.filter(branch_id = request.session['branch_id'])
    return render(request, 'manager/services.html', {'services':services})

def addService(request):
    branch = Branch.objects.get(id = request.session['branch_id'])
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        rate = request.POST['rate']
        service = Service.objects.create(service_name = name, service_description = desc, service_rate = rate, branch_id = branch)
        service.save()
        return redirect('services')
    return render(request, 'manager/add-service.html')
    

#__________________________consumer_page____________________________

def consumer(request):
    user_id = request.session['user_id']
    user = User.objects.get(id = user_id)
    products = Product.objects.filter(branch_id = user.branch_id)
    services = Service.objects.filter(branch_id = user.branch_id)
    return render(request, 'consumer/consumer.html',{'user':user,'products':products,'services':services})

def bookProduct(request, id):
    product = Product.objects.get(id = id)
    user = User.objects.get(id = request.session['user_id'])
    if request.method == 'POST':
        prod_qty = int(request.POST['qty'])
        cost = prod_qty * int(product.product_rate)
        if prod_qty > product.stock:
            return HttpResponse("<script> alert('Not enough stock')</script>")
        booking = Bookings.objects.create(product_id = product, user_id = user, product_qty=prod_qty, cost = cost, payment_status='SUCCESS', delivery_status='PENDING')
        booking.save()
        product.stock = product.stock - prod_qty
        product.save()
        return redirect('consumer')
    return render(request, 'consumer/book-product.html',{'product':product})

def bookService(request, id):
    service = Service.objects.get(id = id)
    user = User.objects.get(id = request.session['user_id'])
    if request.method == 'POST':
        booking = Bookings.objects.create(service_id = service, booking_type = 'SERVICE', user_id = user, product_qty=1, cost = service.service_rate, payment_status='SUCCESS', delivery_status='PENDING')
        booking.save()
        service.save()
        return redirect('consumer')
    return render(request, 'consumer/book-service.html',{'service':service})

def bookings(request):
    bookings = Bookings.objects.filter(user_id = request.session['user_id']).order_by('-created_at')
    return render(request, 'consumer/bookings.html',{'bookings':bookings})

def complaints(request):
    complaints = Complaint.objects.filter(user_id =  request.session['user_id']).order_by('-created_at')
    return render(request, 'consumer/complaints.html',{'complaints':complaints})

def createComplaint(request):
    bookings = Bookings.objects.filter(user_id =  request.session['user_id'], work_assigned = True).order_by('-created_at')
    user = User.objects.get(id = request.session['user_id'])
    if request.method == 'POST':
        booking = Bookings.objects.get(id = request.POST['booking'])
        comp_name = request.POST['name']
        comp_desc = request.POST['desc']
        staff = Work.objects.get(id = booking.id).staff_id
        complaint = Complaint.objects.create(complaint_name = comp_name, 
                                             complaint_desc = comp_desc, 
                                             user_id = user,
                                             booking_id = booking,
                                             staff_id = staff
                                             )
        complaint.save()
        return redirect('complaints')
    return render(request, 'consumer/create-complaint.html',{'bookings':bookings})

def viewComplaintDetails(request, id):
    user_id = request.session['user_id']
    user = User.objects.get(id = user_id)
    complaint = Complaint.objects.get(id = id, user_id = user_id)
    if request.method == 'POST':
        if 'resolve' in request.POST:
            complaint.status = 'RESOLVED'
            complaint.read = None
            complaint.save()
            return redirect('complaints')
        else:
            resolution = request.POST['replay']
            if complaint.resolution is None:
                complaint.resolution = ''
            time_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
            complaint.resolution = complaint.resolution + '\n' + user.first_name + ' consumer('+ str(time_now)+'):' + resolution +'\n'
            complaint.read = True
            complaint.save()
            return redirect('complaint-details',id)
    return render(request, 'consumer/complaint-details.html',{'complaint':complaint})

#_____________________________staff_page____________________________________

def staff(request):
    user_id = request.session['user_id']
    works = Work.objects.filter(staff_id = user_id, work_complete_date__isnull = True)
    if request.method == 'POST':
        work = Work.objects.get(id = request.POST['work'])
        status = request.POST['status']
        work.work_status = 'DONE'
        work.work_complete_date = datetime.now(timezone.utc)
        booking = work.booking_id
        booking.delivery_status = status
        work.save()
        booking.save()
        return redirect('staff')
    return render(request, 'staff/staff.html',{'works':works})

def viewHistory(request):
    user_id = request.session['user_id']
    works = Work.objects.filter(staff_id = user_id, work_complete_date__isnull = False )
    return render(request, 'staff/work-history.html',{'works':works})

def viewComplaints(request):
    complaints = Complaint.objects.filter(staff_id = request.session['user_id']).order_by('updated_at')
    return render(request, 'staff/view-complaints.html',{'complaints':complaints})

def resolveComplaint(request, id):
    user_id = request.session['user_id']
    staff = User.objects.get(id = user_id)
    complaint = Complaint.objects.get(id = id, staff_id = user_id)
    if request.method == 'POST':
        if 'close' in request.POST:
            if complaint.resolution is None:
                return HttpResponse("<script> alert('Cant close if there is no resolution')</script>")
            complaint.status = 'CLOSED'
            complaint.save()
            return redirect('view-complaints')
        else:
            resolution = request.POST['replay']
            if complaint.resolution is None:
                complaint.resolution = ''
            time_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
            complaint.resolution = complaint.resolution + '\n' + staff.first_name + ' staff('+ str(time_now)+'):' + resolution +'\n'
            complaint.read = False
            complaint.save()
            return redirect('resolve-complaint',id)
    return render(request, 'staff/resolve-complaint.html',{'complaint':complaint})

