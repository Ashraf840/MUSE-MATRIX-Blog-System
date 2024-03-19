from django.db import models
from django.urls import reverse
from account.models import User


class Tag(models.Model):
    title=models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})   # the "_detail" is a name pattern defined inside the url associating to a post-tag-detail.


class Category(models.Model):
    title=models.CharField(max_length=100)
    metaTitle=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})   # the "_detail" is a name pattern defined inside the url associating to a post-category-detail.


POST_STATUS_CHOICES = [
    ("DRAFT", "Draft"),
    ("PUBLISHED", "Published"),
    ("ARCHIVED", "Archived"),
]

class Post(models.Model):
    title=models.CharField(max_length=255)
    metaTitle=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255, unique=True)
    summary=models.TextField()
    status=models.CharField(max_length=9, choices=POST_STATUS_CHOICES, default="PUBLISHED")
    # isPublished=models.BooleanField(default=False)
    feature_image = models.ImageField(upload_to='blog/', verbose_name='Add Feature Image', blank=True, null=True)
    published_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    tag=models.ManyToManyField(Tag)
    category=models.ManyToManyField(Category)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    def __str__(self):
        return self.title


class PostMeta(models.Model):
    key=models.CharField(max_length=30)
    content=models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="meta")

    class Meta:
        verbose_name = "Post Meta"
        verbose_name_plural = "Post Meta"


class Comments(models.Model):
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    isPublished=models.BooleanField(default=False)
    published_at=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class TrendingPost(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="trendingPost")
    created_at=models.DateTimeField(auto_now_add=True)


class LatestPost(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="latestPost")
    created_at=models.DateTimeField(auto_now_add=True)


class MostPopularPost(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="mostPopularPost")
    created_at=models.DateTimeField(auto_now_add=True)


class RelatedPost(models.Model):
    post=models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name="originalPost")
    relatedPost=models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name="relatedPost")
    created_at=models.DateTimeField(auto_now_add=True)
