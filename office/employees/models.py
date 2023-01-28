from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Custom User Manager.
class HR_admin(BaseUserManager):
    def create_user(self, email, tc,  password=None, password1=None):
        """
        Creates and saves a User with the given email, tc, password and password1.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            tc=tc
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, tc, password=None):
        """
        Creates and saves a superuser with the given email, tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            tc=tc
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Custom your office models here.
class Employees_data(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    objects = HR_admin()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True 

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class EmployeePersonalInfo(models.Model):
    MARTIAL_STATUS = (
        ('Married','Married'),
        ('UnMarried','UnMarried'),
        ('Divorced','Divorced'),
        ('Widow','Widow'), 
    )
    CASTE = (
        ('OPEN', 'OPEN'),
        ('SC','SC'),
        ('ST','ST'),
        ('OBC', 'OBC'),    
    )
    personal_id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    user = models.ForeignKey(Employees_data, on_delete=models.CASCADE)
    DOB = models.DateField()
    department = models.CharField(max_length=200)
    martial_status = models.CharField(choices=MARTIAL_STATUS, max_length=200)
    caste = models.CharField(max_length=200, choices=CASTE)
    City = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    
    def __str__(self) -> str:
        return self.user.email