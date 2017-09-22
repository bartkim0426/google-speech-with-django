from django import forms
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from ..models import WeatherLocation


class WeatherSelect(forms.widgets.Select):
    def render_option(self, selected_choices, option_value, option_label):
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''
        # get class attrs (customize class_attr by yourself)
        class_attr = 'mdl-menu__item'
        return format_html('<option value="{0}"{1} class="{3}">{2}</option>',
                           option_value,
                           selected_html,
                           force_text(option_label),
                           class_attr)


# class WeatherModelChoiceField(forms.ModelChoiceField):
#     def __init__(self, *args, **kwargs):
#         kwargs['widget'] = WeatherSelect
#         super(WeatherModelChoiceField, self).__init__(*args, **kwargs)


class WeatherForm(forms.Form):
    location = forms.ModelChoiceField(
        queryset=WeatherLocation.objects.active(),
        initial={'location': '고려대학교'},
        widget=WeatherSelect(
            attrs={
                'onChange': 'submit()',
                'class': 'mdl-textfield__input',
            },
        ),
    )
