from django.db import models
from accounts.models import User


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

class FoodRecipes(models.Model):
    categoryCD = models.CharField(max_length=100, choices=CATEGORYCDS)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    tot_price = models.IntegerField()
    sumnail = models.ImageField()
    video = models.URLField()
    intro = models.CharField(max_length=255)
    time = models.DurationField()
    people_num = models.IntegerField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.categoryCD:
            raise ValueError("categoryCD is required.")
        
        self.sumnail.upload_to = f'sumnail/{self.categoryCD}/'

        super().save(*args, **kwargs)
