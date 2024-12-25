from django.db import models

# Create your models here.
# notes/models.py
from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=200)  # 主题标题
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # 主题所有者
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间

    def __str__(self):
        return self.title

class Entry(models.Model):
    topic = models.ForeignKey(Topic, related_name='entries', on_delete=models.CASCADE)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # 假设ID为1的用户是默认所有者
    created_at = models.DateTimeField(auto_now_add=True)