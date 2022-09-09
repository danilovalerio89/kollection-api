from rest_framework import generics

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import Request, Response, status
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from institutions.models import Institution
from .permissions import AdminPermissions, DetailsUserPermissions

from .serializers import SerializerUsers, UserAdminUpdateSerializer, SerializerGetUsers
from .models import User

from utils.mixins import UsersSerializersMixin


class UsersViews(UsersSerializersMixin, generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_map = {
        "GET": SerializerGetUsers,
        "POST": SerializerUsers,
    }

    def perform_create(self, serializer):
        serializer.save(institution_id=self.request.data["institution"])


class LoginView(ObtainAuthToken):
    def post(self, request: Request) -> Response:
        login = self.serializer_class(data=request.data, context={"request": request})

        if not login.is_valid():
            return Response(
                {"details": "Wrong password or username"}, status.HTTP_400_BAD_REQUEST
            )

        user = login.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key})


class UserDetailsView(generics.RetrieveUpdateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, DetailsUserPermissions]

    queryset = User.objects.all()
    serializer_class = SerializerUsers

    lookup_url_kwarg = "user_id"

    def perform_update(self, serializer):
        serializer.save(institution_id=self.request.data["institution"])


class AdminDetailsView(generics.UpdateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, AdminPermissions]

    queryset = User.objects.all()
    serializer_class = UserAdminUpdateSerializer

    lookup_url_kwarg = "user_id"

    def perform_update(self, serializer):
        serializer.save(institution_id=self.request.data["institution"])
