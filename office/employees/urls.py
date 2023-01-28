from django.urls import path
from employees.views import EmployeeRegistrationView, EmployeeLoginView, EmployeeChangePasswordView, EmployeePersonalInfoView


urlpatterns = [
    path('register/', EmployeeRegistrationView.as_view(), name='register'),
    path('login/', EmployeeLoginView.as_view(), name='login'),
    path('changepassword/', EmployeeChangePasswordView.as_view(), name='changepassword'),
    path('info/', EmployeePersonalInfoView.as_view(), name='info'),
    path('info/<int:pk>', EmployeePersonalInfoView.as_view(), name='info'),

]
