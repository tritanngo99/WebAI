from django import forms


class UploadDataTrain(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()


