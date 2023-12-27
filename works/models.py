# job_app/models.py
from django.db import models
from django.forms import ModelForm
from random import choices


class Company(models.Model):
    
    name = models.CharField(max_length = 200)
    Website = models.CharField(max_length = 300)
    Industry = models.CharField(max_length = 200)
    EstablishedYear = models.CharField(max_length = 200)
    Introduction = models.TextField()

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Companies'   


class Provinces(models.Model):
    
    PROVINCES_CHOICES = (
        ('Tehran', 'Tehran') ,
        ('Khorasan Razavi' , 'Khorasan Razavi') ,
        ('Isfahan' , 'Isfahan') ,
        ('Alborz', 'Alborz') ,
        ('Fars', 'Fars') ,
        ('Qom' , 'Qom'),
        ('East Azerbaijan' , 'East Azerbaijan') ,
        ('Mazandaran', 'Mazandaran'), 
        ('Gilan', 'Gilan') ,
        ('Kerman', 'Kerman'),
        ('Khozestan', 'Khozestan'),
        ('Yazd', 'Yazd'),
        ('Markazi', 'Markazi'),
        ('Qazvin', 'Qazvin'),
        ('Hormozgan', 'Hormozgan'),
        ('Golestan', 'Golestan'), 
        ('Zanjan', 'Zanjan'),
        ('Hamedan', 'Hamedan') ,
        ('Semnan', 'Semnan'),
        ('West Azerbaijan', 'West Azerbaijan'),
        ('Boushehr', 'Boushehr'),
        ('Kordestan', 'Kordestan'),
        ('Kermanshah', 'Kermanshah'),
        ('Sistan Balouchestan', 'Sistan Balouchestan'),
        ('Charmahal Bakhtiari' , 'Charmahal Bakhtiari'),
        ('Ardebil', 'Ardebil'),
        ('Kohkiluyeh and Boyerahmad' , 'Kohkiluyeh and Boyerahmad'),
        ('Ilam', 'Ilam'),
        ('Khorasan Jonoubi', 'Khorasan Jonoubi'),
        ('Khorestan Shomali', 'Khorestan Shomali'),
        ('Lorestan', 'Lorestan')
     )
    name = models.CharField(max_length=30 , choices = PROVINCES_CHOICES)

    def __str__(self):
        return self.name 


    class Meta:
        verbose_name_plural = 'Provinces'    


class Category(models.Model):
    
    CATEGORY_CHOICES = (
        ('Sales and Marketing' , 'Sales and Marketing') ,
        ('Software and Programming' , 'Software and Programming') , 
        ('Finantial and Accounting' , 'Finantial and Accounting') ,
        ('Official' , 'Official') ,
        ('DigitalMarketing' , 'DigitalMarketing') ,
        ('ContentProduction' , 'ContentProduction') ,
        ('It Devops Server', 'It Devops Server') ,
        ('Design' , 'Design') ,
        ('Customer Support' , 'Customer Support') , 
        ('Industrial Enginerring' , 'Industrial Enginerring') , 
        ('Electrical Engineering' , 'Electrical Engineering') , 
        ('Civil Engineering' , 'Civil Engineering') ,
        ('Human Resources' , 'Human Resources') , 
        ('Servise Force' , 'Servise Force') ,
        ('Education' , 'Education') , 
        ('Inventory', 'Inventory') ,
        ('Cinema Feild' , 'Cinema Feild') ,
        ('Mechanical and Aerospace Engineering' , 'Mechanical and Aerospace Engineering') ,
        ('Technician' , 'Technician') ,
        ('Tourism' , 'Tourism') , 
        ('Product Manager' , 'Product Manager') ,
        ('Medical' , 'Medical') , 
        ('TTransportation' , 'Transportation') ,
        ('HotelManagement' , 'HotelManagement') ,
        ('Public Relations' , 'Public Relations') ,
        ('Chemical Petronum' , 'Chemical Petronum') ,
        ('Insurance Management' , 'Insurance Management') ,
        ('Mine and Metalogy Engineering', 'Mine and Metalogy Engineering'),
        ('Biomedical Engineering', 'Biomedical Engineering') ,
        ('TE' , 'Txtile Engineering') ,
        ('Pharmacology','Pharmacology') , 
        ('Journalist' , 'Journalist') ,
        ('Agricultural Engineering' , 'Agricultural Engineering') ,
        ('Musical and Sound Engineering' , 'Musical and Sound Engineering') ,
        ('Physical Education', 'Physical Education')     
    )
    
    name = models.CharField(max_length=200, choices = CATEGORY_CHOICES)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = 'Categories'


class Job(models.Model):
    
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Provinces,on_delete=models.CASCADE)
    employer = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    min_salary = models.DecimalField(max_digits = 10, decimal_places = 2)
    max_salary = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return self.title 


    class Meta:
        verbose_name_plural = 'Jobs'


class JobSeeker(models.Model):
    
    GENDER_CHOICES = (
        ('Male' , 'Male') ,
        ('Female' , 'Female') ,
        ('Others' , 'Others')
    )
    MARITAL_CHOICES = (
        ('Married' , 'Married') ,
        ('Single' , 'Single')
    )

    name = models.CharField(max_length = 200)
    email_adress = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=12)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, choices = GENDER_CHOICES)
    marital_status = models.CharField(max_length=10, choices = MARITAL_CHOICES)
    residence = models.CharField(max_length=100)
    cv = models.TextField()

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural = 'JobSeekers'