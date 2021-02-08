from django.contrib import admin
from .models import Agent, Category, Lead, User, UserProfile

# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Agent)
admin.site.register(Category)
admin.site.register(Lead)

