from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
       """用户学习的主题"""
       text = models.CharField(max_length=200)  # 文本字段，最大长度200字符
       date_added = models.DateTimeField(auto_now_add=True)  # 自动设置为当前日期和时间
       #owner = models.ForeignKey(User, on_delete=models.CASCADE)
       owner = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
       public = models.BooleanField(default=False)

       def __str__(self):
           """返回模型的字符串表示"""
           return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回一个表示条目的简单字符串"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"