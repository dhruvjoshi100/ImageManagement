from ImageApp.models import MyPhoto
from ImageApp.serializers import PhotoSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from ImageApp.permit import IsOwnerOrReadOnly
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import detail_route, api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    for user in User.objects.all():
        Token.objects.get_or_create(user=user)
    


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = MyPhoto.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)