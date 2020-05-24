from rest_framework import serializers

from students import models


class ProgrammeSerializer(serializers.ModelSerializer):
    """Serialize programme object"""

    class Meta:
        model = models.Programme
        fields = ('id', 'name')
        read_only_fields = ('id',)


class ClassSerializer(serializers.ModelSerializer):
    """Serializer Klass object"""
    programme = serializers.PrimaryKeyRelatedField(
        queryset=models.Programme.objects.all()
    )

    name = serializers.SerializerMethodField(method_name='get_name')

    class Meta:
        model = models.Class
        fields = (
            'id',
            'name',
            'programme',
            'programme_division',
            'year'
        )
        read_only_fields = ('id',)

    def get_name(self, obj):
        return str(obj)
