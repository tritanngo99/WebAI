from django.contrib import admin
from django.db.models import QuerySet

from .models import Contest, Exercise, Result, TestCase

# Register your models here.


admin.site.register(Result)

class ContestAdmin(admin.ModelAdmin):
    list_display = ('author','name')
    fieldsets = [
        (None,{'fields':['name','contest_type','start','length','participant']})
    ]
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('contest','name')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs


class TestCaseAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


admin.site.register(Contest,ContestAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(TestCase,TestCaseAdmin)