from dashboard import models


def auth(username, password):
    try:
        user = models.Users.objects.get(username=username)
        return user.check_password(password)
    except models.Users.DoesNotExist:
        return False