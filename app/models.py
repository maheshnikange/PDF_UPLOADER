from django.db import models

# Create your models here.
class PdfFile(models.Model):
    pdf_file=models.FileField(upload_to='PDF_FILES',null=True,default=None)
class demo1(models.Model):
    NAME_OF_NATURAL_GAS_PIPELINE=models.CharField(max_length=30)
    BID_DOCUMENT_NO=models.CharField(max_length=30)
    Tender_Document_Fee=models.CharField(max_length=30)

    def __str__(self):
        return self.NAME_OF_NATURAL_GAS_PIPELINE