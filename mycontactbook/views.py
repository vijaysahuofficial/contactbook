from django.shortcuts import render, redirect
from .forms import AddContactForm
from .models import AddContact
from django.contrib import messages


def home_view(request, *args, **kwargs):
    form = AddContactForm()
    added_data = AddContact.objects.all()
    if request.method == "POST":
        form = AddContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Contact Successfully Added')
            form = AddContactForm()
    else:
        form = AddContactForm()
    data = {
        'contacts': added_data,
        'form': form,
    }
    return render(request, 'home.html', data)





def updateContact(request, pk):
    if request.method == 'POST':
        form_data = AddContact.objects.get(pk=pk)
        form = AddContactForm(request.POST, instance=form_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully')
    else:
        form_data = AddContact.objects.get(pk=pk)
        form = AddContactForm(instance=form_data)
    return render(request, 'update.html', {'form': form})




def del_contact(request, pk):
    d = AddContact.objects.get(pk=pk)
    d.delete()
    return redirect('home')


def contacts_view(request, *args, **kwargs):
    contacts = AddContact.objects.all()
    return render(request, 'contacts.html', {'contacts': contacts})
