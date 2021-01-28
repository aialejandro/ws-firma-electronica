# from django.shortcuts import render
from ws_firma.models import Documento
from ws_firma.serializers import DocumentoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .xades.xades import Xades
import base64

import logging

logger = logging.getLogger(__name__)

class DocumentoList(APIView):
    """
    List all documents, or create a new document.
    """
    def get(self, request, format=None):
        documentos = Documento.objects.all()
        serializer = DocumentoSerializer(documentos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DocumentoSerializer(data=request.data)
        if serializer.is_valid():
            
            xades = Xades()
            file_pk12 = '/home/aialejandro/Documentos/Bexy/BEXY MAGALY MERA FUENTES 230720185413.p12'
            password = 'bmmf1974!'
            signed_document = xades.sign(serializer.validated_data['documento'], bytes(file_pk12, encoding = 'utf-8'), bytes (password, encoding = 'utf-8'))
            
            doc_base64 = base64.b64encode(signed_document)
            doc_decoded = doc_base64.decode("UTF-8")

            print(serializer.validated_data['documento'])
            serializer.validated_data.update({'documento_firmado':doc_decoded})
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentoDetail(APIView):
    """
    Retrieve, update or delete a document instance.
    """
    def get_object(self, pk):
        try:
            return Documento.objects.get(pk=pk)
        except Documento.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        documento = self.get_object(pk)
        serializer = DocumentoSerializer(documento)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        documento = self.get_object(pk)
        serializer = DocumentoSerializer(documento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        documento = self.get_object(pk)
        documento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)