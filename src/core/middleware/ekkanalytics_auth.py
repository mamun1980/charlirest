# coding=utf-8
from functools import wraps
from jwt import decode as jwt_decode
# from config import EKKPASS_BASE_URL
# import requests
import json

def is_authorized():
    def decorator(func):
        @wraps(func)
        def auth_checker_decorated(request, *args, **kwargs):
            auth_token = request.headers.get('Authorization')
            # if authorization token is in headers
            if auth_token:
                # # post request header dictionary
                # headers = {
                #     'Authorization': request.headers.get('Authorization'),
                #     'Content-Type': 'application/json'
                # }
                # auth_verify_rsp = requests.get(
                #     EKKPASS_BASE_URL + "users/verify/auth-token",
                #     headers=headers
                # )
                #
                # # if auth request verifier status 200
                # if auth_verify_rsp.status_code == 200:
                #     request['user_verified_token'] = auth_verify_rsp.json()
                #     response = func(request, *args, **kwargs)
                #
                #     return response
                #
                # # else status code not equal 200
                # else:
                #     rsp = {
                #         'message': 'Token expired or invalid!',
                #         'status': False
                #     }
                #     return json(rsp, 402)

                decoded_jwt_token = jwt_decode(auth_token, 'EKKBAZ2015BUSINESSBLOCKCHAINSMARTCONTRACTEKKBAZ')
                request['user_verified_token'] = decoded_jwt_token
                response = func(request, *args, **kwargs)

                return response

            else:
                rsp = {
                    'message': 'Sorry, authorization token is missing!',
                    'status': False
                }
                return json(rsp, 403)

        return auth_checker_decorated

    return decorator
