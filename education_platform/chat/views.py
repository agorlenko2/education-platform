from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


@login_required()
def course_chat_room(request, course_id):
    try:
        course = request.user.courses_joined.get(id=course_id)
    except ObjectDoesNotExist:
        return HttpResponseForbidden()
    return render(
        request=request,
        template_name='chat/room.html',
        context={
            'course': course
        }
    )
