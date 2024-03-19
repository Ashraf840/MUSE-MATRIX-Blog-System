from django.contrib import admin
from .models import *

class RelatedPostAdmin(admin.ModelAdmin):
    list_display = ['post', 'relatedPost']

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostMeta)
admin.site.register(Comments)
admin.site.register(TrendingPost)
admin.site.register(LatestPost)
admin.site.register(MostPopularPost)
admin.site.register(RelatedPost, RelatedPostAdmin)
