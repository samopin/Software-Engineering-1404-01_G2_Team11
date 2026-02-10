from rest_framework.views import APIView
from rest_framework.response import Response
from .services import RecommendationService
from .models import Interaction


class RecommendationAPIView(APIView):
    def get(self, request):
        service = RecommendationService()
        # Authenticated vs Guest logic [cite: 1001, 1007]
        recommendations = service.get_recommendations(request.user, request.GET)
        return Response(recommendations)


class FeedbackAPIView(APIView):
    def post(self, request):
        # Explicit feedback logic (Like/Dislike) [cite: 1054, 1060]
        place_id = request.data.get('place_id')
        feedback_type = request.data.get('type')  # 'LIKE' or 'DISLIKE'

        Interaction.objects.create(
            user=request.user,
            place_id=place_id,
            type=feedback_type,
            context=request.data.get('context', {})[cite: 1075, 1077]
        )
        return Response({"status": "recorded"}, status=201)