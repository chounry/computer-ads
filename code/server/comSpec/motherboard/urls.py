from django.urls import path
from . import views


urlpatterns = [
    path('motherboard/',views.mBoardView,name = 'all_mBoard')
]