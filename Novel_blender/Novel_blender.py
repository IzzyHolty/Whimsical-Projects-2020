#inspired by Zach Whalen's NanoGenMo Challenge Markovify code - https://www.youtube.com/watch?v=oeL1u7n2d2s

import random
import markovify
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph

#TO DO
#Create a GUI for users to select files from their computer and customise
#Customise length of output by making range(5) a user inputted variable
#Customise "Strength" of both texts by assigning variable pairs that are placed as an arguement for combined model function
#Customise save as with pdf and txt options, asks user to use txt
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
    
def main():
    #user input text1, text2
    novel = blendNovel("SherlockHolmes.txt", "AliceInWonderland.txt")

    #check if the user wants to save file
    while True:
        saveornot = input(str("Would you like to save this file as a pdf? [Y/N] "))
        saveornot = saveornot.lower().strip()
        try:
            if (saveornot == "yes") or (saveornot == "y") or (saveornot == "ye") or (saveornot == "yeet"):
                saveToPdf(novel)
                return
            elif (saveornot == "no") or (saveornot == "n"):
                print("Thank you.")
                return
            else:
                raise ValueError

        except ValueError:
            print("Invalid Response.")





main()
