from django.db import models

# Create your models here.


class Comment(models.Model):
    # 名字，邮箱，个人网站，用户发表的内容，评论时间
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post')
    # 一个评论只能属于一篇文章，一篇文章可以有多个评论

    def __str__(self):
        return self.text[:20]
