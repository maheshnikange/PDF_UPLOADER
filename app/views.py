from django.shortcuts import render
import PyPDF2
from PyPDF2 import PdfWriter, PdfFileReader, PdfFileMerger
import os
from django.core.files.storage import FileSystemStorage
from .models import demo1

# Create your views here.
def index(request):
    if request.method=='POST':
        pdf_file=request.FILES.get('file1')
        fs = FileSystemStorage()
        filename = fs.save(pdf_file.name, pdf_file)
        uploaded_file_path = fs.path(filename)
        print('absolute file path', uploaded_file_path)   

# -------------------read pdf file------------------------

# Importing required modules

        pdfFileObj = open(uploaded_file_path,'rb')                  # Creating a pdf file object
        pdfReader = PyPDF2.PdfReader(pdfFileObj)                    # Creating a pdf reader object

        pages =  len(pdfReader.pages)                               # Getting number of pages in pdf file
        for i in range(pages):                                      # Loop for reading all the Pages
            pageObj = pdfReader.pages[i]                             # Creating a page object
            print("Page No: ",i)                                     # Printing Page Number

            Extracted_text = pageObj.extract_text()                            # Extracting text from page And splitting it into chunks of lines
            text = pageObj.extract_text().split("  ")                # Extracting text from page And splitting it into chunks of lines

            for i in range(len(text)):
                if 'NAME OF NATURAL GAS PIPELINE' in text[i]:
                    NAME_OF_NATURAL_GAS_PIPELINE=text[i+2]
                if 'BID DOCUMENT NO' in text[i]:
                    BID_DOCUMENT_NO=text[i+2]
                if 'demand draft for' in text[i]:
                    k=text[i].split()
                    for p,j in enumerate(k):
                        if 'Rs' in j:
                            print(p,'-----------',j,k[p+1])
                            Tender_Document_Fee=k[p+1]

            print()

        old_text1 = Tender_Document_Fee
        new_text1 = '5000'
        text = Extracted_text.replace(old_text1, new_text1)                 # replace text in pdf




# ---------------------------------------------------------
# -----------------------------------------------------------
        # import PyPDF2
        # pdfFileObj = open(uploaded_file_path, 'rb')
        # pdfReader = PyPDF2.PdfReader(pdfFileObj)
        # # pdfReader.numPages
        # pdfWriter = PyPDF2.PdfWriter()

        # for pageNum in range(len(pdfReader.pages)):
        #     pageObj = pdfReader.pages[pageNum]
        #     TEST = pageObj.extract_text()
        #     if TEST.find("TEXT") != -1:
        #         pdfWriter.addPage(pageObj)
        # pdfOutput = open(uploaded_file_path, 'wb')
        # pdfWriter.write(pdfOutput)
        # pdfOutput.close()












        pdfFileObj.close()                              # closing the pdf file object
        data=demo1.objects.create(NAME_OF_NATURAL_GAS_PIPELINE=NAME_OF_NATURAL_GAS_PIPELINE,BID_DOCUMENT_NO=BID_DOCUMENT_NO,Tender_Document_Fee=Tender_Document_Fee)        
        data.save()
        return render(request,'index.html')
    else:
        return render(request,'index.html')