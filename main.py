import pdfplumber
import pyttsx3
 
speaker = pyttsx3.init()
 
book = "todayndtomorrow.pdf"
with pdfplumber.open(book) as pdf:
    page = pdf.pages[74]
    print(page.extract_text())
    speaker.say(page.extract_text())
    speaker.runAndWait()