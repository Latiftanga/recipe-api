from students import models
from students import serializers

from core.views import CreateRetrieveUpdateViewSet


class ClassAPIViewSet(CreateRetrieveUpdateViewSet):
    """Create Read and Update views for classes"""

    queryset = models.Class.objects.all()
    serializer_class = serializers.ClassSerializer
