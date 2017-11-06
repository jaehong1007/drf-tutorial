from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method == 'GET':
        # snippets는 모든 Snippet의 쿼리셋
        snippets = Snippet.objects.all()
        # 쿼리셋을 serialize할 때는 many=True 옵션 추가
        serializer = SnippetSerializer(snippets, many=True)
        # JSON방식으로 reponse
        # 기본적으로 JsonResponse는 dict형 객체를 받아 처리하나
        # safe옵션이 False이면 주어진 데이터가 dict가 아니어도 됨
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
