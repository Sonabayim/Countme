from django.shortcuts import render
# from django.http import HttpResponseRedirect
from django.views.generic import FormView
from .forms import UserLoginForm
# Create your views here.

# class UserLoginView(View):
# 	form = UserLoginForm()
# 	def get(self, request, *args, **kwargs):
# 		return render(request, 'login.html', {})

class UserLoginForm(FormView):
    template_name = 'login.html'
    form_class = UserLoginForm
    success_url = '/chart'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        # new_user = MyUser.objects.create(username=username, email=email)
        # new_user.set_password(password)
        # new_user.save()
        return super(UserLoginForm, self).form_valid(form)

# def user_login(request, *args, **kwargs):
# 	form = UserLoginForm(request.POST or None)
# 	if form.is_valid():
# 		return HttpResponseRedirect("/chart/")
# 	return render(request, "login.html", {"form":form })