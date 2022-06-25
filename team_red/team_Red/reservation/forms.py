from django import forms
from reservation.models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation  # 사용할 모델
        fields = ['end_date', 'num_people'] 