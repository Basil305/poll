from django.urls import path
from . import views

app_name = "poll"

urlpatterns = [
    path('list/', views.polls_list, name='list'),
    path('list/user/', views.list_by_user, name='list_by_user'),
    path('add/', views.polls_add, name='add'),
    path('edit/<int:poll_id>/', views.polls_edit, name='edit'),
    path('delete/<int:poll_id>/', views.polls_delete, name='delete_poll'),
    path('end/<int:poll_id>/', views.endpoll, name='end_poll'),
    path('edit/<int:poll_id>/choice/add/', views.add_choice, name='add_choice'),
    path('edit/choice/<int:choice_id>/', views.choice_edit, name='choice_edit'),
    path('delete/choice/<int:choice_id>/',
         views.choice_delete, name='choice_delete'),
    path('<int:poll_id>/', views.poll_detail, name='detail'),
    path('<int:poll_id>/vote/', views.poll_vote, name='vote'),
    path('poll_result/', views.poll_result, name='poll_result'),
    path('poll_results_show/<int:id>', views.poll_results_show, name='poll_results_show'),


    ]