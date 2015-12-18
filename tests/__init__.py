from django.conf import settings


settings.configure(
    SESSION_ENGINE='cluster_redis_sessions.session'
)
