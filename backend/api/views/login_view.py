# from django.middleware import csrf
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from api.util import set_access_cookies, set_refresh_cookies, get_tokens_for_user, combine_role_permissions
# from api.serializers import UserSerializer, LoginSerializer


# class LoginView(APIView):

#     authentication_classes = ()
#     permission_classes = (AllowAny, )

#     def post(self, request):
#         serializer = LoginSerializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']

#         response = Response()

#         token = get_tokens_for_user(user)
#         set_access_cookies(response, token['access'])
#         set_refresh_cookies(response, token['refresh'])
#         csrf.get_token(request)

#         data = UserSerializer(user, context={'request': request}).data
#         data['permissions'] = combine_role_permissions(user.role)

#         response.status_code = status.HTTP_200_OK
#         response.data = {"msg": "Login successfully", "user": data}

#         return response

from django.middleware import csrf
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from api.models import User
from api.util import (set_access_cookies, set_refresh_cookies, get_tokens_for_user, combine_role_permissions)
from api.serializers import UserSerializer, RoleSerializer
from django.utils import timezone
from rest_framework.permissions import AllowAny


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request):

        data = request.data
        response = Response()
        username = data.get('username', None)
        password = data.get('password', None)

        if not username or not password:
            return Response({"msg": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        #UNCOMMENT WHEN USING LDAP AUTH
        # user = None
        # if username != 'superuser':
        #     if not ldap_authenticate(username=username, password=password):
        #         return Response({"msg": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND)
        #     else:
        #         try:
        #             users = User.objects.filter(username=username, role__isnull=False).all()
        #             if len(users) == 0:
        #                 return Response({"msg": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        #
        #             user = users[0]
        #             if not user.role:
        #                 return Response({"msg": "User has no assigned role"}, status=status.HTTP_404_NOT_FOUND)
        #         except User.DoesNotExist:
        #             return Response({"msg": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        # else:
        #     user = authenticate(username=username, password=password)
        #----------------------------------------------------------------------------------------------------------

        #COMMENT WHEN USING LDAP AUTH
        user = None
        if username != 'superuser':
            users = User.objects.filter(username=username, role__isnull=False).all()
            if len(users) == 0:
                return Response({"msg": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
            user = users[0]
        else:
            user = authenticate(username=username, password=password)
        #----------------------------------------------------------------------------------------------------------

        if user is not None:
            permissions = combine_role_permissions(user.role)
            token = get_tokens_for_user(user)
            set_access_cookies(response, token['access'])
            set_refresh_cookies(response, token['refresh'])
            csrf.get_token(request)
            data = UserSerializer(user, context={'request': request}).data
            data['roles'] = RoleSerializer(user.role).data
            data['permissions'] = permissions
            response.status_code = status.HTTP_200_OK
            response.data = {"msg": "Logged in successfully", "user": data}
            user.last_login = timezone.now()
            user.save()
            return response
        else:
            return Response({"msg": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND)