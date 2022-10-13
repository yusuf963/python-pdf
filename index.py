from PyPDF2 import PdfReader
import pyttsx3

reader = PdfReader("bbc_contract.pdf")
number_of_pages = len(reader.pages)
for i in range(number_of_pages):
    page = reader.pages[i]
    text = page.extract_text()
    # print(text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()