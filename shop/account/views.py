from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout, get_user_model
from account.forms import RegisterForm, ContactFrom
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from account.tasks import contact_us


User = get_user_model()


class RegisterFormView(generic.FormView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy("book:book_list")

    def form_valid(self, form):
        user = form.save()
        user = authenticate(username=user.username, password=form.cleaned_data.get("password1"))
        login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("book:book_list")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="account/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("book:book_list")


class UpdateProfile(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'account/update_profile.html'
    success_url = reverse_lazy('account:profile')
    success_message = 'Profile updated'

    def get_object(self, queryset=None):
        user = self.request.user
        return user


class UserProfile(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'account/profile.html'

    def get_object(self, queryset=None):
        return self.request.user


class PublicProfile(generic.DetailView):
    model = User
    template_name = 'account/public_profile.html'

    def get_object(self, queryset=None):
        user = User.objects.get(pk=self.kwargs['pk'])
        return user


def contact_form(request):
    data = dict()
    if request.method == "POST":
        form = ContactFrom(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            contact_us.delay(subject, message, email)
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = ContactFrom()
    data['html_form'] = render_to_string('account/contact.html', {'form': form}, request=request)
    return JsonResponse(data)
