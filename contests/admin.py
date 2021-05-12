from django.contrib import admin
from .models import Contest, Exercise, Result, TestCase, Rank

# Register your models here.
admin.site.register(Contest)
admin.site.register(Exercise)
admin.site.register(TestCase)
admin.site.register(Result)
admin.site.register(Rank)
