from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



# Create your models here.

class Teacher_login_informa(models.Model):
    Teacher_ID = models.CharField(max_length=50)
    Teacher_Name = models.CharField(max_length=255)
    Teacher_pass = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='teacher_profiles/', default='teacher_profiles/default_tea.png')
    class Meta:
        verbose_name = "Teacher Information"
        verbose_name_plural = "Teachers Information"
    def __str__(self):
        return self.Teacher_ID

    @staticmethod
    def matching_loging_teacher(userID):
        try:
            return Teacher_login_informa.objects.get(Teacher_ID=userID)
        except:
            return False


class store_email_teach_new(models.Model):
    Teacher_ID = models.CharField(max_length=100)
    Teacher_email = models.CharField(max_length=30)
    class Meta:
        verbose_name = "Teacher Email"
        verbose_name_plural = "All Teacher Emails"
    def __str__(self):
        return self.Teacher_ID

    @staticmethod
    def matching_show_teacher(userID):
        try:
            return store_email_teach_new.objects.get(Teacher_ID=userID)
        except:
            return False


class Student_courses_with_Teacher_name(models.Model):
    course = models.CharField(max_length=200)
    Teacher_ID = models.ForeignKey(Teacher_login_informa, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True, null=True)
    class_schedule = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "All Courses"
        
    def __str__(self):
        return self.course
    def seats_remaining(self):
        max_seats = 30
        current_enrollments = self.students.count()
        return max_seats - current_enrollments


class Student(models.Model):
    Student_ID = models.CharField(max_length=225, unique=True)
    Student_Name = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='student_profiles/', default='student_profiles/default_stu.png')
    Student_pass = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Student Information"
        verbose_name_plural = "Students Information"
    def __str__(self):
        return self.Student_ID

    @staticmethod
    def matching_loging_stu(userID):
        try:
            return Student.objects.get(Student_ID=userID)
        except:
            return False


class store_email_stu_new(models.Model):
    Student_ID = models.CharField(max_length=100)
    Student_email = models.CharField(max_length=30)
    class Meta:
        verbose_name = "Student Email"
        verbose_name_plural = "All Student Emails"
    def __str__(self):
        return self.Student_ID

    @staticmethod
    def matching_show_stu(userID):
        try:
            return store_email_stu_new.objects.get(Student_ID=userID)
        except:
            return False


class Teacher_Assignment_upload_File(models.Model):
    Assignment_name = models.CharField(max_length=500)
    course = models.CharField(max_length=500)
    date = models.DateField(default=timezone.now, blank=True)
    due_date = models.DateField(default=timezone.now, blank=True)
    title = models.CharField(max_length=500)
    Details = models.TextField(max_length=500)
    attachment = models.CharField(max_length=1000)
    resource = models.CharField(max_length=500)
    posts = models.CharField(max_length=500)
    Out_Of_Grade = models.CharField(max_length=500)
    class Meta:
        verbose_name = "Assignment"
        verbose_name_plural = "Assignments"

    def __str__(self):
        return self.Assignment_name


class Student_Submit_Assignment_pro(models.Model):
    attachment = models.CharField(max_length=1000)
    course = models.CharField(max_length=1000)
    Student_ID = models.CharField(max_length=1000)
    Assignment_name = models.CharField(max_length=1000)
    Submitted_at = models.DateTimeField(auto_now_add=True) 
    class Meta:
        verbose_name = "Student Assignment"
        verbose_name_plural = "Student Assignments"
    


class Grade_Student(models.Model):
    Student_ID = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    Assignment_name = models.CharField(max_length=200)
    Grade = models.CharField(max_length=200)
    Out_Of_Grade = models.CharField(max_length=200)
    class Meta:
        verbose_name = "Grade student"
        verbose_name_plural = "Grade students"

    def __str__(self):
        return self.Student_ID


class Assignment_Comments(models.Model):
    serial_no = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    postID = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    time_comment = models.DateTimeField(default=timezone.now, blank=True)
    class Meta:
        verbose_name = "Assignemt Comment"
        verbose_name_plural = "Assignment comments"
    def __str__(self):
        return self.comment[0:12] + ".... " + " by " + self.user




class Employee(models.Model):
    EMPLOYEE_TYPES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
    )

    EMPLOYEE_STATUSES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    employee_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    hire_date = models.DateField()
    employee_type = models.CharField(max_length=20, choices=EMPLOYEE_TYPES, default='full_time')
    status = models.CharField(max_length=20, choices=EMPLOYEE_STATUSES, default='active')
    roles = models.ManyToManyField('Role', through='EmployeeRole')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.employee_id}"

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class EmployeeRole(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee} - {self.role}"

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name()

class Course(models.Model):
    name = models.CharField(max_length=255)
    total_seats = models.IntegerField(default=30)
    course = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100, blank=True, null=True)
    schedule = models.CharField(max_length=100, blank=True, null=True)  # e.g., "Mon & Wed 10-11 AM"
    location = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.course

    


    

class Enrollment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey(Student_courses_with_Teacher_name, on_delete=models.CASCADE, related_name='students')
    enrolled_on = models.DateTimeField(auto_now_add=True)

    def seats_remaining(self):
            max_seats = 30
            current_enrollments = self.enrolled_on.count()  # use the related_name from Enrollment
            return max_seats - current_enrollments

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"

    def __str__(self):
        return f"{self.student.Student_Name} -> {self.course.course}"


    class Meta:
        unique_together = ('student', 'course')