import pdfplumber
import pyttsx3
 
speaker = pyttsx3.init()
 
book = "todayndtomorrow.pdf"
with pdfplumber.open(book) as pdf:
    # for reading one page or any specific page
    page = pdf.pages[74]
    print(page.extract_text())
    speaker.say(page.extract_text())
    speaker.runAndWait()

# for reading the whole pdf
    pages = pdf.pages
    for i,pg in enumerate(pages):
        content = pages[i].extract_text()
        print(content)
        speaker.say(content)
        speaker.runAndWait()