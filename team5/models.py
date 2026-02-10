from django.db import models
from django.contrib.postgres.fields import ArrayField

class City(models.Model):
    """City information for filtering and recommendations [cite: 850]"""
    city_id = models.CharField(primary_key=True, max_length=50) [cite: 859]
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, null=True, blank=True) [cite: 859]
    total_score = models.FloatField(default=0.0)
    feature = models.JSONField(default=dict) [cite: 859]

class Place(models.Model):
    """Places/Attractions (Replica) used for popularity algorithms [cite: 837, 839]"""
    place_id = models.CharField(primary_key=True, max_length=50) [cite: 849]
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='places') [cite: 915]
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255, null=True, blank=True)
    total_score = models.FloatField(default=0.0) [cite: 845]
    feature = models.JSONField(default=dict) [cite: 842, 182]

class Cluster(models.Model):
    """User clustering based on similar behavioral patterns [cite: 882, 884]"""
    cluster_id = models.CharField(primary_key=True, max_length=50)
    algorithm = models.CharField(max_length=100) [cite: 885]
    centroid_vector = ArrayField(models.FloatField(), size=60, null=True) [cite: 805]

class User(models.Model):
    """User profile and preferences [cite: 861, 864]"""
    user_id = models.CharField(primary_key=True, max_length=50)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True) [cite: 869, 922]
    cluster = models.ForeignKey(Cluster, on_delete=models.SET_NULL, null=True) [cite: 868, 956]
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    embed_vector = ArrayField(models.FloatField(), size=60, null=True) [cite: 866, 792]

class Interaction(models.Model):
    """Logs all user interactions for ML models [cite: 824, 825]"""
    interaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) [cite: 929]
    place = models.ForeignKey(Place, on_delete=models.CASCADE) [cite: 934]
    type = models.CharField(max_length=20) [cite: 831, 836]
    context = models.JSONField(default=dict) [cite: 829]
    timestamp = models.DateTimeField(auto_now_add=True) [cite: 834]

class Like(models.Model):
    """Explicit likes between users and places [cite: 896, 897]"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'place') [cite: 901]

class ABConfig(models.Model):
    """Algorithm versions management [cite: 873, 874]"""
    strategy_id = models.AutoField(primary_key=True)
    strategy_name = models.CharField(max_length=100) [cite: 880]
    is_active = models.BooleanField(default=False) [cite: 878]

class UserOfflineFeed(models.Model):
    """Cache for pre-calculated offline recommendations [cite: 888, 889]"""
    feed_id = models.AutoField(primary_key=True)
    cluster = models.OneToOneField(Cluster, on_delete=models.CASCADE) [cite: 949]
    recommended_places = models.JSONField() [cite: 895]
    generated_at = models.DateTimeField(auto_now=True)

class RecommendationLog(models.Model):
    """Records generated recommendations for analysis [cite: 905, 907]"""
    log_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) [cite: 963]
    strategy = models.ForeignKey(ABConfig, on_delete=models.CASCADE) [cite: 971]
    recommended_items = models.JSONField() [cite: 911]
    timestamp = models.DateTimeField(auto_now_add=True)