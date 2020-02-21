from django import forms
# from django.core import validators
from AppTwo.models import User


class NewUser(forms.ModelForm):
    
    class Meta():
        model = User     
        fields = '__all__'

        

# class UserForm(forms.Form):
#     name = forms.CharField(max_length=264, required=False)
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label='Enter your email again:')
#     text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False,
    #                             widget=forms.HiddenInput,
    #                             validators = [validators.MaxLengthValidator(0)])

    # def clean(self):
    #     all_clean_data = super().clean()
    #     email = all_clean_data['email']
    #     vmail = all_clean_data['verify_email']

    #     if email != vmail:
    #         raise forms.ValidationError("MAKE SURE EMAIL MATCH")

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data["botcatcher"]
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher
        