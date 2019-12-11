from django.db import models


# Create your models here.
class ShortlistedMaid(models.Model):
    maid = models.ForeignKey('agency.Maid', on_delete=models.CASCADE)
    owner = models.ForeignKey('accounts.Employer', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.maid.name + " " + str(self.owner)
