from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_main, name='api-main'),
    path('users/all', views.get_all_users, name='get_all_users'),
    path('user/register', views.register_user, name='user_register'),
    path('user/notes', views.get_notes_for_user, name='get_notes_for_user'),
    path('user/delete', views.delete_user, name='delete_user'),
    path('notes/all', views.get_all_notes, name='get_all_notes'),
    path('note/create', views.create_note, name='create_note'),
    path('note/delete/<str:note_id>', views.delete_note, name='delete_note'),
    path('note/update/<str:note_id>', views.update_note, name='update_note')
]
