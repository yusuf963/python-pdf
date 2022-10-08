from PyPDF2 import PdfReader
import pyttsx3

reader = PdfReader("mat67-Common_Math_Symbols.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)
# engine = pyttsx3.init()
# engine.say(text)
# engine.runAndWait()