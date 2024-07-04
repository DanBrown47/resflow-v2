import logging
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Resume
from .serializers import ResumeSerializer

logger = logging.getLogger(__name__)

class ResumeCreateView(generics.CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if not request.data.get('name'):
            return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not request.data.get('email'):
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not request.FILES.get('file'):
            return Response({'error': 'File is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Resume uploaded successfully: {serializer.data['name']}")
            return Response({
                'message': 'Resume uploaded successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            logger.error(f"Resume upload failed: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
