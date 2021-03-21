from django.urls import path
from .views import home_view, del_contact,updateContact, contacts_view, del_contact_from_updatePage
urlpatterns = [
    path('', home_view, name='home'),
    path('del/<int:pk>', del_contact, name='del'),
    path('update/<int:pk>', updateContact, name='update'),
    path('update/del/<int:pk>', del_contact_from_updatePage, name='del_update'),
    path('contacts/', contacts_view, name='contacts'),
]


