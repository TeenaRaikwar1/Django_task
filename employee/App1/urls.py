from django.contrib import admin
from django.urls import path
from App1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empdata/',views.display,name='display'),
    path('addemp/', views.addEmpData, name='addemp'),
    path('editdata/<int:id>/',views.updateEmpData,name='editdata'),
    path('deletedata/<int:id>/',views.deleteEmpData,name='deletedata')
]
