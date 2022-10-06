from django.urls import path
from wishlist import views

app_name = "wishlist"

urlpatterns = [
    path("", views.show_wishlist, name="show_wishlist"),
    path("xml/", views.show_xml, name="show_xml"),
    path("xml/<int:id>/", views.show_xml_by_id, name="show_xml_by_id"),
    path("json/", views.show_json, name="show_json"),
    path("json/<int:id>/", views.show_json_by_id, name="show_json_by_id"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("ajax/", views.show_wishlist_ajax, name="ajax"),
    path("ajax/submit", views.add_wishlist_ajax, name="ajax"),
]
