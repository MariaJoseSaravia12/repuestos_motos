from django.shortcuts import render
from django.views.generic import View
from contacto.models import Consulta
from django.views.generic import FormView
from contacto.forms import ConsultaForm

class Contacto(FormView):
  template_name='contacto/contacto.html'
  form_class = ConsultaForm
  success_url = 'mensaje_enviado'

  def form_valid(self, form):
    form.save()
    form.send_email()
    return super().form_valid(form)

class MensajeEnviado(View):
  template_name='contacto/mensaje_enviado.html'

  def get(self, request):
    form = ConsultaForm()
    params={}
    params['form']= form
    return render(request, self.template_name, params)
