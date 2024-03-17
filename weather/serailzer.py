from rest_framework import serializers
from .models import Description




class DescriptionSerailzer(serializers.ModelSerializer):
    """ serializer the Description """

    class Meta:
        model = Description
        fields = ['id','weather_dercription','temparature','create_on']