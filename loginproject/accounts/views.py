
from django.shortcuts import render
from .forms import LoginForm

def login_view(request):
    message = ""

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            message = "Login validation successful!"
    else:
        form = LoginForm()

    return render(
        request,
        "accounts/login.html",
        {"form": form, "message": message}
    )
