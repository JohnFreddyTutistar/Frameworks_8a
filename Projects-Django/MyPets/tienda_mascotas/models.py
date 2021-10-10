from django.db import models
from django.db.models.expressions import CombinedExpression

class user(models.Model) :
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    id_identification_type = models.IntegerField()
    number_id = models.CharField(max_length = 15)
    id_city = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    password = models.CharField(max_length = 200)
    status = models.BooleanField(default=True)
    created_at = models.DateField()
    update_at = models.DateField()
    delete_at = models.DateField()
