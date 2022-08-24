# coding=utf-8

import requests
from django.http import JsonResponse
from decouple import config

EKKPASS_BASE_URL = config('EKKPASS_BASE_URL', '127.0.0.1:8000')

auth_url = EKKPASS_BASE_URL + "users/verify/auth-token"

def is_authenticated(func):
    
    def auth_checker_decorated(request, *args, **kwargs):

        try:
            # import pdb; pdb.set_trace()
            # if authorization token is in headers
            if request.headers.get('Authorization', None):
                # post request header dictionary
                headers = {
                    'Authorization': request.headers.get('Authorization'),
                    'Content-Type': 'application/json'
                }
                auth_verify_rsp = requests.get(auth_url, headers=headers)

                if auth_verify_rsp.status_code == 200:
                    # if already user_verified_rsp in session
                    if request.session.get('user_verified_rsp'):
                        request.session.clear()

                    # user verified response set in session for future use
                    request.session['user_verified_rsp'] = auth_verify_rsp.json()

                # else-if status code not equal 200
                elif auth_verify_rsp.status_code != 200:
                    rsp = {
                        'message': 'Sorry, you are not authorized to access this route!',
                        'status': False,
                        'status_code': 403
                    }
                    return JsonResponse(rsp, status=auth_verify_rsp.status_code)

            else:
                rsp = {
                    'message': 'Sorry, authorization token is missing!',
                    'status': False,
                    'status_code': 403
                }
                return JsonResponse(rsp, status=403)

            return func(request, *args, **kwargs)

        except Exception as ex:
            rsp = {
                'message': str(ex),
                'status': False,
                'status_code': 403
            }
            # ekk_logger.exception(rsp)

            return JsonResponse(data=rsp)

    return auth_checker_decorated
