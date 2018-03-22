"""
model->序列化—>在settings中配置'rest_framework','app'->迁移数据库->编写视图函数views->编写url
jwt api—auth生成token，相对于session的cookies。带token去请求主页面，就可以解析出来
"""

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=20)
