from django.contrib import admin
from .models import Post


# Register your models here.

# admin.site.register(Post)  # Register the Post model with the admin site | برای این که توی پنل ادمین جنگو نمایش داده بشه باید اینجا این رو اضافه کنیم


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')  # سرچ در چه جاهایی انجام شود
    prepopulated_fields = {'slug': ('title',)}  # با اضافه کردن این ایتم موقع ایجاد پست جدید به صورت خودکار اسلاگ با توجه به تایتل وارد شده ایجاد میشود
    raw_id_fields = ('author',)  # برای اینکه بتوانیم از این دیتا بیس استفاده کنیم باید از این کلاس استفاده کنیم
    date_hierarchy = 'publish'  # برای اینکه بتوانیم بر اساس تاریخ ایجاد کردن پست ها به صورت درختی به صورت زیر برسی کنیم
    ordering = ('status', 'publish')  # برای اینکه بتوانیم بر اساس چه جایی بر اساس چه جایی بر اساس چه جایی برسی کنیم
    list_editable = ('status',)  # قابلیت ادیت داخل لیست
    list_display_links = ('slug',)
