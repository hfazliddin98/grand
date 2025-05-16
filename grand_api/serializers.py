from rest_framework.serializers import ModelSerializer
from grand_ariza.models import Ariza


class ArizaGetSerializer(ModelSerializer):
    class Meta:
        model = Ariza
        fields = ['id', 'user', 'oquv', 'manaviyat', 'ilmiy', 
                  'ariza_role', 'tasdiqlash', 'rad_etish', 'is_active'
                ]
    

class ArizaPostSerializer(ModelSerializer):
    class Meta:
        model = Ariza
        fields = ['user', 'oquv', 'manaviyat', 'ilmiy', 
                  'ariza_role', 'tasdiqlash', 'rad_etish', 'is_active'
                ]