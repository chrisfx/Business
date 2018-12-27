from django import forms 
 
#creating our forms
class CustomerForm(forms.Form):
 #django gives a number of predefined fields
 #CharField and EmailField are only two of them
 #go through the official docs for more field details
 # name = forms.CharField(label='Enter your name', max_length=100)
 # email = forms.EmailField(label='Enter your email', max_length=100)

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    street_name = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    Zip = forms.CharField(max_length=10)
