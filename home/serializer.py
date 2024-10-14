from rest_framework import serializers
from.models import Choclate


class ChoclateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Choclate
        fields =['id','name','price','quantity','brand']