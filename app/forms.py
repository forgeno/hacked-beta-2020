from django import forms

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class ExampleForm(forms.Form):
    my_date_field = forms.DateField(widget=DateInput)


class ExampleModelForm(forms.Form):
    class Meta:
        widgets = {'date_field' : DateInput()}
