from django.contrib import admin

from api.models import *

@admin.register(Edition, Category, Requirement, AwardNomination, UserNomination, UserVote,)

class ApiAdmin(admin.ModelAdmin):
    pass