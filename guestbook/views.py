from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import GuestBook
import json

# TEST
def hello_world(request):
    if request.method == "GET":
        return JsonResponse({
            'status': 200,
            'success': True,
            'message': '메시지 전달 성공!',
            'data': "Hello World!",
        })
        
# Create your views here.

@require_http_methods(["POST"])
def create_guestbook(request):
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))

        new_guestbook = GuestBook.objects.create(
            name = body['name'],
            message = body['message']
        )

        new_guestbook_json = {
            "id": new_guestbook.id,
            "name": new_guestbook.name,
            "message": new_guestbook.message
        }      

        return JsonResponse({
            'status' : 200,
            'message' : '방명록 작성 성공',
            'result' : new_guestbook_json
        })

@require_http_methods(["GET"])
def list_guestbook(request):
    if request.method == "GET":
        guestbooks = GuestBook.objects.all()

        guestbook_list = [{"id": guestbook.id, "name": guestbook.name, "message": guestbook.message, "created_at": guestbook.created_at} for guestbook in guestbooks]

        return JsonResponse({
            'status' : 200,
            'message' : '전체 방명록 조회 성공',
            'result' : guestbook_list
        })

@require_http_methods(["DELETE"])
def delete_guestbook(request, id):
    if request.method == "DELETE":
        guestbook = get_object_or_404(GuestBook, pk=id)
        guestbook.delete()

        return JsonResponse({
            'status' : 200,
            'message' : '방명록 삭제 성공',
            'result' : None
        })