from django.contrib import admin
from Nathaniel.models import Chauffeur , Score , Post

# Register your models here.
admin.site.register(Chauffeur)
admin.site.register(Score)
admin.site.register(Post)

class Post(admin.ModelAdmin):
    readonly_fields = ('date',)
