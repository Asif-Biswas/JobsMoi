
from auths.forms import RegisterForm, LoginForm

def auth_forms(request):
    reg_form = RegisterForm()
    signin_form = LoginForm()
    return {'regForm': reg_form, 'loginForm': signin_form}