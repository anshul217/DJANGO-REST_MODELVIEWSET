from rest_framework.viewsets import ModelViewSet

from .serializers import Inventory, InventorySerializer


class InventoryModelViewSet(ModelViewSet):
  queryset = Inventory.objects.all()
  serializer_class = InventorySerializer
