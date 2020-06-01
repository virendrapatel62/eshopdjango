from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print(request.session.get('customer'))
        if not request.session.get('customer'):
           return redirect('login')

        response = get_response(request)
        return response

    return middleware