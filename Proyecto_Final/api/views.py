from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
from .models import Nota
import json
# Create your views here.

class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) 


    def get(self, request, id=0):
        if (id>0):
            usuarios = list(Usuario.objects.filter(id=id).values())
            if len(usuarios) > 0:
                usuario = usuarios[0]
                datos={'message': 'Success', 'usuario': usuario}
            else:
                datos = {'message': 'Usuario noy found ...'}
            return JsonResponse(datos)
        else:
            usuarios=list(Usuario.objects.values())
            if len(usuarios)>0:
                datos={'message':'Success', 'usuarios':usuarios}
            else:
                datos={'message': "Usuario not found ..."}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Usuario.objects.create(name=jd['name'], surname=jd['surname'])
        datos={'message':'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        usuarios = list(Usuario.objects.filter(id=id).values())
        if len(usuarios) > 0:
            usuario=Usuario.objects.get(id=id)
            usuario.name=jd['name']
            usuario.surname=jd['surname']
            usuario.save()
            datos={'message':'Success'}
        else:
            datos={'message': "Usuario not found ..."}
        return JsonResponse(datos)
        
    def delete(self, request, id=id):
        usuarios = list(Usuario.objects.filter(id=id).values())
        if len(usuarios) > 0:
            Usuario.objects.filter(id=id).delete()
            datos={'message':'Success'}
        else:
            datos={'message': "Usuario not found ..."}
        return JsonResponse(datos)    

class NotaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) 

    def get(self, request, id=0):
        if(id>0):
            notas=list(Nota.objects.filter(id=id).values())
            if len(notas) > 0:
                nota=notas[0]
                datos={'message':'Success', 'notas':nota}
            else:
                datos={'message':"Nota not found ..."}
            return JsonResponse(datos)
        else:
            nota=list(Nota.objects.values())
            if len(nota) > 0:
                datos={'message':'Success', 'notas':nota}
            else:
                datos={'message':"Nota not found ..."}
            return JsonResponse(datos)

    def post(self, request, id=id):
        jd=json.loads(request.body)
        Nota.objects.create(titulo=jd['titulo'],contenido=jd['contenido'],autor_id=jd['autor_id'])
        datos={'message':'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        notas=list(Nota.objects.filter(id=id).values())
        if len(notas) > 0:
            nota=Nota.objects.get(id=id)
            nota.titulo=jd['titulo']
            nota.contenido=jd['contenido']
            nota.autor_id=jd['autor_id']
            nota.save()
            datos={'message':'Success'}
            
        else:
            datos={'message':"Nota not found ..."}  
        return JsonResponse(datos)

    def delete(self, request,id):
        notas=list(Nota.objects.filter(id=id).values())
        if len(notas) > 0:
            Nota.objects.filter(id=id).delete()
            datos={'message':'Success'}
        else:
            datos={'message':"Nota not found ..."}  
        return JsonResponse(datos)