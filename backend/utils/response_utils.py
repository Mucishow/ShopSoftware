from django.http import JsonResponse
import base64

def json_response(query_list):
    return JsonResponse(list(query_list),safe=False)