from django.contrib import admin
from .models import BlogArticles


class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')       # 列表上显示内容
    list_filter = ('publish', 'author')                 # 过滤器
    search_fields = ('title', 'body')                   # 搜索框
    raw_id_fields = ('author',)                         # 显示外键详细信息
    date_hierarchy = 'publish'                          # 列表显示日期模块
    ordering = ['publish', 'author']                    # 排序


admin.site.register(BlogArticles, BlogArticleAdmin)
