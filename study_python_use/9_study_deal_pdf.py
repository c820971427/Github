import PyPDF2

# 获取需要解析的PDF文件
pdfFile = open('../tmp_files/Python编程从入门到实践.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFile)  # 取代  PyPDF2.PdfFileReader(pdfFileObj)
print(len(pdfReader.pages))
# 获取单页的内容
pdfPage = pdfReader.pages[104]  # 取代 pageObj = pdfReader.getPage(0)
print(pdfPage.extractText)  # 取代 pageObj.extractText()
if pdfReader.is_encrypted:  # 取代 pdfReader.isEncrypted
    print('lllllll')
# 文档解密命令
# pdfReader.decrypt('rosebud')
# pdf2File = open('../tmp_files/copy_pdf.pdf', 'rb')
# pdf2Reader = PyPDF2.PdfReader(pdf2File)
pdfWriter = PyPDF2.PdfWriter()  # 取代 pdfWriter =PyPDF2.PdfFileWriter()

for pageNum in range(len(pdfReader.pages)):  # 取代 (pdfReader.numPages)
    pageObj = pdfReader.pages[pageNum]
    pdfWriter.add_page(pageObj)  # 取代 pdfWriter.addPage(pageObj)
pdfWriter.encrypt('swordfish')
pdfOutputFile = open('../tmp_files/copy_pdf.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdfFile.close()
