from django.contrib.auth.models import User

admin_user = User.objects.get(username='admin')
last_login = admin_user.last_login
print(last_login)