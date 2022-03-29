from django.contrib import admin

from .forms import ReviewsForm
from .models import Reviews
from .models import ReviewsZoon
from .models import ReviewsYoll

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'review', 'date')
    form = ReviewsForm

@admin.register(ReviewsZoon)
class ReviewsZoonAdmin(admin.ModelAdmin):
    list_display = ('name1', 'review1', 'date1')
    form = ReviewsForm

@admin.register(ReviewsYoll)
class ReviewsYollAdmin(admin.ModelAdmin):
    list_display = ('name2', 'review2', 'date2', 'rating2')
    form = ReviewsForm