from rest_framework import serializers
from firstApp.models import Store

class CalcSerializer(serializers.Serializer):
    action = serializers.CharField()
    number1 = serializers.IntegerField()
    number2 = serializers.IntegerField()

    def validate(self, data):
        if data['action'] == 'divide' and data['number2'] <= 0:
            raise serializers.ValidationError("ZerroDevisionError: not 0")
        return data

    def validate_action(self, value):
        if value not in ['minus', 'plus', 'divide', 'multiply']:
            raise serializers.ValidationError("you can write 'minus' or 'plus' or 'divide' or 'multiply'")
        return value


class StoreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=800)
    rating = serializers.IntegerField(max_value=100, min_value=1)

    def create(self, validated_data):
        store = Store.objects.create(**validated_data)
        return store

class StoreNewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Store
        fields = ('name', 'description', 'rating', 'id', 'owner', 'status')
        read_only_fields = ('status',)
