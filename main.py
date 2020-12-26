import pyttsx3
import PyPDF2

book = open('art-of-the-deal.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()

for r in range(0, pages):
    page = pdfReader.getPage(4)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
    