from django.shortcuts import render
from django.shortcuts import redirect
from usuarios.forms import CreateUserForm



def pagina_registro(request):
    params={}
    form=CreateUserForm()
    params["form"]=form

    if request.method =="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, "usuarios/registro.html", params)


