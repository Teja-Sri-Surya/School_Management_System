
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_func, name='login') ,
    path('logout', views.logout_func, name='logout'),
    path('profile', views.profile, name='profile'),
    path('upload_profile_pic', views.upload_profile_pic, name='upload_profile_pic'),
    path('settings', views.settings, name='settings'),
    path('check_user', views.check_user, name='check_user'),
    path('check_user_password', views.check_user_password, name='check_user_password'),
    path('check_user_student', views.check_user_student, name='check_user_student'),
    path('check_user_password_student', views.check_user_password_student, name='check_user_password_student'),
    path('stu_course', views.stu_course, name='stu_course'),
    path('submit_assignment', views.submit_assignment, name='submit_assignment'),
    path('submit_assignment_student', views.submit_assignment_student, name='submit_assignment_student'),
    path('sir_course', views.sir_course, name='sir_course'),
    path('assignment_page', views.assignment_page, name='assignment_page'),
    path('grading_page', views.grading_page, name='grading_page'),
    path('grading_submit', views.grading_submit, name='grading_submit'),
    path('add_assignment', views.add_assignment, name='add_assignment'),
    path('add_assignment_up_page', views.add_assignment_up_page, name='add_assignment_up_page'),
    path('stu_id_details', views.stu_id_details, name='stu_id_details'),
    path('postComments', views.postComments, name='postComments'),
    path('courses/', views.available_courses, name='available_courses'),
    path('courses/enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
    path('update_change_password/93875995<str:pk>87438737/345', views.update_change_password, name='update_change_password'),
    path('update_change_password/5564995<str:pk>87436565547/345', views.update_change_password_stu, name='update_change_password_stu'),
    path('my-courses/', views.my_enrolled_courses, name='my_courses'),
    path('courses/seats/<int:course_id>/', views.course_seat_count, name='seat_count'),
    path('courses/unenroll/<int:course_id>/', views.unenroll_course, name='unenroll_course'),


]
