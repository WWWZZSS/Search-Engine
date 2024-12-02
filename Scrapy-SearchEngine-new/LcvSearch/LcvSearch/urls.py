from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView  # 引入TemplateView
from .views import SearchSuggest  # 搜索建议
from .views import SearchView   # 搜索功能


urlpatterns = [
    url(r'^admin/', admin.site.urls),  # 管理后台 URL 配置
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),  # 引入主页
    url(r'^suggest/$', SearchSuggest.as_view(), name="suggest"),      # 处理搜索建议
    url(r'^search/$', SearchView.as_view(), name="search"),    # 处理搜索功能
]


