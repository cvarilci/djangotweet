from django.contrib import admin
from tweety_app.models import Tweet

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Message Group',{"fields":["message"]}),
        ('Nickname Group',{"fields":["nickname"]})
    ]
    #fields = ['message','nickname']

# Register your models here.
admin.site.register(Tweet,TweetAdmin)

