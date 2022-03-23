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
    response_body = {}
    if request.body:
        response_data = json.loads(request.body)
        if not response_data['A']:
            response_body['error_msg'] = 'Введите первое число!'
            response = JsonResponse(response_body, status=HTTPStatus.BAD_REQUEST)
            print(response)
            return response
        elif not response_data['B']:
            response_body['error_msg'] = 'Введите второе число!'
            response = JsonResponse(response_body, status=HTTPStatus.BAD_REQUEST)
            return response
        else:
            num1 = float(response_data['A'])
            num2 = float(response_data['B'])
            summa = num1 + num2
            response_body['answer'] = summa
            response = JsonResponse(response_body)
            return response


def subtract(request):
    response_body = {}
    if request.body:
        response_data = json.loads(request.body)
        if not response_data['A']:
            response_body['error_msg'] = 'Введите первое число!'
            response = JsonResponse(response_body, status=HTTPStatus.BAD_REQUEST)
            print(response)
            return response
        elif not response_data['B']:
            response_body['error_msg'] = 'Введите второе число!'
            response = JsonResponse(response_body, status=HTTPStatus.BAD_REQUEST)
            return response
        else:
            num1 = float(response_data['A'])
            num2 = float(response_data['B'])
            subtraction = num1 - num2
            response_body['answer'] = subtraction
            response = JsonResponse(response_body)
            return response


def multiply(request):
    response_body = {}
    if request.body:
        response_data = json.loads(request.body)
        if not response_data['A']:
            response_body['error_msg'] = 'Введите первое число!'
            response = JsonResponse(response_body, status=HTTPStatus.BAD_REQUEST)
            print(response)
            return response
        elif not response_data['B']:
            response_body['error_msg'] = 'Введите второе число!'
            response = JsonResponse(response_body, status=HTTPStatus.BAD_REQUEST)
            return response
        else:
            num1 = float(response_data['A'])
            num2 = float(response_data['B'])
            product = num1 * num2
            response_body['answer'] = product
            response = JsonResponse(response_body)
            return response


def divide(request):
    response_body = {}
    if request.body:
        response_data = json.loads(request.body)
        if not response_data['A']:
            response_body['error_msg'] = 'Введите первое число!'
            response = JsonResponse(response_body, status=HTTPStatus.BAD_REQUEST)
            print(response)
            return response
        elif not response_data['B']:
            response_body['error_msg'] = 'Введите второе число!'
            response = JsonResponse(response_body, status=HTTPStatus.BAD_REQUEST)
            return response
        else:
            num1 = float(response_data['A'])
            num2 = float(response_data['B'])
            if num2 == 0:
                response_body['error_msg'] = 'Делить на НОЛЬ нельзя!'
                response = JsonResponse(response_body, status=HTTPStatus.BAD_REQUEST)
                return response
            division = num1 / num2
            response_body['answer'] = division
            response = JsonResponse(response_body)
            return response
