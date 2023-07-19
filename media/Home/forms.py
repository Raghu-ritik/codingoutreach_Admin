from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import Contact
from django.core.validators import RegexValidator
from django  import forms

class Contactusfrom(forms.ModelForm):
    # email = forms.EmailField(required=True)
    # name = forms.CharField(max_length=5,required=True)    
    # # phone_regex = RegexValidator(regex = r'^\+?1?\d{10}$',message = "The format : '+9999999999' .Up to 14 digits allowd "   )
    # phone_regex = RegexValidator(regex = r'^\+?1?\d{10}$',message = "The format should be exactly be of 10 digits"   )
    # phone = forms.CharField(max_length=255,required=True,validators=[phone_regex])
    # query = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = [
            'email',
            'name',
            'contactno',
            'query',
        ] 