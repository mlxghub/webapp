from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserProfile(models.Model):
    SEX_CHOICES = {  #字典
        1: 'boy',
        2: 'girl',
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE) #当删除一对一绑定表的信息时时，另外一个表也会删除对应的信息删除。
    sex = models.SmallIntegerField(default=1, choices=SEX_CHOICES.items())
    age = models.SmallIntegerField(blank=True, null=True)
    sign = models.CharField(max_length=128, blank=True, null=True)
    acount = models.IntegerField(default=0, blank=True, null=True)
    icon = models.ImageField(upload_to="Image/", blank=True, null=True)
    book = models.CharField(max_length=128, blank=True, null=True)

    def __unicode__(self):
        return self.user.username

    class Meta:
        db_table = 'UserProfile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Novel(models.Model):
    TYPE_CHOICES = {  # 字典
        1: '玄幻',
        2: '武侠',
        3: '仙侠',
    }
    novel_id = models.IntegerField(primary_key=True)
    type =models.SmallIntegerField(default=1,choices=TYPE_CHOICES.items())
    novel_name = models.CharField(max_length=128)
    writer = models.CharField(max_length=128)
    create_time =models.DateTimeField()
    wordcount = models.IntegerField()
    updatatime =models.DateTimeField()
    price = models.IntegerField()