from rest_framework import serializers

from credits.models import Solicitude, Client

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id','dni', 'name', 'punctuation','debt_sbs']


class SolicitudeSerializer(serializers.ModelSerializer):
    #question = QuestionSerializer(read_only=True)

    class Meta:
        model = Solicitude
        fields = ['id','state','credit_indicator','client']