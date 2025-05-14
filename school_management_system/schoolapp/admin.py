from django.contrib import admin
from .models import Course, Enrollment, store_email_teach_new, store_email_stu_new,  Teacher_login_informa, Student_courses_with_Teacher_name, Student, Grade_Student, Student_Submit_Assignment_pro, Assignment_Comments, Teacher_Assignment_upload_File, Employee, Role, EmployeeRole
# Register your models here.



admin.site.register(store_email_teach_new)
admin.site.register(store_email_stu_new)
admin.site.register(Teacher_login_informa)
admin.site.register(Student_courses_with_Teacher_name)
admin.site.register(Student)
admin.site.register(Grade_Student)
admin.site.register(Student_Submit_Assignment_pro)
admin.site.register(Assignment_Comments)
admin.site.register(Teacher_Assignment_upload_File)
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(EmployeeRole)
