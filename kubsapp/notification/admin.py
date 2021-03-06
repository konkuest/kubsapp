# -*- coding: utf-8 -*-
from django.contrib import admin
import site

from .models import Student, Notice, Push

# Register your models here.

admin.site.register(Student)
admin.site.register(Notice)
admin.site.register(Push)

class StudentAdmin(admin.ModelAdmin):
    #Filtering by studentid
    list_filter = ('studentid',)

    #Search by studentid and username
    search_fields = ('studentid', 'username',)


class NoticeAdmin(admin.ModelAdmin):
    list_filter = ('title', 'day',)
    search_fields = ('number', 'day',)
    ordering = ('-number',)


class PushAdmin(admin.ModelAdmin):
    list_filter = ('push_title', 'push_author')