from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



from django.urls import path
from django.shortcuts import redirect
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', lambda request: redirect('login'), name='root'),  # Redirect root URL to login
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    

    path('accounts/forgot_password',views.forgot_password,name='forgot'),
    path('accounts/resetpassword',views.resetpassword,name='reset'),

    # CRUD operations
    path('home/', views.home, name='home'),
    path('create_resume/', views.create_resume, name='create_resume'),
    path('view_resume/<int:resume_id>/', views.view_resume, name='view_resume'),
    path('update_resume/<int:resume_id>/', views.update_resume, name='update_resume'),
    path('delete_resume/<int:resume_id>/', views.delete_resume, name='delete_resume'),  # Added resume_id

    path('download_resume_pdf/<int:resume_id>/', views.download_resume_pdf, name='download_resume_pdf'),

]
