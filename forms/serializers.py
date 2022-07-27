from .models import MyModel
from rest_framework import serializers

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyModel
        fields = ('fullname', 'gender','mobile_number','email','company_name','visit_date','id_proof','id_number')
