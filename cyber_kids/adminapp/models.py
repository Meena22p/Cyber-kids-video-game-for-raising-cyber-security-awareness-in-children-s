from django.db import models

# Create your models here.

class AddGameModel(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_title = models.CharField(max_length=300,null=True)
    game_type = models.CharField(max_length=500)
    game_platform = models.CharField(max_length=500)
    game_image = models.ImageField(upload_to='images/',null=True)
    game_url = models.URLField(max_length=500)

    class Meta:
        db_table = "Game_details"

class AddQuestions(models.Model):
    q_id = models.AutoField(primary_key=True)
    game = models.ForeignKey(AddGameModel,on_delete=models.CASCADE ,null=True)
    questions = models.CharField(max_length=1000,null=True)
    option1 = models.CharField(max_length=100,null=True)
    option2 = models.CharField(max_length=100,null=True)
    option3 = models.CharField(max_length=100,null=True)
    option4 = models.CharField(max_length=100,null=True)
    answer = models.CharField(max_length=100,null=True)


    class Meta:
        db_table = "Game_questions"

class Answers(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(AddQuestions,on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000,null=True)

    class Meta:
        db_table = 'Quiz_Answers'

