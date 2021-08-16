from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, RedirectView
from apps.user.models import User
from apps.user.forms import FormUser,FormPersona
# Create your views here.



class SolicitudCreate(CreateView):
    model = User
    form_class = FormUser
    second_form_class = FormPersona

    template_name = 'login/registro.html'
    success_url = reverse_lazy('index')


    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        # recoger la informacion de los formularios

        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        # evaluar si son valores son validos para guardarlos
        if form.is_valid() and form2.is_valid():
            pwd = form.cleaned_data['password']
            registro = form.save(commit=False)  # no guardar hasta que guardemos los datos del seguando form

            # encryptar password
            if registro.pk is None:
                registro.set_password(pwd)
            else:
                user = User.objects.get(pk=registro.pk)
                if user.password != pwd:
                    registro.set_password(pwd)

            registro.persona = form2.save()
            registro.save()
            for g in form.cleaned_data['groups']:
                registro.groups.add(g)    #guardar grupos

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class logout_view(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)

class login_view(FormView):
    form_class = AuthenticationForm
    template_name = 'login/login.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated: #verificar si un usuario se encuentra logueado
           return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['title'] = 'Iniciar Sesion'
        return context

def index(request):

    return render(request, 'login/index.html',)

