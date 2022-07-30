from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def api_post_list_view(request):
    return Response('API Post List View')
