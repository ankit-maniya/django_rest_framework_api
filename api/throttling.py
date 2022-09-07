from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class JackRateThrottle(UserRateThrottle):
    scope = 'jack'
