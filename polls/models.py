import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model): # models.Model을 상속받아서 Question 테이블 생성
    question_text = models.CharField(max_length=200) #id는 Primary Key여서 자동으로 적용되므로 안적어줘도 됨
    pub_date = models.DateTimeField('date published')

    def __str__(self): #관리자 페이지에서 question 테이블에 질문이 추가될때마다  pub에 데이터가 들어가게 되고 그 데이터를 가져와서 출력하게 될 때도 있는데 그때 해당 함수 호출
        return self.question_text #질문 바로 보여주도록 구현

    def was_published_recently(self): #등록한 질문들이 하루 지났는지 체크
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model): #id는 Primary Key여서 자동으로 적용되므로 안적어줘도 됨
    question = models.ForeignKey(Question, on_delete = models.CASCADE) # 삭제되었을 때 어떻게 진행 해줄건지 작성
    choice_text = models.CharField(max_length=200) #choice_text는 Charater로 받는데 최대 길이 200자로 제한
    votes = models.IntegerField(default = 0) #votes는 Integer로 받음

    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.booleadn = True
    was_published_recently.short_description = 'Published recently?'