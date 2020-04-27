from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from event.models import Event
from event.serializers import EventSerializer

from baby.models import Baby

from guardian.shortcuts import assign_perm
from permissions.services import APIPermissionClassFactory

from django.core.exceptions import PermissionDenied


def evaluate_user_permission(user, obj, request):
    return obj.baby.parent.username == user.username

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
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
                    'perform_create': evaluate_user_permission,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        user = self.request.user
        baby = Baby.objects.get(pk=self.request.data['baby'])
        print(baby.parent.username)
        print(user.username)
        
        if(baby.parent.username == user.username):
            event = serializer.save()
            assign_perm('events.view_event', user, event)
            assign_perm('events.change_event', user, event)
            return Response(serializer.data)
        else:
            raise PermissionDenied()
        