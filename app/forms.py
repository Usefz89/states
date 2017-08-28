from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



from app.models import *
from crispy_forms.helper import FormHelper

from django import forms
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User


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





# class UserSignUp(forms.ModelForm):
#     class Meta:
#
#         model = User
#         fields = ['username', 'password']
#
#         widgets = {'password': forms.PasswordInput()}






class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())





# class UserCreationForm(forms.ModelForm):
#     """
#     A form that creates a user, with no privileges, from the given username and
#     password.
#     """
#     error_messages = {
#         'duplicate_username': _("A user with that username already exists."),
#         'password_mismatch': _("The two password fields didn't match."),
#     }
#     username = forms.RegexField(label=_("Username"), max_length=30,
#         regex=r'^[\w.@+-]+$',
#         help_text=_("Required. 30 characters or fewer. Letters, digits and "
#                       "@/./+/-/_ only."),
#         error_messages={
#             'invalid': _("This value may contain only letters, numbers and "
#                          "@/./+/-/_ characters.")})
#     password1 = forms.CharField(label=_("Password"),
#         widget=forms.PasswordInput)
#     password2 = forms.CharField(label=_("Password confirmation"),
#         widget=forms.PasswordInput,
#         help_text=_("Enter the same password as above, for verification."))
#
#     class Meta:
#         model = User
#         fields = ("username",)
#
#     def clean_username(self):
#         # Since User.username is unique, this check is redundant,
#         # but it sets a nicer error message than the ORM. See #13147.
#         username = self.cleaned_data["username"]
#         try:
#             User._default_manager.get(username=username)
#         except User.DoesNotExist:
#             return username
#         raise forms.ValidationError(self.error_messages['duplicate_username'])
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError(
#                 self.error_messages['password_mismatch'])
#         return password2
#
#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user

class User_signup(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(User_signup, self).__init__(*args, **kwargs)



