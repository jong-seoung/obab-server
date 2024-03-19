from django.db import models
from accounts.models import User
from core.models import TimeStampedModel


CATEGORYCDS = [
    ('food_recipe', '음식 레시피'),
    ('menu_recommendation', '메뉴 추천'),
    ('convenience_store_combination', '편의점 꿀 조합'),
    ('seasoning_recipe', '양념 레시피'),
    ('cooking_tip', '요리 TIP'),
]

DIFFICULTY_CHOICES = [
        ('easy', '쉬움'),
        ('medium', '보통'),
        ('hard', '어려움'),
]

class FoodRecipes(TimeStampedModel, models.Model):
    categoryCD = models.CharField(max_length=100, choices=CATEGORYCDS, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_foodrecipe_author', blank=True, null=True)
    title = models.CharField(max_length=255)
    tot_price = models.IntegerField(blank=True, null=True)
    thumnail = models.ImageField(blank=True, null=True, upload_to='thumnail/')
    content = models.TextField()
    video = models.URLField(blank=True, null=True)
    intro = models.CharField(max_length=255, blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    people_num = models.IntegerField(blank=True, null=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, blank=True, null=True)

    like = models.ManyToManyField(User, related_name='user_foodrecipe_like', blank=True)
    bookmark = models.ManyToManyField(User, related_name='user_foodrecipe_bookmark', blank=True)

    def __str__(self):
        return self.title


class Ingredients(models.Model):
    foodrecipe = models.ForeignKey(FoodRecipes, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    count = models.SmallIntegerField()
    unit = models.CharField(max_length=10)
    etc = models.CharField(max_length=255)


class RecipeProcess(models.Model):
    foodrecipe = models.ForeignKey(FoodRecipes, on_delete=models.CASCADE)
    content = models.TextField()

class ConvenienceItems(models.Model):
    foodrecipe = models.ForeignKey(FoodRecipes, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()