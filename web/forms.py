from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User
from base.models import Users as baseModel, Feedback
'''
form that uses built in user creation form
'''
class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'First Name'}))

    last_name = forms.CharField(max_length=50, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'Last Name'}))

    username = forms.EmailField(max_length=50, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'Email'}))
                                                               
    password1 = forms.CharField(max_length=50, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=50, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'Confirm Password'}))


    """
    Password validation is already validated by the UserCreationForm class in the built in form
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(email=username).exists():
            raise forms.ValidationError("Email already exists")
        return username
    
'''
Basic model form that uses the Users model, extended from auth Model
'''
class UserProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=50, required=True,
                                      widget=forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'Phone Number'}))
    class Meta:
        model = baseModel
        fields = ('phone_number',)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if baseModel.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Phone number already exists")
        return phone_number

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True,
                            
                                      widget=forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'Name'}))
    email = forms.EmailField(max_length=50, required=True,
                                      widget=forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'Email'}))
    message = forms.CharField(max_length=500, required=True,
                                      widget=forms.Textarea(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'Message'}))
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'message')
    
    def clean_subject(self):
        name = self.cleaned_data['subject']
        return name
    
    def clean_message(self):
        message = self.cleaned_data['message']
        return message
