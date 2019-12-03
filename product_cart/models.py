from django.db import models

# Create your models here.

PLAN_CHOICES = (
    
)

class SubPlan(models.Model):
    name = models.CharField(max_length=50,
        choices = [
            ("Basic", "Basic"),
            ("Standard", "Standard"),
            ("Premium", "Premium"),
            ],
        default="Basic"
        )
    price = models.IntegerField(
        choices = [
            (200, 'Basic ($200)'),
            (260, 'Standard ($260)'),
            (500, 'Premium ($500)'),
            ],
        default=200
        )
        
    def __str__(self):
        return self.name + " " + str(self.id)
    

class CartItem(models.Model):
    
    plan = models.ForeignKey('SubPlan', on_delete=models.CASCADE)
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    month = models.IntegerField(blank=False, default=0)
    
    def __str__(self):
        return self.plan.name + " x " + str(self.month)