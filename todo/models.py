from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    Heading=models.CharField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.heading
    
    
class TodoTable(models.Model):
    heading=models.ForeignKey(Topic,related_name='points', on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    
    def __str__(self):
            return self.title
        
        
class WordMeaning(models.Model):
    heading=models.ForeignKey(Topic,related_name='meaning', on_delete=models.CASCADE, null=True, blank=True)
    word=models.TextField()
    meaning=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.word    
    

class Publisher(models.Model):
    name=models.CharField(max_length=250)
    join_date=models.DateField(default=now)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    popularity_score=models.IntegerField(default=0)
    join_data=models.DateField(default=now)
    followers = models.ManyToManyField(User, related_name="following_authors", blank=True)
    recommender = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL, related_name="recommended_authors"
    )
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Book(models.Model):
    title=models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish_date=models.DateField()
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL, related_name="books")
    publisher = models.ForeignKey(Publisher, null=True, blank=True, on_delete=models.SET_NULL, related_name="books")
    
    def __str__(self):
        return self.title