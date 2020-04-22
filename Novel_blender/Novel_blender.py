#inspired by Zach Whalen's NanoGenMo Challenge Markovify code - https://www.youtube.com/watch?v=oeL1u7n2d2s

import random
import markovify
import reportlab
from reportlab.pdfgen import canvas

#TO DO
#Create a GUI for users to select files from their computer and customise
#Customise length of output by making range(5) a user inputted variable
#Customise "Strength" of both texts by assinging variable pairs that are placed as an arguement for combined model function
#Customise save as with pdf and txt options, asks user to use pdf, docx or txt extensions
#Customise file name
#Customise amount of docs you can use

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

    #print number of sentences
    for i in range(10):
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

    pdf = canvas.Canvas(filename)
    pdf.drawString(150, 200, text)
    pdf.save()
    
def main():
    #user input text1, text2
    novel = blendNovel("SherlockHolmes.txt", "AliceInWonderland.txt")
    saveToPdf(novel)



main()
