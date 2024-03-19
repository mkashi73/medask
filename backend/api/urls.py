from django.urls import path
from api import views
# from jpa import views as jpa_view
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

routers.register('roles', views.RoleViewSet, basename='role')
routers.register('users', views.UserViewSet, basename='user')
routers.register('users-unpaginated', views.UserListViewSet, basename='user')

# routers.register('send_web_mail', views.SendEmail, basename='send_web_mail')

#JPA Routes
# routers.register('migrate_database', jpa_view.MigrateViewSet, basename='migrate_database')
# routers.register('generate_excel', jpa_view.MigrateExcelViewSet, basename='generate_excel')



urlpatterns = [
    path('login', views.LoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('refresh', views.RefreshView.as_view()),
    path('current', views.CurrentUserView.as_view()),
    path('permissions', views.PermissionListView.as_view()),
    # path('send_web_mail', views.SendEmailView.as_view()),
]

urlpatterns += routers.urls
