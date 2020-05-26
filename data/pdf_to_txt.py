from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import argparse
import os
import io

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()

    filename = path[:-4]
    with io.open(filename +".txt", "w+", encoding="utf-8") as f:
        f.write(str(text))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', help="Requires the directory to your pdf files")
    args = parser.parse_args()
    file_path = args.input_path
    file_list = os.listdir(file_path)
    for file in file_list:
        fileName = os.path.join(file_path, file)
        convert_pdf_to_txt(fileName)
