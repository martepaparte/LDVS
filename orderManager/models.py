from django.db import models


class Order(models.Model):
    place = models.CharField(max_length=200, )
    order_date = models.DateTimeField()
    order_created = models.DateTimeField(auto_now_add=True)
    emp_count = models.IntegerField()
    emp_qualification = models.TextField()
    order_task = models.TextField()
    task_duration_hours = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=200)
    order_comments = models.JSONField()
    order_emp = models.JSONField()
    order_confirm = models.BooleanField()
    order_payment = models.FileField()
    payment_confirm = models.BooleanField()

