from rest_framework import viewsets
from .models import Document
from .serializers import DocumentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from .utils import extract_text_from_pdf, extract_nouns_verbs

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

@api_view(['POST'])
def upload_file(request):
    # Check if the file is included in the request
    if 'file' not in request.FILES:
        return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)
    
    file = request.FILES['file']
    
    # Save the uploaded file
    try:
        file_path = default_storage.save(file.name, file)
    except Exception as e:
        return Response({'error': f'Error saving file: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # Extract text from the file
    try:
        text = extract_text_from_pdf(file_path)
    except Exception as e:
        return Response({'error': f'Error extracting text from PDF: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # Extract nouns and verbs
    try:
        nouns, verbs = extract_nouns_verbs(text)
    except Exception as e:
        return Response({'error': f'Error extracting nouns and verbs: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # Get email from request data
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create and save Document instance
    document = Document(email=email, pdf_file=file, nouns=nouns, verbs=verbs)
    try:
        document.save()
    except Exception as e:
        return Response({'error': f'Error saving document: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # Return serialized document data
    return Response(DocumentSerializer(document).data, status=status.HTTP_201_CREATED)
