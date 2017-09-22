from django import forms

from ..models import Speech


class InputFileForm(forms.ModelForm):
    class Meta:
        model = Speech
        fields = ('docx_input',)

    def __init__(self, *args, **kwargs):
        super(InputFileForm, self).__init__(*args, **kwargs)
        self.fields['docx_input'].required = False
