from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_task, name='addTask'),
    path('undo/<task_id>', views.undo_task, name='undoTask'),
    path('cmpl/<task_id>', views.cmpl_task, name='completeTask'),
    path('delcmpl', views.del_cmpl, name='deleteCompleted'),
    path('delall', views.del_all, name='deleteAll'),
]
