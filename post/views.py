from django.shortcuts import render, HttpResponse
from django.views import View
from post.models import Post, RelatedPost

class postDetail(View):

    template_name = 'post/postDetail.html'

    def get(self, request, id, slug):
        post = Post.objects.get(id=id)
        relatedPost = RelatedPost.objects.filter(post=post)
        context = {
            'post': post,
            'relatedPost': relatedPost,
        }
        return render(request, self.template_name, context=context)
    
