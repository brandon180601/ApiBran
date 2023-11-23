from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroForm
from .models import *
from django.core.mail import send_mail
from django.db.models import Count


# Create your views here.
# class Home(APIView):
#     items = ['Hola Mundo']
#     def get(self,request):
#         return Response(self.items)
    
#     def post(self, request):
#         data = request.data
#         if 'name' in data:
#             new_item = {'name': data['name']}
#             self.items.append(new_item)
#             return Response(new_item, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'error': 'Missing "name" field in the request data'}, status=status.HTTP_400_BAD_REQUEST)


class Home(APIView):
    template_name="login.html"
    def get(self,request):
        return render(request, self.template_name)
    
class IndexView(APIView):
    template_name = "index.html"
    def get(self,request):
        return render(request, self.template_name)
    
class colors(APIView):
    template_name = "colors.html"
    def get(self,request):
        return render(request, self.template_name)
    
class calendars(APIView):
    template_name = "calendars.html"
    def get(self,request):
        return render(request, self.template_name)
    
class icons(APIView):
    template_name = "icons.html"
    def get(self,request):
        return render(request, self.template_name)
    
class forms(APIView):
    template_name = "forms.html"
    def get(self,request):
        return render(request, self.template_name)
    
class alerts(APIView):
    template_name = "alerts.html"
    def get(self,request):
        return render(request, self.template_name)

class flex(APIView):
    template_name = "flex.html"
    def get(self,request):
        return render(request, self.template_name)

class footers(APIView):
    template_name = "footers.html"
    def get(self,request):
        return render(request, self.template_name)

class gettingStarted(APIView):
    template_name = "getting-started.html"
    def get(self,request):
        return render(request, self.template_name)

class list(APIView):
    template_name = "list.html"
    def get(self,request):
        return render(request, self.template_name)

class navs(APIView):
    template_name = "navs.html"
    def get(self,request):
        return render(request, self.template_name)

class navs(APIView):
    template_name = "navs.html"
    def get(self,request):
        return render(request, self.template_name)

class panels(APIView):
    template_name = "panels.html"
    def get(self,request):
        return render(request, self.template_name)

class timeline(APIView):
    template_name = "timeline.html"
    def get(self,request):
        return render(request, self.template_name)

class typography(APIView):
    template_name = "typography.html"
    def get(self,request):
        return render(request, self.template_name)

from django.contrib import messages
from django.core.mail import send_mail

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Envía un correo de confirmación o bienvenida al usuario
            subject = '¡Bienvenido a nuestra aplicación!'
            message = f'Gracias por registrarte en nuestra aplicación. Tu nombre de usuario es: {user.usuario} y tu contraseña es: {user.password}'
            from_email = 'brandon.silva.180@gmail.com'  # Reemplaza con tu dirección de correo electrónico
            recipient_list = [user.correo]  # Utiliza el campo "correo" del usuario registrado

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            # Agrega un mensaje de éxito para el usuario
            messages.success(request, '¡Registro exitoso! Se ha enviado un correo de bienvenida con tus credenciales.')

            # Redirige a la página de inicio de sesión u otra página que desees
            login(request, user)
            return redirect('iniciar_sesion')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})





def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']  # Asegúrate de que coincida con el campo del formulario
        password = request.POST['password']

        # Autenticar al usuario utilizando el modelo de usuario predeterminado (auth_user)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirigir al usuario a la página deseada después del inicio de sesión
            return redirect('index.html')
        else:
            error_message = "Usuario o contraseña incorrectos"
            return render(request, 'login.html', {'error_message': error_message})
    
    # Agrega un retorno para el caso en que el método no sea "POST"
    return render(request, 'login.html')

