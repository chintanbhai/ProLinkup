from django import forms
from .models import profile 

class UserProfileForm(forms.ModelForm):
    
    # dynamic_language = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Language'}))
        
    class Meta:
        model = profile
        fields = ['image', 'contact', 'city','education','about'] 
        widgets = {
            'education': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'about': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
        }