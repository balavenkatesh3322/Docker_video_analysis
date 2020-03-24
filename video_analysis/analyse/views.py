from django.shortcuts import render
from rest_framework.views import APIView
from analyse.analyse import detect_objects_from_video
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class AnalyseVideoView(APIView):

	def get(self, request):
		video_url = self.request.query_params.get('video_url')
		print(video_url)
		if video_url is not None:
		    detect_objects_from_video(video_url)
		    return Response(data={'data': {'message': 'Successfully updated'}},
		                    status=status.HTTP_200_OK)
		else:
		    return Response(data={'data': {'message': 'No video_url in the request'}},
		                    status=status.HTTP_404_NOT_FOUND)