def dashboard(request):
    p1Labels=[]
    p1Values=[]
    p1 = Preguntas.objects.values('descripcion').annotate(total=Count('descripcion'))
    for p1D in p1:
        p1Labels.append(p1D['descripcion'])
        p1Values.append(p1D['total'])
    
    p2Labels = []
    p2Values = []
    p2 = Preguntas.objects.values('descripcion1').annotate(total=Count('descripcion1'))
    for p2D in p2:
        p2Labels.append(p2D['descripcion1'])
        p2Values.append(p2D['total'])
    
    p3Labels = []
    p3Values = []
    p3 = Preguntas.objects.values('descripcion2').annotate(total=Count('descripcion2'))
    for p3D in p3:
        p3Labels.append(p3D['descripcion2'])
        p3Values.append(p3D['total'])
    
    p4Labels = []
    p4Values = []
    p4 = Preguntas.objects.values('descripcion3').annotate(total=Count('descripcion3'))
    for p4D in p4:
        p4Labels.append(p4D['descripcion3'])
        p4Values.append(p4D['total'])
    
    p5Labels = []
    p5Values = []
    p5 = Preguntas.objects.values('descripcion4').annotate(total=Count('descripcion4'))
    for p5D in p5:
        p5Labels.append(p5D['descripcion4'])
        p5Values.append(p5D['total'])
    
    p6Labels=[]
    p6Values=[]
    p6 = Preguntas.objects.values('descripcion5').annotate(total=Count('descripcion5'))
    for p6D in p6:
        p6Labels.append(p6D['descripcion5'])
        p6Values.append(p6D['total'])
    
    p7Labels = []
    p7Values = []
    p7 = Preguntas.objects.values('descripcion6').annotate(total=Count('descripcion6'))
    for p7D in p7:
        p7Labels.append(p7D['descripcion6'])
        p7Values.append(p7D['total'])
    
    p8Labels = []
    p8Values = []
    p8 = Preguntas.objects.values('descripcion7').annotate(total=Count('descripcion7'))
    for p8D in p8:
        p8Labels.append(p8D['descripcion7'])
        p8Values.append(p8D['total'])
    
    p9Labels = []
    p9Values = []
    p9 = Preguntas.objects.values('descripcion8').annotate(total=Count('descripcion8'))
    for p9D in p9:
        p9Labels.append(p9D['descripcion8'])
        p9Values.append(p9D['total'])
    
    p10Labels = []
    p10Values = []
    p10 = Preguntas.objects.values('descripcion9').annotate(total=Count('descripcion9'))
    for p10D in p10:
        p10Labels.append(p10D['descripcion9'])
        p10Values.append(p10D['total'])
    
    p11Labels = []
    p11Values = []
    p11 = Preguntas.objects.values('descripcion10').annotate(total=Count('descripcion10'))
    for p11D in p11:
        p11Labels.append(p11D['descripcion10'])
        p11Values.append(p11D['total'])
        
    context = {
        'p1Label': p1Labels,
        'p1Value': p1Values,
        'p2Label': p2Labels,
        'p2Value': p2Values,
        'p3Label': p3Labels,
        'p3Value': p3Values,
        'p4Label': p4Labels,
        'p4Value': p4Values,
        'p5Label': p5Labels,
        'p5Value': p5Values,
        'p6Label': p6Labels,
        'p6Value': p6Values,
        'p7Label': p7Labels,
        'p7Value': p7Values,
        'p8Label': p8Labels,
        'p8Value': p8Values,
        'p9Label': p9Labels,
        'p9Value': p9Values,
        'p10Label': p10Labels,
        'p10Value': p10Values,
        'p11Label': p11Labels,
        'p11Value': p11Values
    }
    
    template_name = "footers.html"
    return render(request, template_name, context)


class persona1(APIView):
    template_name = "persona1.html"
    def get(self,request):
        return render(request, self.template_name)

class persona2(APIView):
    template_name = "persona2.html"
    def get(self,request):
        return render(request, self.template_name)

class persona3(APIView):
    template_name = "persona3.html"
    def get(self,request):
        return render(request, self.template_name)

class persona4(APIView):
    template_name = "persona4.html"
    def get(self,request):
        return render(request, self.template_name)