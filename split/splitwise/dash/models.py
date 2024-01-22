# from django.db import models
# from django.contrib.auth.models import AbstractUser
# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.models import Permission


# class Group(models.Model):
#     name = models.CharField(max_length=100)
#     members = models.ManyToManyField(User)

#     def __str__(self):
#         return self.name

# class Expense(models.Model):
#     description = models.CharField(max_length=200)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField()
#     category = models.CharField(max_length=100)
#     paid_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     # group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
#     user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

#     participants = models.ManyToManyField(User, related_name='expenses_participated')

#     def __str__(self):
#         return self.description

# class Settlement(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"{self.user.username} - {self.expense.description}"







# class CustomUser(AbstractUser):
#     phone_number = models.CharField(max_length=20)

#     # profile_picture = models.ImageField(upload_to='profile_pictures/')
#     # address = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.username

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Group(models.Model):
    
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('CustomUser')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Expense(models.Model):
     
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=100)
    paid_by = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    participants = models.ManyToManyField('CustomUser', related_name='expenses_participated')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.description



class Settlement(models.Model):
    expense = models.ForeignKey('Expense', on_delete=models.CASCADE, null=True)

    payer = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='settlements_paid',null=True)
    
    receiver = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='settlements_received',null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    
    # def __str__(self):
    #     return f"Settlement {self.id}"

    def __str__(self):
        return f"{self.payer.username} - {self.receiver.username}"


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    groups = models.ManyToManyField(Group, related_name='custom_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users', blank=True)
   

    def __str__(self):
        return self.username
