from django.contrib import admin
from .models import FKALL, CardUser, Education, Language, Work, Family


class EducationInline(admin.TabularInline):
    model = Education
    extra = 0


class LanguageInline(admin.TabularInline):
    model = Language
    extra = 0


class WorkInline(admin.TabularInline):
    model = Work
    extra = 0


class FamilyInline(admin.TabularInline):
    model = Family
    extra = 0


@admin.register(FKALL)
class FKALLAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'positions'
    list_filter = 'positions',
    list_editable = 'name', 'positions',


@admin.register(CardUser)
class CardUserAdmin(admin.ModelAdmin):
    inlines = EducationInline, LanguageInline, WorkInline, FamilyInline


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    pass


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    pass
