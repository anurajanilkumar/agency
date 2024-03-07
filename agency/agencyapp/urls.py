from django.urls import path
from agencyapp import views

urlpatterns=[

    path('',views.viewIndex, name="Index"),
    path('logins',views.loginpage,name="loginpage"),
    path('signup', views.signUp, name = "SignUp"),
    path('admin', views.viewAdmin, name="Admin Page"),
    path('addGroup',views.viewAndGroup, name="Add Group"),
    path('addBranches',views.addBranch, name="Add Branch"),
    path('branches',views.viewBranch, name="branches"),
    path('bookings',views.viewBooking, name="bookings"),
    path('delete-branch/<int:id>/',views.deleteBranch, name = 'delete-branch'),

    #consumer
    path('consumer',views.consumer, name="consumer"),
    path('book-product/<int:id>/', views.bookProduct, name='book-product'),
    path('book-service/<int:id>/', views.bookService, name='book-service'),
    path('bookings',views.bookings, name="bookings"),
    path('complaints', views.complaints, name="complaints"),
    path('create-complaint', views.createComplaint, name="create-complaint"),
    path('complaint-details/<int:id>', views.viewComplaintDetails, name='complaint-details'),

    #manager
    path('manager',views.manager, name="manager"),
    path('staffs',views.staffs, name='staffs'),
    path('add-staff',views.addStaff, name='add-staff'),
    path('products', views.products, name='products'),
    path('add-product', views.addProduct, name='add-product'),
    path('update-stock/<int:id>/', views.updateProdStock, name='update-stock'),
    path('works', views.works, name = 'works'),
    path('services', views.viewServices, name='services'),
    path('add-service', views.addService, name='add-service'),

    #staff
    path('staff', views.staff, name='staff'),
    path('work-history', views.viewHistory, name='work-history'),
    path('view-complaints', views.viewComplaints, name='view-complaints'),
    path('resolve-complaint/<int:id>', views.resolveComplaint, name='resolve-complaint'),
    
]