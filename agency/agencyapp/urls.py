from django.urls import path
from agencyapp import views

urlpatterns=[
    path('',views.viewIndex, name="Index"),
    path('logins',views.loginpage,name="loginpage"),
    path('signup', views.signUp, name = "SignUp"),
    path('logout', views.logout, name="logout"),
    path('admin', views.viewAdmin, name="Admin Page"),
    path('addGroup',views.viewAndGroup, name="Add Group"),
    path('addBranches',views.addBranch, name="Add Branch"),
    path('branches',views.viewBranch, name="branches"),
    path('bookings',views.viewBooking, name="bookings"),
    path('delete-branch/<int:id>/',views.deleteBranch, name = 'delete-branch'),

    #consumer
    path('consumer',views.consumer, name="consumer"),
    path('consumer/book-product/<int:id>/', views.bookProduct, name='book-product'),
    path('consumer/book-service/<int:id>/', views.bookService, name='book-service'),
    path('consumer/bookings',views.bookings, name="bookings"),
    path('consumer/complaints', views.complaints, name="complaints"),
    path('consumer/create-complaint', views.createComplaint, name="create-complaint"),
    path('consumer/complaint-details/<int:id>', views.viewComplaintDetails, name='complaint-details'),

    #manager
    path('manager',views.manager, name="manager"),
    path('manager/staffs',views.staffs, name='staffs'),
    path('manager/add-staff',views.addStaff, name='add-staff'),
    path('manager/products', views.products, name='products'),
    path('manager/add-product', views.addProduct, name='add-product'),
    path('manager/update-stock/<int:id>/', views.updateProdStock, name='update-stock'),
    path('manager/works', views.works, name = 'works'),
    path('manager/services', views.viewServices, name='services'),
    path('manager/add-service', views.addService, name='add-service'),

    #staff
    path('staff', views.staff, name='staff'),
    path('staff/work-history', views.viewHistory, name='work-history'),
    path('staff/view-complaints', views.viewComplaints, name='view-complaints'),
    path('staff/resolve-complaint/<int:id>', views.resolveComplaint, name='resolve-complaint'),
    
]