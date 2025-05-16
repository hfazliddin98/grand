from rest_framework import serializers
from user.models import User




class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 
                  'last_name', 'role', 'is_active',
                  'fakultet', 'yonalish', 'kurs', 
                  'guruh', 'gpa'
                  ]
    
class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 
                  'password', 'role', 'is_active',
                  'fakultet', 'yonalish', 'kurs', 
                  'guruh', 'gpa'
                  ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Foydalanuvchini yaratish
        password = validated_data.pop('password', None)
        user = User(**validated_data)

        if password:
            user.set_password(password)  # Parolni shifrlash
            user.parol = password
        user.save()

        return user

    def update(self, instance, validated_data):
        # Foydalanuvchini yangilash
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)  # Parolni shifrlash
            instance.parol = password

        instance.save()

        return instance