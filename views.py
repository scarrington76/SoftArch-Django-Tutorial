from django.http import HttpResponse, JsonResponse


def index(request):
    response = {
        'Message' : 'Hello World!!'
    }
    return JsonResponse(response)

def htmltype(request):
    return HttpResponse()