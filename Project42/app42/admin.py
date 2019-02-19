from django.contrib import admin
from .models import Publication
from .models import Article

admin.site.register(Publication)
admin.site.register(Article)