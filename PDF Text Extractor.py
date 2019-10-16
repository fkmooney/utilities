import PyPDF2

# create empty container to toss pages output into
output = ''

# read in PDF
pdf_file = open('epdf.tips_j-r.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)

# place name of file in output
output += str(pdf_file)
output += str('\n\n')

# get number of pages
number_of_pages = read_pdf.getNumPages()
print("Number of pages: ", number_of_pages)

# paramaters for loop
end_loop = number_of_pages
page_number = 0


# loop to go through PDF page by page
for page_number in range(0, end_loop):
	print("Page: ", page_number)
	output += str('\n\n')

	
	# extract text for each page
	page = read_pdf.getPage(page_number)
	page_content = page.extractText()
	
	# remove funky preaks making each page a paragraph
	page_content = page_content.encode('utf-8')
	page_content = str(page_content)
	page_content = page_content.replace('\\n', '')
	page_content = page_content.replace("b'  ", '    ')

	# add page text to output
	output += str(page_content)


else: 
	print("The End")
	output += str(page_content)
	

# create output as txt
text_file = open("Output.txt", "w")
text_file.write(output)
text_file.close()
