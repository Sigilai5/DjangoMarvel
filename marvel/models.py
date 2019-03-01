from django.db import models

# Create your models here.

class Category(models.Model):
    CATEGORIES =(("Iron Man","Iron Man"),("Captain America","Captain America"),("Thor","Thor"))

    user_category = models.CharField(max_length=40,choices=CATEGORIES,)

    def __str__(self):
        return self.user_category

class Image(models.Model):
    post_image = models.ImageField(upload_to='post/', default='Image')
    image_caption = models.CharField(max_length=30, null=True)
    category = models.ForeignKey(Category, null=True, blank=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.image_caption