from django.conf import settings


SESSION_REDIS_HOST = getattr(settings, 'SESSION_REDIS_HOST', 'localhost')
SESSION_REDIS_PORT = getattr(settings, 'SESSION_REDIS_PORT', 6379)
SESSION_REDIS_DB = getattr(settings, 'SESSION_REDIS_DB', 0)
SESSION_REDIS_PREFIX = getattr(settings, 'SESSION_REDIS_PREFIX', '')
SESSION_REDIS_PASSWORD = getattr(settings, 'SESSION_REDIS_PASSWORD', None)
SESSION_REDIS_UNIX_DOMAIN_SOCKET_PATH = getattr(
    settings, 'SESSION_REDIS_UNIX_DOMAIN_SOCKET_PATH', None
)
SESSION_REDIS_URL = getattr(settings, 'SESSION_REDIS_URL', None)

SESSION_REDIS_NODES =  getattr(settings, 'SESSION_REDIS_NODES',
                               [{"host": "127.0.0.1", "port": "30001"},
                                {"host": "127.0.0.1", "port": "30002"},
                                {"host": "127.0.0.1", "port": "30003"},
                                {"host": "127.0.0.1", "port": "30004"},
                                {"host": "127.0.0.1", "port": "30005"},
                                {"host": "127.0.0.1", "port": "30006"},
                                ])