from django.urls import path
from hospital.views import test_helloworld, doctors_info, doctors_individual_info, add_doctors,delete_doctor

urlpatterns = [
    path('test/', test_helloworld, name='test_endpoint'),
    path('doc-info/', doctors_info, name='Doctos information'),
    path('individual-doc-info/<int:id>', doctors_individual_info, name='individual docs infor'),
    path('add-doctors-info/', add_doctors, name='add doctors info'),
    path('doc-info/remove/<str:email>', delete_doctor, name='delete doctors info'),
]
