from django.shortcuts import render
from .models import *
# Create your views here.
from rest_framework import viewsets
from .serializers import *

class WorthWatchingViewSets(viewsets.ModelViewSet):
    queryset = WorthWatching.objects.all()
    serializer_class = WorthWatchingSerializer

class SpecialRecommendViewSets(viewsets.ModelViewSet):
    queryset = SpecialRecommend.objects.all()
    serializer_class = SpecialRecommendSerializer

class HighlightsViewSets(viewsets.ModelViewSet):
    queryset = Highlights.objects.all()
    serializer_class = HighlightsSerializer

class RoleListsViewSets(viewsets.ModelViewSet):
    queryset = RoleLists.objects.all()
    serializer_class = RoleListsSerializer
class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegistSerialize
        return UserSerializer