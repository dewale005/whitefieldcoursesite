from django import forms
from django.contrib.auth import get_user_model

User = get_user_model();


class LoginForm(forms.Form):
    email_address = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-prepended', 
                'id': "email_2",
                'placeholder': "email@email.com",
                'label': "Email Address"
                }))
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "password"
            }
        )
    );


class RegisterForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField(
        label="Phone Number",
        widget=forms.TextInput(
            attrs={
                'placeholder': '08012345678'
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": 'password'
            }
        )
    )

    def clean(self):
        username = self.cleaned_data.get('email')
        qs = User.objects.filter(email=username); 
        if qs.exists():
            raise forms.ValidationError("Email already exist")

        phone = self.cleaned_data.get('phone_number')
        qs2 = User.objects.filter(phone_number=phone); 
        if qs2.exists():
            raise forms.ValidationError("Phone number already exist")

        return self.cleaned_data


class VerificationForm(forms.Form):
    one_time_password = forms.CharField(
        label="OTP Verification Code",
        max_length=6,
        widget=forms.TextInput(
            attrs={
                'placeholder': "e.g 123456"
                })
    )

