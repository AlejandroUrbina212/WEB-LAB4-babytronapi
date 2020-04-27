from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from parent.models import Parent
from baby.models import Baby 
from event.models import Event

from parent.serializers import ParentSerializer
from baby.serializers import BabySerializer
from event.serializers import EventSerializer

from guardian.shortcuts import assign_perm
from permissions.services import APIPermissionClassFactory

def evaluate_user_permission(user, obj, request):
    return user.username == obj.parent.username

class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='BabyPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': evaluate_user_permission,
                    'destroy': evaluate_user_permission,
                    'update': evaluate_user_permission,
                    'partial_update': evaluate_user_permission,
                    'events': evaluate_user_permission
                }
            }
        ),
    )
    # create a baby and give the user in the request permission to change and view the
    # created baby, via assign_perm
    def perform_create(self, serializer):
        baby = serializer.save()
        user = self.request.user
        assign_perm('baby.change_baby', user, baby)
        assign_perm('baby.view_baby', user, baby)
        return Response(serializer.data)

    @action(detail=True, url_path='events' , methods=['get'])
    def events(self, request, pk=None):
        baby = self.get_object()
        events = Event.objects.filter(baby = baby)
        data = EventSerializer(events, many = True).data
        return Response(data)

