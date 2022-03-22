import json
from datetime import datetime
from http import HTTPStatus

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed


@ensure_csrf_cookie
def get_csrf_token(request):
    if request.method == "GET":
        return HttpResponse()
    return HttpResponseNotAllowed(["GET"])


def echo_view(request):
    response_data = {
        "method": request.method,
        "datetime": datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    }

    if request.body:
        response_data["body"] = json.loads(request.body)
    response = JsonResponse(response_data)
    return response


def add(request):
    body = {}
    response_data = json.loads(request.body)
    if type(response_data['A']) == int and type(response_data['B'] == int):
        summa = response_data['A'] + response_data['B']
        body['answer'] = summa
        response = JsonResponse(body)
        return response
    else:
        body['error'] = 'Must be integers!'
        response = JsonResponse(body, status=HTTPStatus.BAD_REQUEST)
        return response


def subtract(request):
    body = {}
    response_data = json.loads(request.body)
    if type(response_data['A']) == int and type(response_data['B'] == int):
        summa = response_data['A'] - response_data['B']
        body['answer'] = summa
        response = JsonResponse(body)
        return response
    else:
        body['error'] = 'Must be integers!'
        response = JsonResponse(body, status=HTTPStatus.BAD_REQUEST)
        return response


def multiply(request):
    body = {}
    response_data = json.loads(request.body)
    if type(response_data['A']) == int and type(response_data['B'] == int):
        summa = response_data['A'] * response_data['B']
        body['answer'] = summa
        response = JsonResponse(body)
        return response
    else:
        body['error'] = 'Must be integers!'
        response = JsonResponse(body, status=HTTPStatus.BAD_REQUEST)
        return response


def divide(request):
    body = {}
    response_data = json.loads(request.body)
    if type(response_data['A']) == int and type(response_data['B'] == int):
        if response_data['B'] != 0:
            summa = response_data['A'] / response_data['B']
            body['answer'] = summa
            response = JsonResponse(body)
            return response
        else:
            body['error'] = 'Division by zero!'
            response = JsonResponse(body, status=HTTPStatus.BAD_REQUEST)
            return response
    body['error'] = 'Must be integers!'
    response = JsonResponse(body, status=HTTPStatus.BAD_REQUEST)
    return response
