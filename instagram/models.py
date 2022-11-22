from django.db import models


class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString

    def __str__(self):  # 객체를 출력할 때 리턴값 활용
        #return "Custom Post Object {}".format(self.id)
        return self.message

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = '메세지 글자수'

