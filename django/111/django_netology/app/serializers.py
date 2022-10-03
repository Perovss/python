from dataclasses import field
from rest_framework import serializers
from app.models import Weapon

# class WeaponSerializers(serializers.Serializer):
#     power = serializers.IntegerField()
#     rarity = serializers.CharField()



class WeaponSerializers(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ['id','power','rarity']