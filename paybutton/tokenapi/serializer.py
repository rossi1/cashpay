from rest_framework import serializers


class SerializerUser(serializers.Serializer):
    usr = serializers.CharField(required=True, allow_blank=False)
    pwd = serializers.CharField(required=True, allow_blank=False)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class SerializerToken(serializers.Serializer):
    url = serializers.URLField(required=True, allow_blank=False)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
