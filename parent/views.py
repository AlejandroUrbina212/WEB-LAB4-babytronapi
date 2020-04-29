from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from parent.models import Parent
from parent.serializers import ParentSerializer

from baby.models import Baby 
from baby.serializers import BabySerializer



from guardian.shortcuts import assign_perm
from permissions.services import APIPermissionClassFactory

from django.core.exceptions import PermissionDenied

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    @action(detail=True,url_path='babies', methods=['get'])
    def viewBabies(self, request, pk=None):
        parent = self.get_object()
        print(parent.username)
        print(self.request.user)
        if (parent.username == self.request.user.username):
            babies = Baby.objects.filter(parent = parent)
            data = BabySerializer(babies, many = True).data
            return Response(data)
        else:
            raise PermissionDenied()
        





