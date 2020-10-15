from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Poll

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class PollForm(forms.ModelForm):
    
    class Meta:
        model = Poll
        fields = ["title"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-pollForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'create new poll'
        self.helper.add_input(Submit('cancel', 'Cancel', css_class="btn-secondary", formnovalidate='formnovalidate'))
        self.helper.add_input(Submit('submit', 'Create'))