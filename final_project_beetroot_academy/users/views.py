from django.shortcuts import render, redirect
from .forms import RegistrationUserForm, ChangeProfileDataForm, ChangeUserDataForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def registration(request):
    if request.method == "POST":
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f"Account was successfully created! ")
            return redirect("start-page")
        else:
            messages.error(request,'Your form is invalid')
            context = {"form": form}
            return render(request, 'users/registration.html', context)

    context = {"form" : RegistrationUserForm() }
    return render(request,'users/registration.html',context)

@login_required
def profile(request):

    if request.method == 'POST':

        user_form = ChangeUserDataForm(request.POST,instance=request.user)
        prof_form = ChangeProfileDataForm(request.POST,request.FILES,instance=request.user.profile)

        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            messages.success(request,f'You profile was successfully updated!')
            return redirect('blog-profile')


    else:
        user_form = ChangeUserDataForm(instance=request.user)
        prof_form = ChangeProfileDataForm(instance=request.user.profile)

        return render(request, 'users/profile.html', {'user_form':user_form, 'prof_form':prof_form})
