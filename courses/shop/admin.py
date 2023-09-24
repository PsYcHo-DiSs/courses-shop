from django.contrib import admin
from .models import Course, Category  # рефакторинг

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcome to the Courses admin area"


class CourseAdmin(admin.ModelAdmin):
    # Атрибуту передаётся кортеж из значений
    list_display = ('title', 'price', 'category')


class CoursesInline(admin.TabularInline):
    model = Course
    exclude = ['created_at']  # Данным атрибутом скрываем поле создания
    extra = 1  # отвечает за количество пустых рядов, доступных для добавления нового курса


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        # Здесь описываем какие поля будут отображаться на странице редактирования категории
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]
    inlines = [CoursesInline]  # Таким образом, связываем курсы с категорией


# Регистрируем вновь созданные классы
# благодаря изменению импорта можно упростить обращение
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
