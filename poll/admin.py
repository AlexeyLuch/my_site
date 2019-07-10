from django.contrib import admin

from .models import Question,Phonebase,Tank,Article,Comments,Unique_set

admin.site.register(Question)
admin.site.register(Phonebase)
admin.site.register(Tank)
admin.site.register(Unique_set)

class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title','article_text','article_date']
    inlines = [ArticleInline]
    list_filter = ['article_date']
    list_display = ['article_text']


admin.site.register(Article,ArticleAdmin)
admin.site.register(Comments)


# class FlatPageAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (None, {
#             'fields': ('url', 'title', 'content', 'sites')
#         }),
#         ('Advanced options', {
#             'classes': ('collapse',),
#             'fields': ('registration_required', 'template_name'),
#         }),
#     )