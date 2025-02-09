from django.shortcuts import render ,redirect
from django.urls import path
from auth_system.auth_manager import user_login, user_logout
from auth_system.utils import dashboard
from auth_system.dashboard_content import get_dashboard_content

from .models import Admin
from django.contrib.auth.decorators import login_required

# @login_required
# def dashboard_view(request):
#     # Dummy data for sales metrics
#     sales_data = {
#         "active_users": 100,  
#         "premium_users": 50,  
#         "total_users": 500,  
#         "total_employees": 30,  
#         "total_superadmins": 5,  
#         "total_admins": 10,  
#         "total_managers": 20,  
#         "total_sale": "10L",  
#         "yearly_sale": "10.2k",  
#         "monthly_sale": "4.2k",  
#         "weekly_sale": "80L",  
#         "daily_sale": "10L",  
#     }

#     return render(request, 'dashboard.html', sales_data)

# @login_required
# def manage_admin_view(request):
#     admins = Admin.objects.all()
#     print(admins)
#     return render(request, 'dashboard.html', {"admins": admins})


# def dashboard_view(request):
#     user_role = request.user.role  # Assuming role is stored in user model
#     content_permissions = get_dashboard_content(user_role)

#     return render(request, "dashboard.html", {"content_permissions": content_permissions})

def dashboard(request):
    admins = Admin.objects.all()  # Load all admins
    return render(request, 'dashboard.html', {'admins': admins})

def add_admin(request):
    if request.method == "POST":
        admin_name = request.POST.get("admin_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        admin_id = request.POST.get("admin_id")

        # Generate next Sno
        last_admin = Admin.objects.order_by('-Sno').first()  # Get latest record
        next_sno = str(int(last_admin.Sno) + 1) if last_admin and last_admin.Sno else "1"

        # Save to database
        Admin.objects.create(Sno=next_sno, admin_name=admin_name, email=email, password=password, phone=phone, admin_id=admin_id)

        return redirect('dashboard')  # Redirect to dashboard

    return redirect('dashboard')  # Fallback redirect