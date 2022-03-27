from django import forms

from .models import Reviews
from .models import ReviewsZoon
from .models import ReviewsYoll

class ReviewsForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = (
            'name',
            'review',
            'date',
        )
        model = ReviewsZoon
        fields = (
             'name1',
             'review1',
             'date1',
        )
        model = ReviewsYoll
        fields = (
             'name2',
             'review2',
             'date2',
        )
        widgets = {
            'title': forms.TextInput,
        }
