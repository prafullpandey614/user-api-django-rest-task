from django.db import models

# Create your models here.
# class Friend(models.Model):
#     from_user = models.CharField(max_length=10)
#     to_user = models.CharField(max_length=10)
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    friends = models.ManyToManyField("User", through="Friendship" )
    
    def __str__(self):
        return f"{self.username}"
class FriendShip(models.Model):
    user_one = models.ForeignKey(User, on_delete=models.CASCADE , related_name='+')
    user_two = models.ForeignKey(User, on_delete=models.CASCADE ,  related_name='+')
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta :
        unique_together = [['user_one', 'user_two']]
    def __str__(self):
        return f"{self.user_one}      {self.user_two}"
