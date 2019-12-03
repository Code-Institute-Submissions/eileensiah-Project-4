from django.db import models


# Create your models here.
class ShortlistedMaid(models.Model):
    maid = models.ForeignKey('agency.Maid', on_delete=models.CASCADE)
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    # quantity = models.IntegerField(blank=False, default=0)
    
    
    def __str__(self):
        return self.maid.name + " x " + str(self.quantity)
