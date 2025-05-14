from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from schoolapp.models import (
    Teacher_login_informa, Course, Student,
    Student_courses_with_Teacher_name, Enrollment,
    Teacher_Assignment_upload_File, Assignment_Comments
)

# --------------------------
# Class 1: Admin & Login Tests
# --------------------------
class AdminAndLoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.student = Student.objects.create(Student_ID="stu999", Student_Name="Bob", Student_pass="secret123")

    def test_admin_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_login_logout(self):
        response = self.client.post(reverse("login"), {"log_ID": "dummy", "log_password": "pass"})
        self.assertIn(response.status_code, [200, 302])
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)

    def test_student_login_success(self):
        response = self.client.post(reverse("login"), {"log_ID": "stu999", "log_password": "secret123"})
        self.assertEqual(response.status_code, 302)

    def test_student_login_wrong_password(self):
        response = self.client.post(reverse("login"), {"log_ID": "stu999", "log_password": "wrongpass"})
        self.assertEqual(response.status_code, 200)

    def test_student_login_invalid_id(self):
        response = self.client.post(reverse("login"), {"log_ID": "invalid_user", "log_password": "any"})
        self.assertEqual(response.status_code, 200)

# ------------------------------------------
# Class 2: Student Course Enroll/Unenroll
# ------------------------------------------
class StudentEnrollmentTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.teacher = Teacher_login_informa.objects.create(Teacher_ID="T1", Teacher_Name="Prof A", Teacher_pass="pass")
        self.course = Student_courses_with_Teacher_name.objects.create(course="Physics", Teacher_ID=self.teacher, location="Lab")
        self.student = Student.objects.create(Student_ID="S1", Student_Name="Eve", Student_pass="123")
        session = self.client.session
        session["Stu_id"] = self.student.Student_ID
        session["Stu_name"] = self.student.Student_Name
        session.save()

    def test_enroll_course(self):
        response = self.client.get(reverse("enroll_course", args=[self.course.id]))
        self.assertIn(response.status_code, [200, 302])

    def test_unenroll_course(self):
        Enrollment.objects.create(student=self.student, course=self.course)
        response = self.client.get(reverse("unenroll_course", args=[self.course.id]))
        self.assertIn(response.status_code, [200, 302])

# ----------------------------------
# Class 3: Teacher Assignment & Grade
# ----------------------------------
class TeacherAssignmentTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.teacher = Teacher_login_informa.objects.create(Teacher_ID="T2", Teacher_Name="Dr. Jane", Teacher_pass="abc")
        self.course = Student_courses_with_Teacher_name.objects.create(course="Chemistry", Teacher_ID=self.teacher, location="Lab")
        session = self.client.session
        session["Teacher_id"] = self.teacher.Teacher_ID
        session["Teacher_name"] = self.teacher.Teacher_Name
        session.save()

    def test_teacher_upload_assignment(self):
        file = SimpleUploadedFile("assignment.pdf", b"dummy content", content_type="application/pdf")
        response = self.client.post(reverse("add_assignment"), {"file": file, "description": "Unit 1"})
        self.assertIn(response.status_code, [200, 302])

    def test_access_upload_assignment_page(self):
        response = self.client.get(reverse("add_assignment_up_page"))
        self.assertIn(response.status_code, [200, 302])

    def test_invalid_assignment_submission(self):
        response = self.client.post(reverse("add_assignment"), {})
        self.assertEqual(response.status_code, 200)

# ---------------------------------------
# Class 4: Communication (Student & Teacher)
# ---------------------------------------
class CommunicationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.teacher = Teacher_login_informa.objects.create(Teacher_ID="T3", Teacher_Name="Dr. Talk", Teacher_pass="talk123")
        self.course = Student_courses_with_Teacher_name.objects.create(course="English", Teacher_ID=self.teacher, location="Classroom")
        self.student = Student.objects.create(Student_ID="S3", Student_Name="Charlie", Student_pass="talkpass")
        session = self.client.session
        session["Stu_id"] = self.student.Student_ID
        session["Stu_name"] = self.student.Student_Name
        session.save()

    def test_post_comment(self):
        assignment = Teacher_Assignment_upload_File.objects.create(
            Assignment_name="Essay", course=self.course.course, title="Essay", Details="Topic A",
            attachment="file.pdf", resource="book", posts="note", Out_Of_Grade="100")

        response = self.client.post(reverse("postComments"), {
            "comment_ass": "Good!",
            "comment_username": self.student.Student_Name,
            "ass_id": assignment.id,
            "serial_no": ""
        })
        self.assertIn(response.status_code, [200, 302])

    def test_reply_to_comment(self):
        assignment = Teacher_Assignment_upload_File.objects.create(
            Assignment_name="Essay 2", course=self.course.course, title="Essay", Details="Topic B",
            attachment="essay2.pdf", resource="notes", posts="feedback", Out_Of_Grade="100")

        parent = Assignment_Comments.objects.create(
            comment="Well done!", user="Teacher", post=assignment.Assignment_name, postID=str(assignment.id))

        response = self.client.post(reverse("postComments"), {
            "comment_ass": "Thank you!",
            "comment_username": self.student.Student_Name,
            "ass_id": assignment.id,
            "serial_no": parent.serial_no
        })
        self.assertIn(response.status_code, [200, 302])

# ---------------------------------------------
# Class 5: Student Info, Course Creation, Assignment Submission
# ---------------------------------------------
class StudentCourseAssignmentFlowTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.teacher = Teacher_login_informa.objects.create(Teacher_ID="T888", Teacher_Name="Mr. Build", Teacher_pass="buildpass")
        self.course = Student_courses_with_Teacher_name.objects.create(course="Geography", Teacher_ID=self.teacher, location="Room A")
        self.student = Student.objects.create(Student_ID="S888", Student_Name="Nina", Student_pass="ninapass")
        session = self.client.session
        session["Stu_id"] = self.student.Student_ID
        session["Stu_name"] = self.student.Student_Name
        session.save()

    def test_create_teacher_and_assign_course(self):
        self.assertEqual(self.course.Teacher_ID.Teacher_Name, "Mr. Build")
        self.assertEqual(self.course.course, "Geography")

    def test_student_info_display(self):
        self.assertEqual(self.student.Student_Name, "Nina")
        self.assertEqual(self.student.Student_ID, "S888")

    def test_student_submit_assignment(self):
        file = SimpleUploadedFile("assignment.pdf", b"file content", content_type="application/pdf")
        response = self.client.post(reverse("submit_assignment_student"), {
            "ass_name_stu_submit1": "Geo Assignment",
            "cor_name_stu_submit1": self.course.id,
            "stu_id_stu_submit1": self.student.Student_ID,
            "attachment_ass_sub": file
        })
        self.assertIn(response.status_code, [200, 302])
