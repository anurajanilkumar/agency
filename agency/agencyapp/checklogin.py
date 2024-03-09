from django.shortcuts import redirect

class CheckLoginMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        allowed_paths = ['','logins','signup']
        # Code that is executed in each request before the view is called
        if 'user_id' in request.session or request.path.strip('/') in allowed_paths:
            # print(request.session['user_id'])

            response = self.get_response(request)

        # Code that is executed in each request after the view is called
            return response
        else:
            return redirect('loginpage')

    # def process_view(request, view_func, view_args, view_kwargs):
    # #     # This code is executed just before the view is called

    # def process_exception(request, exception):
        # This code is executed if an exception is raised

    # def process_template_response(request, response):
    #     # This code is executed if the response contains a render() method
    #     return response