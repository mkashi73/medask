from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.models import User, Role


class UserCreateUpdateView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request):
        data = request.data


        try:
            user = User.objects.get(pk=data['id'])
            user.username = data['username']
            user.name = data['name']
            user.profile_status = data['profile_status']
            user.telephone = data['telephone']
            if data['role']:
                user.role = Role.objects.get(pk=data['role'])
            else:
                user.role = None
            # user.set_password('123')    
            user.save()
        except User.DoesNotExist:
            role = None
            if data['role']:
                role = Role.objects.get(pk=data['role'])

            user = User.objects.create(
                id=data['id'],
                username=data['username'],
                name=data['name'],
                profile_status=data['profile_status'],
                telephone=data['telephone'],
                role=role
            )
            # user.set_password('123')
            user.save()

        response = Response()

        response.status_code = status.HTTP_200_OK
        response.data = {"msg": "User updated successfully"}

        return response
