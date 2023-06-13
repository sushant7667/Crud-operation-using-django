from rest_framework import serializers
from .models import *

class Countryserializer(serializers.ModelSerializer):
    class Meta:
        model = countrymodel
        fields = '__all__'

class Stateserializer(serializers.ModelSerializer):
    class Meta:
        model = statemodel
        fields = '__all__'

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = Employeecrud
        fields = '__all__'

class checkboxserializer(serializers.ModelSerializer):
    class Meta:
        model = checkbox
        fields = '__all__'

class hobbiesserializer(serializers.ModelSerializer):
    class Meta:
        model = checkboxmany
        fields = '__all__'