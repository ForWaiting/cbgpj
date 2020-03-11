# -*- encoding: utf-8 -*-
"""
@File    : serializers.py
@Time    : 2020/3/9 16:44
@Author  : hzf
@Email   : huangzhenfang2017@163.com
@Software: PyCharm
"""
from rest_framework import serializers
from .models import *

# 序列化值得看
class WorthWatchingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=30,min_length=5, error_messages={
        'max_length':'最大30个字符',
        'min_length':'最小5个字符',
    })
    video_url = serializers.URLField(error_messages={
        'required':'需要视频地址'
    })
    img = serializers.ImageField(error_messages={
        'required':'需要一张视频图片'
    })

    def create(self, validated_data):
        instance = WorthWatching.objects.create(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.video_url = validated_data.get('video_url')
        instance.img = validated_data.get('img')
        instance.save()
        return instance

class SpecialRecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialRecommend
        fields = '__all__'

class HighlightsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10,error_messages={
        'max_length': '最大10个中文字符',
    })
    class Meta:
        model = Highlights
        fields = '__all__'


class RoleListsSerializer(serializers.ModelSerializer):

    highlights = HighlightsSerializer(many=True)
    class Meta:
        model = RoleLists
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        # fields = '__all__'
        # 排除某些信息
        exclude = ['user_permissions']

    def validate(self, attrs):
        from django.contrib.auth import hashers
        if attrs.get('password'):
            print(attrs['password'])
            attrs['password'] = hashers.make_password(attrs['password'])
        return attrs

# 用户注册序列化类
class UserRegistSerialize(serializers.Serializer):
    username = serializers.CharField(max_length=10,min_length=3,error_messages={'required':'用户名必填'})
    password = serializers.CharField(max_length=10,min_length=3,write_only=True)
    password2 = serializers.CharField(max_length=10,min_length=3,write_only=True)

    def validate_password2(self,data):
        if data != self.initial_data['password']:
            raise serializers.ValidationError('密码不一致')
        else:
            return data
    def create(self, validated_data):
        return User.objects.create_user(username=validated_data.get('username'),email=validated_data.get('email'),password=validated_data.get('password'))
