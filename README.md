# 🏫 School Management System (Django + PostgreSQL)

A comprehensive **School Management System** web application built using **Django** and **PostgreSQL**, designed to simplify the administrative processes of educational institutions. This system supports managing students, teachers, courses, assignments, enrollments, and more through a user-friendly interface.

---

## 📚 Overview

Educational institutions often face challenges managing large amounts of data related to students, faculty, classes, schedules, and performance tracking. This **School Management System (SMS)** addresses these challenges by offering a centralized platform where:

- Admins can manage teachers, students, and course offerings
- Teachers can create assignments, manage enrollments, and track student progress
- Students can view course content and submit assignments
- All users have role-based access controls to ensure security and proper usage

The system ensures streamlined communication, data integrity, and real-time updates across school operations.

---

## 🎯 Key Features

- 👨‍🏫 Teacher & Student Management (CRUD operations)
- 📚 Course & Subject Management
- 📋 Assignment Creation & Submission Tracking
- 🎓 Student Enrollments with performance records
- 🔐 Role-based Access Control (Admin, Teacher, Student)
- 🗂️ Dashboard for each user type
- 📊 Student Performance Tracking
- 📅 Schedule & Timetable Support (optional)
- ✉️ Notification system for deadlines or updates (extendable)
- 🧪 Unit Testing with Django TestCase
- REST API (Optional extension)

---

## 🛠️ Tech Stack

| Layer         | Technology          |
|--------------|---------------------|
| Backend       | Django (Python)     |
| Database      | PostgreSQL          |
| Frontend      | HTML5, CSS3, Bootstrap |
| Authentication| Django's Auth System |
| Admin Panel   | Django Admin        |
| Optional APIs | Django REST Framework |

---

## 📁 Project Structure

```
school_management_system/
├── core/                     # Core application (models, views, urls)
│   ├── models.py             # Student, Teacher, Course, Enrollment, etc.
│   ├── views.py              # Logic for handling user interactions
│   ├── forms.py              # Forms for input validation
│   ├── tests.py              # Django TestCases
├── templates/                # HTML templates
├── static/                   # CSS, JS, image assets
├── media/                    # Uploaded files
├── manage.py                 # Django's command-line utility
├── db.sqlite3 / PostgreSQL   # Database (prefer PostgreSQL in production)
└── requirements.txt          # Dependencies
```

---

## ⚙️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/your-username/school_management_system.git
cd school_management_system
```

2. **Set up the virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure PostgreSQL DB** in `settings.py` or use SQLite for testing

5. **Run migrations**

```bash
python manage.py migrate
```

6. **Create superuser**

```bash
python manage.py createsuperuser
```

7. **Start the development server**

```bash
python manage.py runserver
```

---

## 🧪 Running Tests

```bash
python manage.py test
```

Covers model relationships, views, and custom business logic.

---

## 🌍 Future Enhancements

- Integration with email/SMS for notifications
- Attendance tracking module
- Parent portal access
- RESTful API using Django REST Framework
- Payment & fee tracking

---

## 📄 License

MIT License – feel free to use, modify, and enhance this project.

---

## 👨‍💻 Author & Contributions

Developed by Ambati Teja Sri Surya 
Open to contributions. Fork the repo and open a pull request!
