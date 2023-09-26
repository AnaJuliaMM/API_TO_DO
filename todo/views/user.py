from rest_framework import views
from ..serializers.user import UserSerializer
from ..models.user import UserEntity
from rest_framework.response import Response
from rest_framework import status


class UserView(views.APIView):
    """
    List all categories, or create a new USER.
    """
    def get(self, request, format=None):
        #Busca todos os objeto dos banco
        categories = UserEntity.objects.all()
        #Serializa os objetos trazidos
        serializer = UserSerializer(categories, many=True)
        #Gera uma resposta com eles
        return Response(serializer.data)

    def post(self, request, format=None):

        #Serializar o dado mandando na requisição
        serializer = UserSerializer(data=request.data)
        #Verificar se está válido nos termos da classe seriializer de usuário
        if (serializer.is_valid()):
            #Se válido, salva
            serializer.save()
            #Retorna o objeto criado e um código 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #Caso não seja válido, retorna o erro detectado pelo serializador
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)