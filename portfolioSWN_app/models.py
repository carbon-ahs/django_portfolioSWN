from django.db import models
'''
class newTableName(models.Model):
    clmn_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.clmn_name
'''

class contractContent(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()

    comment = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name + ' | ' + self.email
