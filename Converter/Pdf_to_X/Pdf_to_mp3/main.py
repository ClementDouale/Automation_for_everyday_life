import pyttsx3,PyPDF2
from PyPDF2 import PdfReader

## Utility of this project : being able to listen to a specific text / book / lesson when we can't focus on reading it
pdfreader = PdfReader('book.pdf')
speaker = pyttsx3.init()

## Going through each page of the document until the end
for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
    
speaker.save_to_file(clean_text, 'book.mp3')
speaker.runAndWait()

speaker.stop()