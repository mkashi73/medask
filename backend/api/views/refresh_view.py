from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.conf import settings
from api.util import set_access_cookies, set_refresh_cookies
from api.serializers import RefreshSerializer


class RefreshView(APIView):

    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RefreshSerializer(data=request.COOKIES, context={'request': request})
        serializer.is_valid(raise_exception=True)
        refresh = serializer.validated_data['refresh']

        response = Response()
        set_access_cookies(response, str(refresh.access_token))

        if settings.SIMPLE_JWT['ROTATE_REFRESH_TOKENS']:
            if settings.SIMPLE_JWT['BLACKLIST_AFTER_ROTATION']:
                try:
                    refresh.blacklist()
                except AttributeError:
                    pass

            refresh.set_jti()
            refresh.set_exp()
            refresh.set_iat()

            set_refresh_cookies(response, str(refresh))

        return response


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from rest_framework import status
# from api.util import set_access_cookies, set_refresh_cookies
# from rest_framework_simplejwt.tokens import RefreshToken, TokenError
# from django.conf import settings


# class RefreshView(APIView):

#     authentication_classes = ()
#     permission_classes = (AllowAny,)

#     def post(self, request):
#         response = Response()

#         try:
#             refresh = RefreshToken(request.COOKIES['refresh_token'])
#         except TokenError:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#         set_access_cookies(response, str(refresh.access_token))

#         if settings.SIMPLE_JWT['ROTATE_REFRESH_TOKENS']:
#             if settings.SIMPLE_JWT['BLACKLIST_AFTER_ROTATION']:
#                 try:
#                     refresh.blacklist()
#                 except AttributeError:
#                     pass

#             refresh.set_jti()
#             refresh.set_exp()
#             refresh.set_iat()

#             set_refresh_cookies(response, str(refresh))

#         return response