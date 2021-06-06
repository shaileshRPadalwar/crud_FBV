from django.urls import path
from empdetails import views
urlpatterns=[

    path('',views.home_view),
    path('insert/',views.insert_view),
    path('delete/<id>/',views.delete_view),
    path('update/<id>/',views.update_view),

]


