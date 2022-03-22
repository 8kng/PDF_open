from pikepdf import Pdf

password = input('Password=')
path = input('path=')
filename = path + "\\" + input('filename=')
#filename = "2021_1126_後学期_CA_第15回_補助記憶装置.pdf"
newfilename = filename + "_unlock.pdf"

pdf = Pdf.open(filename + ".pdf", password=password)
pdf_unlock = Pdf.new()
pdf_unlock.pages.extend(pdf.pages)
pdf_unlock.save(newfilename)