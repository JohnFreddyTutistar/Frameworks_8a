from django.db import models
from django.db.models.expressions import CombinedExpression

class user(models.Model) :
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    id_identification_type = models.ForeignKey().IntegerField(max_length=10)
    number_id = models.CharField(max_length = 15)
    id_city = models.ForeignKey().CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    password = models.CharField(max_length = 200)
    status = models.BooleanField()
    created_at = models.DateField(default=now)
    update_at = models.DateField(default=1)
    delete_at = models.DateField(default=1)

class session(models.Model) :
    id_user = models.ForeignKey().IntegerField() 
    ip = models.CharField(max_length = 200)
    status = models.BooleanField(default=True)
    created_at = models.DateField(default=1)
    update_at = models.DateField()
    delete_at = models.DateField()

class identification_type(models.Model) :
    type = models.CharField(max_length = 150)
    abrev = models.CharField(max_length = 4)
    created_at = models.DateField(default=1)
    update_at = models.DateField(default=1)
    delete_at = models.DateField(default=1)

class city(models.Model) :
    code = models.CharField(max_length = 10)
    name = models.CharField(max_length = 150)
    abrev = models.CharField(max_length = 4)
    id_country = models.IntegerField(max_length=10) 
    status = models.BooleanField(default=True)
    created_at = models.DateField(default=1)
    update_at = models.DateField(default=1)
    delete_at = models.DateField(default=1)

class country(models.Model) :
    code = models.CharField(max_length = 10)
    name = models.CharField(max_length = 150)
    abrev = models.CharField(max_length = 4)
    status = models.BooleanField(default=True)
    created_at = models.DateField(default=1)
    update_at = models.DateField(default=1)
    delete_at = models.DateField(default=1)

class pet(models.Model) :
    code = models.CharField(max_length = 10)
    name = models.CharField(max_length = 150)
    status = models.BooleanField(default=True)
    id_user = models.IntegerField(max_length=10) 
    id_type = models.IntegerField(max_length=10) 
    id_race = models.IntegerField(max_length=10) 
    created_at = models.DateField(default=1)
    update_at = models.DateField(default=1)
    delete_at = models.DateField(default=1)

class type(models.Model) :
    code = models.CharField(max_length = 10)
    abrev = models.CharField(max_length = 4)
    status = models.BooleanField(default=True)
    created_at = models.DateField(default=1)
    update_at = models.DateField(default=1)
    delete_at = models.DateField(default=1)

class race(models.Model) :
    code = models.CharField(max_length = 10)
    abrev = models.CharField(max_length = 4)
    status = models.BooleanField(default=True)
    created_at = models.DateField(default=1)
    update_at = models.DateField(default=1)
    delete_at = models.DateField(default=1)