from PyPDF2 import PdfMerger

merger = PdfMerger()

input1 = open("ex1.pdf","rb")
input2 = open("ex2.pdf","rb")
input3 = open("ex3.pdf","rb")

for i in [input1,input2,input3]:
    merger.append(i)

output = open("output.pdf","wb")
merger.write(output)

merger.close()
output.close()