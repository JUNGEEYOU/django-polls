import datetime
from django.db import models
from django.utils import timezone
"""
 모델 만들기 
 - 장고에서 모델은 데이터베이스 구조도로 어떤 테이블을 만들고, 어떤 컬럼을 갖게할지 결정합니다. 
  설문조사(Question 테이블)과 설문조사 선택지(Choice 테이블)을 생성합니다. 
  models.Model을 상속 받습니다. 이는 부모 클래스가 실제로 데이터베이스와 ORM을 이용해 동작하는 기능을 가집니다. 
"""

class Question(models.Model):
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes= models.IntegerField(default=0)
