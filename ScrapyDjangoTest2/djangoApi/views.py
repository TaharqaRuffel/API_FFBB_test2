from django.shortcuts import render

# Create your views here.
from djangoApi.models import Match
from djangoApi.serializers import MatchSerializer, UserSerializer
from djangoApi.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import mixins, viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

class MatchViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        match = self.get_object()
        return Response(match.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
