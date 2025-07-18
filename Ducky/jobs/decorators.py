from django.contrib.auth.decorators import user_passes_test

def headhunter_required(view_func):
    """
    Decorador para verificar si el usuario está logueado y pertenece al grupo 'headhunter'.
    """
    def check_user(user):
        return user.is_authenticated and user.groups.filter(name='headhunter').exists()

    return user_passes_test(check_user, login_url='/accounts/login/')(view_func)