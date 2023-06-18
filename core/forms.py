from typing import Any, Mapping, Optional, Type, Union
from django import forms
from django.forms.utils import ErrorList
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class loginForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # ganti index jadi nama url yang ada formnya
        self.helper.form_action = reverse_lazy("index")
        self.helper.form_method = "GET"


    username = forms.CharField()
    password = forms.CharField()
