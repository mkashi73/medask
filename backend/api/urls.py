from django.urls import path
from api import views
from jpa import views as jpa_view
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

routers.register('roles', views.RoleViewSet, basename='role')
routers.register('users', views.UserViewSet, basename='user')
routers.register('candidates_data', views.CandidatePrivateViewSet, basename='candidate')
routers.register('candidates', views.CandidateViewSet, basename='candidate')
routers.register('candidates_edu', views.CandidateEduViewSet, basename='candidate')
routers.register('candidate_prev_candidature', views.CandidatePrevCandidatureViewSet, basename='candidate')


routers.register('users-unpaginated', views.UserListViewSet, basename='user')


routers.register('question', views.QuestionViewSet, basename='question')
routers.register('question_option', views.QuestionOptionViewSet, basename='question_option')


routers.register('center', views.CenterViewSet, basename='center')
routers.register('center_list', views.CenterListViewSet, basename='center_list')

routers.register('batch', views.BatchesViewSet, basename='batch')
routers.register('batch_list', views.BatchesListViewSet, basename='batch_list')

routers.register('course', views.CoursesViewSet, basename='course')
routers.register('course_list', views.CoursesListViewSet, basename='course_list')

routers.register('discipline', views.DisciplineViewSet, basename='discipline')
routers.register('discipline_list', views.DisciplineListViewSet, basename='discipline_list')

routers.register('distt', views.DisttViewSet, basename='distt')
routers.register('distt_list', views.DisttListViewSet, basename='distt_list')

routers.register('tehsil', views.TehsilViewSet, basename='tehsil')
routers.register('tehsil_list', views.TehsilListViewSet, basename='tehsil_list')

routers.register('province', views.ProvinceViewSet, basename='province')
routers.register('province_list', views.ProvinceListViewSet, basename='province_list')

routers.register('language', views.LanguageViewSet, basename='language')
routers.register('language_list', views.LanguageListViewSet, basename='language_list')

routers.register('profession', views.ProfessionViewSet, basename='profession')
routers.register('profession_list', views.ProfessionListViewSet, basename='profession_list')

routers.register('qualtype', views.QualTypeViewSet, basename='qualtype')
routers.register('qualtype_list', views.QualtypeListViewSet, basename='qualtype_list')

routers.register('rank', views.RankViewSet, basename='rank')
routers.register('rank_list', views.RankListViewSet, basename='rank_list')

routers.register('religion', views.ReligionViewSet, basename='religion')
routers.register('religion_list', views.ReligionListViewSet, basename='religion_list')

routers.register('education_board', views.EducationBoardViewSet, basename='education_board')
routers.register('education_board_list', views.EducationBoardListViewSet, basename='education_board_list')

routers.register('sect', views.SectViewSet, basename='sect')
routers.register('sect_list', views.SectListViewSet, basename='sect_list')


# routers.register('send_web_mail', views.SendEmail, basename='send_web_mail')

#JPA Routes
routers.register('migrate_database', jpa_view.MigrateViewSet, basename='migrate_database')
routers.register('generate_excel', jpa_view.MigrateExcelViewSet, basename='generate_excel')



urlpatterns = [
    path('login', views.LoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('refresh', views.RefreshView.as_view()),
    path('current', views.CurrentUserView.as_view()),
    path('permissions', views.PermissionListView.as_view()),
    path('course_wise_report', views.CourseWiseReport.as_view()),
    path('discipline_wise_report', views.DisciplineWiseReport.as_view()),
    path('course_count_dashboard_data', views.CenterWiseDashboardData.as_view()),
    path('overall_dashboard_data', views.OverallRegistrationData.as_view()),
    path('centers_reg_data', views.CenterWiseRegistrationData.as_view()),
    path('courses_dashboard_data', views.CourseWiseRegistrationData.as_view()),
    # path('send_web_mail', views.SendEmailView.as_view()),
]

urlpatterns += routers.urls
