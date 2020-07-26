

# 정규표현식 파일 import
from reg import REGEX_EXPRESSION

import re
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open



FILE_PATH = "C:/test_3.pdf"

# pdf 를 텍스트로 바꿔주는 함수
def read_pdf_file(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

'''
pdf_file = open(FILE_PATH, "rb")
contents = read_pdf_file(pdf_file)
pdf_file.close()
regex = re.compile('{}'.format(REGEX_EXPRESSION))

# pdf 파일의 텍스트 중 불러온 정규표현식에 맞는 match (주민등록번호) 들을 찾는다
matchobj = regex.finditer(contents)

# 찾은 match들 출력하기
for r in matchobj:
    print(r.group())
'''
import docx

templ = docx.Document('C:\\test_modify.docx')

for x, paragraph in enumerate(templ.paragraphs):
    print(str(x) + " : " + paragraph.text)