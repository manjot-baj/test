from django.db import models

# Create your models here.
class Details(models.Model):
    Name = models.CharField(max_length = 20)
    Add = models.CharField(max_length = 20)
    MobileNo = models.IntegerField()
    EmailId = models.CharField(max_length = 20)

    def __str__(self):
        return "Name : {0} | Address : {1} | MobileNo : {2} |  EmailId : {3}  ".format(self.Name,self.Add,self.MobileNo,self.EmailId)

