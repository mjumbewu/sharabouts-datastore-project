from django import forms

class ActivityStreamForm (forms.Form):
    count = forms.IntegerField(required=False)
    before = forms.DateTimeField(required=False)
