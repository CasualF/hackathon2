from rest_framework.views import APIView
from rest_framework import permissions, generics
from .serializers import RegisterSerializer, ContactSerializer, UserDetailSerializer, UserSerializer
from .send_email import send_activation_email
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

User = get_user_model()


class RegistrationView(APIView):
    permission_classes = permissions.AllowAny,

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            try:
                send_activation_email(user.email, 'http://127.0.0.1:8000/account/activate/?c='+str(user.activation_code))
            except:
                return Response({'message': 'Registered, but wasnt able to send activation code',
                                 'data': serializer.data}, status=201)

        return Response(serializer.data, status=201)


class ActivationView(APIView):
    def get(self, request):
        code = request.GET.get('c')
        user = get_object_or_404(User, activation_code=code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Successfully Activated your account', status=200)


class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)


class LogoutView(APIView):
    permission_classes = permissions.IsAuthenticated,

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response('You logged out', status=205)
        except:
            return Response('Smth went wrong', status=400)


class UserDetailView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    # lookup_field = 'username'

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            return permissions.IsAuthenticated(),
        return permissions.IsAdminUser(),

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def contacts(self, request, pk):
        user = request.user
        if request.method == 'GET':
            print(1111111111111111111111)
            contacts = user.my_contacts.all()
            serializer = ContactSerializer(instance=contacts, many=True)
            return Response(serializer.data, status=200)

        elif request.method == 'POST':
            if user.my_contacts.filter(contact2=request.data.get('contact2')).exists():
                return Response('You already have that person in your contacts', status=400)
            serializer = ContactSerializer(data=request.data, context={'contact1': user})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=201)
