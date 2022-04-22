from ssl import OP_NO_TLSv1_1
from django.db import models


class Quesions(models.Model):
    question = models.CharField(max_length=200)
    op1 = models.CharField(max_length=200)
    op2 = models.CharField(max_length=200)
    op3 = models.CharField(max_length=200)
    op4 = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question
    
