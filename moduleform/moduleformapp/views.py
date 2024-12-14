from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm

# Create your views here.
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to success page after form is saved
        else:
            return HttpResponse("There was an error with the form submission.")  # Return error message if form is invalid
    else:
        form = EmployeeForm()  # Create an empty form for GET request
        return render(request, 'employee_form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')  # Render success page after successful form submission
