from django import forms

from .models import Reviews
from .models import ReviewsZoon

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
        widgets = {
            'title': forms.TextInput,
        }
