from django import forms
from app.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div
from crispy_forms.bootstrap import FormActions





#class CitySearchForm(forms.Form):
 #   name = forms.CharField(required=True, initial="Orem")
  #  state = forms.CharField(required=True, initial="Utah")

class CreateCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'




class CitySearchForm(forms.Form):
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)


    def __init__(self, *args, **kwargs):
        super(CitySearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
    #     self.helper.form_action = '/city_search/'
    #     self.helper.help_text_inline = True
    #     self.helper.error_text_inline = True
    #     self.helper.html5_required = True
    #     self.helper.layout = Layout(
    #             Div('city', 'state',
    #                 FormActions(
    #                     Submit('submit', 'search', css_class="btn-success")
    #                     ),
    #                 ), #css_class='col-md-6'
    #             Div('message', css_class='col-md-6')
        #        )


class DeleteCityForm(forms.ModelForm):
    class Meta:

        model = City
        fields = ['name']








