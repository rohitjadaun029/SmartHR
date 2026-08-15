from django.db import models


class Employee(models.Model):

    DEPARTMENT_CHOICES = [
        ("HR", "Human Resources"),
        ("IT", "Information Technology"),
        ("Finance", "Finance"),
        ("Accounting", "Accounting"),
        ("Sales", "Sales"),
        ("Marketing", "Marketing"),
        ("Operations", "Operations"),
        ("Administration", "Administration"),
        ("Customer Support", "Customer Support"),
        ("Research & Development", "Research & Development"),
        ("Production", "Production"),
        ("Quality Assurance", "Quality Assurance"),
        ("Legal", "Legal"),
        ("Procurement", "Procurement"),
        ("Supply Chain", "Supply Chain"),
        ("Engineering", "Engineering"),
        ("Design", "Design"),
        ("Security", "Security"),
        ("Management", "Management"),
    ]

    DESIGNATION_CHOICES = [
        ("CEO", "Chief Executive Officer"),
        ("CTO", "Chief Technology Officer"),
        ("CFO", "Chief Financial Officer"),
        ("COO", "Chief Operating Officer"),

        ("HR Manager", "HR Manager"),
        ("HR Executive", "HR Executive"),
        ("HR Assistant", "HR Assistant"),

        ("Project Manager", "Project Manager"),
        ("Team Lead", "Team Lead"),

        ("Software Engineer", "Software Engineer"),
        ("Software Developer", "Software Developer"),
        ("Web Developer", "Web Developer"),
        ("Frontend Developer", "Frontend Developer"),
        ("Backend Developer", "Backend Developer"),
        ("Full Stack Developer", "Full Stack Developer"),
        ("Python Developer", "Python Developer"),

        ("Data Analyst", "Data Analyst"),
        ("Data Scientist", "Data Scientist"),
        ("Business Analyst", "Business Analyst"),

        ("DevOps Engineer", "DevOps Engineer"),
        ("Cloud Engineer", "Cloud Engineer"),
        ("QA Engineer", "QA Engineer"),
        ("System Administrator", "System Administrator"),

        ("UI/UX Designer", "UI/UX Designer"),
        ("Graphic Designer", "Graphic Designer"),

        ("Accountant", "Accountant"),
        ("Finance Manager", "Finance Manager"),

        ("Sales Executive", "Sales Executive"),
        ("Sales Manager", "Sales Manager"),

        ("Marketing Executive", "Marketing Executive"),
        ("Marketing Manager", "Marketing Manager"),

        ("Customer Support Executive", "Customer Support Executive"),

        ("Business Development Executive", "Business Development Executive"),

        ("Operations Manager", "Operations Manager"),
        ("Operations Executive", "Operations Executive"),

        ("Intern", "Intern"),
        ("Trainee", "Trainee"),
    ]

    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    department = models.CharField(
        max_length=100,
        choices=DEPARTMENT_CHOICES
    )

    designation = models.CharField(
        max_length=100,
        choices=DESIGNATION_CHOICES
    )

    joining_date = models.DateField()

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"