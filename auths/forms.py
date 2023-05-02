from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# class registerForm(forms.Form):
#     fname = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'id': 'firstName'}))
#     lname = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'id': 'lastName'}))
#     email = forms.CharField(label='Email ID', max_length=50,
#                             widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailID'}))
#     password = forms.CharField(label='Password', max_length=50,
#                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'pwd'}))
#     url = forms.URLField(label='URL', max_length=50, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'id': 'URL'}))
#     contactno = forms.DecimalField(label='Contact Number', max_digits=10,
#                                    decimal_places=0,
#                                    widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'contactNo'}))

class RegisterForm(forms.Form):
    email = forms.CharField(label='Email ID', max_length=50,
                            widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailID'}))
    password = forms.CharField(label='Password', max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'pwd'}))
    confirm_password = forms.CharField(label='Confirm Password', max_length=50,
                                       widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'cpd'}))
    url = forms.URLField(label='LinkedIn Url', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'linkedInUrl'}), required=False)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
