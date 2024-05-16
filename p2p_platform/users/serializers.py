from rest_framework import serializers
from .models import User , Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'rating', 'balance', 'num_of_deals', 'num_of_buys', 'review_set']
        
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'rating', 'balance', 'num_of_deals', 'num_of_buys', 'Reviews']
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {'read_only': True},
            'email': {'read_only': True},
            'rating': {'read_only': True},
            'balance': {'read_only': True},
            'num_of_deals': {'read_only': True},
            'num_of_buys': {'read_only': True},
            'Reviews': {'read_only': True}
        }
        
    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.num_of_deals = validated_data.get('num_of_deals', instance.num_of_deals)
        instance.num_of_buys = validated_data.get('num_of_buys', instance.num_of_buys)
        instance.save()
        return instance
    
    
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'author', 'text', 'rating', 'created_at']
        
class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'author', 'text', 'rating', 'created_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True}
        }
        
    def create(self, validated_data):
        review = Review.objects.create(**validated_data)
        return review
    
class ReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'author', 'text', 'rating', 'created_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'read_only': True},
            'author': {'read_only': True},
            'created_at': {'read_only': True}
        }
        
    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance

