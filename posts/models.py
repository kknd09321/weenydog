from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):

    # author = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='posts', null=True)
    created_at = models.DateTimeField()
    liked_users = models.ManyToManyField(User, related_name='liked_posts')

    def __str__(self):
        if self.user:
            return f'{self.user.get_username()}: {self.body}'

        return f'{self.body}'

# null로 변경하면서 빈곳이 되었으니 있을때와 없을때를 따져야 하니까 if 로 해야하고 if else도 써도 되지만 리턴이 되서 빼도 됨

# null =false 로 바꾸면서 다시 makemigrations 하면 1) 널에다가 디폴트값을 줘 2) 넌 이미 해결을 했어
# author = models.CharField(max_length=100)
    # on_delete=models.CASCADE 해도 그만 안해도 그만이지만 ForeignKey 지워지면 다 같이 지워지고 캐스 케이드는 계단식으로 처리된다는뜻