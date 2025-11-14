from django.db import models

# Create your models here.

class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_join_date = models.DateField(auto_now_add=True)
    user_name = models.CharField(max_length=100)
    user_age = models.CharField(max_length=10)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=100)
    user_prifile = models.ImageField(upload_to="user_images/",null=True)
    status = models.CharField(max_length=20,default="Pending")

    class Meta:
            db_table = "user_details"

class FeedbackModel(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedback = models.TextField()
    date = models.DateField(auto_now_add=True,null=True)
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True)
    sentiment = models.CharField(max_length=100,null=True)

    class Meta:
        db_table = "user_feedback"

class Analysis(models.Model):
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)

    class Meta:
        db_table = 'result_analysis'