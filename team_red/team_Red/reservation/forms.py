from django import forms
from reservation.models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation  # 사용할 모델
        fields = ['end_date', 'num_people', 'place'] 

        widgets = {
            'end_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  
                      }),
            'num_people': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }),
        }