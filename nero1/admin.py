from django.contrib import admin

from .forms import ReviewsForm
from .models import Reviews

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'review', 'date')
    form = ReviewsForm
