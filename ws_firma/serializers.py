from rest_framework import serializers
from ws_firma.models import Documento
# from .xades.sri import DocumentXML
# from .xades.xades import Xades
import logging

logger = logging.getLogger(__name__)

class DocumentoSerializer(serializers.ModelSerializer):
    # documento_firmado = serializers.SerializerMethodField(method_name="get_signed_document")
    
    def get_signed_document(self, obj):
               
        xades = Xades()
        inv_xml = DocumentXML(obj.documento, obj.documento_tipo)
        inv_xml.validate_xml()

        if obj.autorizacion == 1:
            return "AutorizacionInicio" + str(inv_xml.request_authorization(obj.clave_acceso)) + "AutorizacionFin"
        else:

            file_pk12 = '/opt/django/firma_ec/ws_firma/p12/CARLOS FRANCISCO MONTALVAN CAMPOVERDE 090720220037.p12'
            password = 'mason2020'
            
            signed_document = xades.sign(obj.documento, bytes(file_pk12, encoding = 'utf-8'), bytes (password, encoding = 'utf-8'))
            
            ok, errores = inv_xml.send_receipt(signed_document)
            
            if not ok:
                return "RespuestaSriInicio" + str(errores) + "RespuestaSriFin" + "DocumentoInicio" + signed_document.decode("utf-8")  + "DocumentoFin"
            return "RespuestaSriInicioRECIBIDARespuestaSriFin" + "DocumentoInicio" + signed_document.decode("utf-8")  + "DocumentoFin"

        # return inv_xml.request_authorization(obj.clave_acceso)

        # auth, m = inv_xml.request_authorization(obj.clave_acceso)
        # if not auth:
        #     msg = ' '.join(list(itertools.chain(*m)))
        #     return msg
        # auth_einvoice = self.render_authorized_einvoice(auth)
        # return signed_document

    class Meta:
        model = Documento
        # fields = ['fecha_creacion', 'documento', 'documento_tipo', 'documento_firmado', 'autorizacion', 'clave_acceso']
        fields = ['documento', 'documento_firmado']


# 'out_invoice': 'schemas/factura.xsd',
# 'out_refund': 'schemas/nota_credito.xsd',
# 'withdrawing': 'schemas/retencion.xsd',
# 'delivery': 'schemas/guia_remision.xsd',
# 'in_refund': 'schemas/nota_debito.xsd'