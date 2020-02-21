from django import forms
from second.models import User
from django.forms import ModelForm


# class Form_model(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     verify_email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)


#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         vmail = all_clean_data['verify_email']

#         if email != vmail:
#             raise forms.ValidationError("MAKE SURE EMAIL MATCH")


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        # fields = ['fName', 'lName', 'email', 'verify_email', 'text'] 
        fields ='__all__'

    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAIL MATCH")

User = UserForm(request.POST)
new_user = User.save()