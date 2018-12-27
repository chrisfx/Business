from django.shortcuts import render
from .forms import CustomerForm

# Create your views here.

def customerform(request):
 #if form is submitted
    if request.method == 'POST':
        form = CustomerForm(request.POST)
 #will handle the request later
    
 #   if form.is_valid():
 #if valid rendering new view with values
 #the form values contains in cleaned_data dictionary
        return render(request, 'result.html', {
        'first_name': form.cleaned_data['first_name'],
        'last_name': form.cleaned_data['last_name'],
        })    


 
    else:
        form = CustomerForm()
 
 #returning form 
    return render(request, 'customerform.html', {'form':form});

from CustomerData.models import Customer

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_customer = Customer.objects.count()

    context = {
        'num_customer': num_customer,
    }

# Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)



from django.views import generic

class CustomerListView(generic.ListView):
    model = Customer

