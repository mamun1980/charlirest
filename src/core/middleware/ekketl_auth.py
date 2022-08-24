# coding=utf-8
# from flask import jsonify, request, session, g
import http
from jwt import decode as jwt_decode
# from libs import EkkLogger
# ekk_logger = EkkLogger()
from django.http import JsonResponse


def is_authorized(func):
    # import pdb; pdb.set_trace()
    def auth_checker_decorated(request, *args, **kwargs):
        
        try:
            auth_token = request.headers.get('Authorization', None)
            # if authorization token is in headers
            if auth_token:
                decoded_jwt_token = jwt_decode(auth_token, 'EKKBAZ2015BUSINESSBLOCKCHAINSMARTCONTRACTEKKBAZ')
                # if already user_verified_rsp in session
                if request.session.get('user_verified_rsp'):
                    request.session.clear()

                # user verified response set in session for future use
                request.session.set('user_verified_rsp', decoded_jwt_token)

            else:
                rsp = {
                    'message': 'Sorry, authorization token is missing!',
                    'status': False,
                    'status_code': 401
                }
                return JsonResponse(rsp, status=401)

            return func(*args, **kwargs)

        except Exception as ex:
            rsp = {
                'message': str(ex),
                'status': False,
                'status_code': 403
            }

            return JsonResponse(rsp, status=403)

    return auth_checker_decorated
