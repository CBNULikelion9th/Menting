from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'studenttype', 'nickname',
        'university', 'studentnumber','mentor_check','name', 'major','highschool','entrancetype','image']

