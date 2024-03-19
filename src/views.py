from django.shortcuts import render, HttpResponse
from django.views import View
from post.models import Post, TrendingPost, LatestPost, MostPopularPost, Category


class homePage(View):

    template_name = 'src/homePage.html'
    
    def get(self, request):
        posts = Post.objects.all()
        trendingPosts = TrendingPost.objects.all()
        latestPosts = LatestPost.objects.all()
        mostPopularPosts = MostPopularPost.objects.all()
        b_category = Category.objects.get(title='Business')
        t_category = Category.objects.get(title='Travel')
        businessPosts = Post.objects.filter(category=b_category)
        travelPosts = Post.objects.filter(category=t_category)
        context = {
            'posts': posts,
            'trendingPosts': trendingPosts,
            'latestPosts': latestPosts,
            'mostPopularPosts': mostPopularPosts,
            'businessPosts': businessPosts,
            'travelPosts': travelPosts,
        }
        return render(request, self.template_name, context=context)
