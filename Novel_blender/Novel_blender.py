#inspired by Zach Whalen's NanoGenMo Challenge Markovify code - https://www.youtube.com/watch?v=oeL1u7n2d2s

import random
import markovify
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

#TO DO
#Create a GUI for users to select files from their computer and customise
#All user inputs must become integrated into GUI, leaning towards tkinter because mobile compatibility isn't neccessary + kivy doesn't support ios packaged past py 2.7
#Customise "Strength" of both texts by assigning variable pairs that are placed as an arguement for combined model function, i.e. (1, 1.5), (0.5, 1) etc.
#Customise amount of docs you can use, blendNovel can have optional parameter arguments to achieve this
#BUTTONS NEEDED = Save as, Open file buttons, *(strength slider), run INPUTS NEEDED = title, sentence number, strength slider

def blendNovel(file1, file2):
    
    story = " "

    #open files passed from parameters
    with open(file1, encoding="utf8") as f1:
        text1 = f1.read()

    with open(file2, encoding="utf8") as f2:
        text2 = f2.read()

    #build models
    novel_model1 = markovify.Text(text1)
    novel_model2 = markovify.Text(text2)

    #combine models thus combining texts
    combinedmod = markovify.combine([novel_model1, novel_model2])


    #create number of sentences
    storyLength = int(input("How many sentences would you like your story to be? "))
    for i in range(storyLength):
        story += str((combinedmod.make_sentence(tries=200))) + " "

        #randomly gen linebreaks
        linebreak = random.randint(0, 100)
        if linebreak < 25:
            story += "\n\n"
    
    return story

def saveToPdf(text):
    #get user inputted file name and cocatenate file extension
    filename = input(str("Save file name as: "))
    filename = filename + ".pdf"

    #grabs styles
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH = styles['Heading1']
    content = []

    #set file name
    pdf = filename

    #set document parameters
    doc = SimpleDocTemplate(
        pdf,
        pagesize=A4,
        bottomMargin=.4 * inch,
        topMargin=.6 * inch,
        rightMargin=.8 * inch,
        leftMargin=.8 * inch)

    #create header
    title = input(str("Name your story: "))
    Header = Paragraph(title, styleH)
    content.append(Header)

    #create flowable paragraph with the text and add to variable that can be stored in document
    P = Paragraph(text, styleN)
    content.append(P)

    #build document and save
    doc.build(content)

#checks if user wants to save or not
def saveQuery(story):
    while True:
        saveornot = input(str("Would you like to save this file as a pdf? [Y/N] "))
        saveornot = saveornot.lower().strip()
        try:
            if (saveornot == "yes") or (saveornot == "y") or (saveornot == "ye") or (saveornot == "yeet"):
                saveToPdf(story)
                return
            elif (saveornot == "no") or (saveornot == "n"):
                print("Thank you.")
                return
            else:
                raise ValueError

        except ValueError:
            print("Invalid Response.")



#make save button functional
def saveButton():
    print("Save the cat!")

#open file button
def openFile():
    filename = filedialog.askopenfile()
    filelabel = Label(text=filename).pack()
    return filename
        
#create the GUI, lel this code is a hot mess
def createGUI():

    #create window
    root = Tk()
    root.geometry('400x400')
    root.title("Novel Blender")
    root.wm_iconbitmap("icon.ico")

    #rendering buttons
    program = Label(root, text="Novel Blender 1.0").pack(side=TOP)
    save = Button(root, text="Generate!", command=saveButton).pack(side = BOTTOM, pady = 10)
    openf = Button(root, text="Open File", command=openFile).pack(pady = 20)
    openf2 = Button(root, text="Open File", command=openFile).pack(pady = 20)


    #run window
    root.mainloop()

def main():
    #user input text1, text2
    #novel = blendNovel("SherlockHolmes.txt", "AliceInWonderland.txt")

    #saveQuery(novel)
    
    createGUI()



main()
