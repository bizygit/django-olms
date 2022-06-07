from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# to extend users UserCreationForm with ohter fields 
# user model

# Add Some Extra fields in UserCreation Form
class MyUserCreationForm(UserCreationForm):
    
    # CH=(
    #     ('lecture','Lecture'),
    #     ('learner','Learner')
    # )
    # role = forms.CharField(widget=forms.RadioSelect(choices=CH))

    class Meta:
        model = User
        #fields='__all__'
        # for seelcted fields 
        fields=('first_name','last_name','username','email','password1','password2')


class MyUserCreationForm1(UserCreationForm):

    class Meta:
        model = User
        #fields='__all__'
        # for seelcted fields 
        fields=('username','email', 'password')
