from snippetsapp.models import Snippet
from snippetsapp.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, viewsets
from rest_framework import permissions
from django.contrib.auth.models import User


"""
對GenericAPIView再進行包裝，類名也顯示出他會有什麼功能
"""
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # 覆寫perform_create()方法，perform_create方法是在使用create操作時負責進行數據持久化動作
    def perform_create(self, serializer):
        # 在持久化前，先把owner字段賦值為當前登入用戶
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


from rest_framework import renderers
from rest_framework.response import Response


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        # get_object()取出當前對象
        snippet = self.get_object()
        return Response(snippet.highlighted)
