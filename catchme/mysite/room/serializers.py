
from rest_framework import serializers
from common.models import *

class MenPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = menParty
        fields = ['pnum','name','age','school']

class WomenPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = womenParty
        fields = ['pnum','name','age','school']

class MenInfoSerializer(serializers.ModelSerializer):
    menPartys = MenPartySerializer(many = True, read_only = True, source = 'men_party')
    class Meta:
        model = menInfo
        fields = ['nickname','ready','menPartys','school','major']
        

class WomenInfoSerializer(serializers.ModelSerializer):
    womenPartys = WomenPartySerializer(many = True, read_only = True, source = 'women_party')
    class Meta:
        model = menInfo
        fields = ['nickname','ready','womenPartys','school','major']
        

class RoomSerializer(serializers.ModelSerializer):
    menInfos = MenInfoSerializer(many = True, read_only = True, source = 'men_infos')# source에 등록한 것은 model에서 related_name항목
    womenInfos = WomenInfoSerializer(many = True, read_only = True,source = 'women_infos')

    mnum = serializers.SerializerMethodField()
    wnum = serializers.SerializerMethodField()


    def get_mnum(self, obj):
        # men_infos 관련 객체의 개수를 반환합니다.
        return obj.men_infos.count()
    
    def get_wnum(self, obj):
        # men_infos 관련 객체의 개수를 반환합니다.
        return obj.women_infos.count()

    class Meta :
        model = room
        fields = ['rno','rname', 'mnum','wnum','created_at','location','menInfos','womenInfos']