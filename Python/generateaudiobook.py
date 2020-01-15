#https://www.youtube.com/watch?v=UmPe07a3bWs
#https://www.youtube.com/watch?v=BFl6V4sIcWQ
#https://www.youtube.com/watch?v=5z1Irm6d_BE
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PyPDF2
from gtts import gTTS

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filelocation = askopenfilename() # open the dialog GUI


with open(filelocation, "rb") as f:  # open the file in reading (rb) mode and call it f
    pdf = PyPDF2.PdfFileReader(f) #store the pdf to pdf variable
    i=0
    Text = ""
    while i<pdf.getNumPages():
        page = pdf.getPage(i)
        Text+=page.extractText()
        i+=1
#print(text)

final_file = gTTS(text=Text, lang='en')  # store file in variable
final_file.save("Generated Speech.mp3")  # save file to computer
print("Task Completed!!")