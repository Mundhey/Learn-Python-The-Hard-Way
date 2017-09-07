
txt=raw_input("File name?")
text=open(txt)

print"Her's your file %r "% txt
print text.read()

text.close()
