from rest_framework import serializers

from credits.models import Solicitude, Client

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id','dni', 'name', 'punctuation','debt_sbs']


class SolicitudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitude
        fields = ['id','state','credit_indicator','client','amount']
        write_only_fields = ('client',)
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['client'] = ClientSerializer(instance.client).data
        return response