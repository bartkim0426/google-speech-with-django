from django.forms import ModelForm
from django import forms
from ..models import Speech


class DateInput(forms.DateInput):
    input_type = 'date'


class SpeechForm(ModelForm):
    class Meta:
        model = Speech
        fields = ['file_name', 'title', 'lecture_date', 'memo']
        widgets = {
            'lecture_date': forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'mdl-textfield__input',
                    'type': 'date',
                    'placeholder': 'YYYY-MM-DD',
                }
            ),
            'memo': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(SpeechForm, self).__init__(*args, **kwargs)
        self.fields['file_name'].widget.attrs['class'] = "mdl-textfield__input"
        self.fields['title'].widget.attrs['class'] = "mdl-textfield__input"
        self.fields['memo'].widget.attrs['class'] = "mdl-textfield__input"
        # self.fields['lecture_date'].widget.attrs = {
        #     'class': 'mdl-textfield__input',
        #     'type': 'date',
        #     'placeholder': '',
        # }
        self.fields['lecture_date'].label = ""
#         for fname, f in self.fields.items():
#             f.label = ''

#         self.fields['title'].label = 
