#inspired by Zach Whalen's NanoGenMo Challenge Markovify code - https://www.youtube.com/watch?v=oeL1u7n2d2s

import random
import markovify


def blendNovel(file1, file2):
    
    with open(file1, encoding="utf8") as f1:
        text1 = f1.read()

    novel_model = markovify.Text(text1)

    for i in range(5):
        print(novel_model.make_sentence())
    
    #for testing
    #print(text1)


    
def main():
    #user input text1, text2, blendNovel(text1, text2)
    blendNovel("SherlockHolmes.txt", "AliceInWonderland.txt")



main()
