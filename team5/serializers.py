from rest_framework import serializers
from .models import Place, RecommendationLog

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['place_id', 'name', 'total_score', 'feature']

class RecommendationResponseSerializer(serializers.Serializer):
    # This matches the output metadata defined in Phase 4 [cite: 198, 199]
    place_id = serializers.CharField()
    name = serializers.CharField()
    score = serializers.FloatField()
    reason = serializers.CharField() # Explanation field [cite: 1005, 1020]