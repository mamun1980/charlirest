from logging import getLogger
import pdb
from turtle import pd
from django.http import JsonResponse
from django.utils.encoding import force_str
import requests
from django.conf import settings
import time
import functools
from django.db import connection, reset_queries
import jwt
# Get an instance of a logger

logger = getLogger('ekkpay')


# Create your decorators here
def authentication(view_func):
    # import pdb; pdb.set_trace()
    def _view(request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        try:
            if request.META.get('HTTP_AUTHORIZATION', None):
                try:
                    auth_response = jwt.decode(request.META.get(
                        'HTTP_AUTHORIZATION', None), settings.SECRET_KEY)
                    request.auth_user = auth_response
                    request.HTTP_ORIGIN = request.META.get('HTTP_ORIGIN')
                except Exception as decode_exception:
                    response = {
                        'success': False,
                        'message': force_str(decode_exception),
                    }
                    logger.error(decode_exception)
                    return JsonResponse(response, status=401)
            elif request.META.get('HTTP_DASHBOARD_SECRET', None) == settings.DASHBOARD_SECRET:
                return view_func(request, *args, **kwargs)
            else:
                response = {
                    'success': False,
                    'message': 'No Authentication token provided',
                }
                return JsonResponse(response, status=403)

        except Exception as e:
            response = {
                'success': False,
                'message': force_str(e),
            }
            logger.error(e)
            return JsonResponse(response, status=401)

        return view_func(request, *args, **kwargs)

    return _view


def debugger_queries(func):
    """Basic function to debug queries."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("func: ", func.__name__)
        reset_queries()

        start = time.time()
        start_queries = len(connection.queries)

        result = func(*args, **kwargs)

        end = time.time()
        end_queries = len(connection.queries)

        print("queries:", end_queries - start_queries)
        print("took: %.2fs" % (end - start))
        return result

    return wrapper
