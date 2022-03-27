from django.contrib import admin

from .forms import ReviewsForm
from .models import Reviews
from .models import ReviewsZoon

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'review', 'date')
    form = ReviewsForm

@admin.register(ReviewsZoon)
class ReviewsZoonAdmin(admin.ModelAdmin):
    list_display = ('name1', 'review1', 'date1')
    form = ReviewsForm
