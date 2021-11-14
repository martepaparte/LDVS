from django import forms

from django.core.exceptions import ValidationError

from .models import Order


class CreateOrderForm:
    class Meta:
        model = Order
        fields = ['place', 'order_date', 'emp_count', 'emp_qualification', 'order_task', 'task_duration_hours']


class AdminOrderForm:
    class Meta:
        model = Order
        fields = ['status', 'order_comments', 'order_emp']


class ConfirmOrderForm:
    class Meta:
        model = Order
        fields = ['order_confirm']


class OrderPaymentForm:
    class Meta:
        model = Order
        fields = ['order_payment', 'payment_confirm']