from  .models import *
from django import forms


from  django_filters import DateFilter, CharFilter
import django_filters

class ArticleFilter(django_filters.FilterSet):
    title = CharFilter(field_name = "title", lookup_expr="icontains")
    class Meta():
        model = Article
        fields = ('title',)