from . import views
from django.urls import path
app_name='footballapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('team/<int:team_id>/',views.detail,name='detail'),
    path('add/',views.add_team,name='add_team'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]
