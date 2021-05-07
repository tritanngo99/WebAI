from django import forms
from contests.models import Contest

class ContestForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={'col':20}))
    time = forms.DateField()
    class Meta:
        model = Contest
        fields = '__all__'