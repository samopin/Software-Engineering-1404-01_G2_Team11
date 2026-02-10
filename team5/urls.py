from django.urls import path
from .views import RecommendationAPIView, FeedbackAPIView

urlpatterns = [
    path('recommendations/', RecommendationAPIView.as_view(), name='get_recommendations'), # POST/GET recommendations [cite: 194]
    path('feedback/', FeedbackAPIView.as_view(), name='post_feedback'), # Feedback endpoint [cite: 223]
]