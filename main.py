import cv2 as cv
import numpy as np
from random import randint

background = cv.imread("background.png") #sets the background


string='Thanks for downloading!'.replace(".", "ა").replace('"', "ბ").replace('?', "გ").replace('<', "ე").replace('>', "ვ").replace(':', "ჰ").replace('/', "ჯ").replace('\\', "კ") # replaces ."?<>:/\ because Windows can't name files like this


x_offset=0
y_offset=0
row = 0

downward = "ßjgpy" #sets the letters wich should be moved under

for letter in string:

    if letter == " ": #for spaces
        letter_image = cv.imread("letters/space.png")
     
    elif letter.isupper(): #for capital letters
        letter_image = cv.imdecode(np.fromfile(f"letters/{letter}/upper/{randint(1, 3)}.png", dtype=np.uint8), cv.IMREAD_UNCHANGED) #loads image of character

    else: #for lowercase letters
        letter_image = cv.imdecode(np.fromfile(f"letters/{letter}/lower/{randint(1, 3)}.png", dtype=np.uint8), cv.IMREAD_UNCHANGED) #loads image of character
     


    #the png image can't be higher then 60px
    if letter in downward:
        y_offset=int(60-letter_image.shape[0]+(0.5*letter_image.shape[0])) #checks if the character should be moved 
    else:    
        y_offset=int(60-letter_image.shape[0])
   

    if x_offset >= 1630: #for the row arrangement
        x_offset = 0
        row+=1
    
    
    y_offset+= 80*row #sets the row
    
    


    
    background[y_offset:y_offset+letter_image.shape[0], x_offset:x_offset+letter_image.shape[1]] = letter_image #sets the image in place

    
    x_offset+=letter_image.shape[1] #expands the line


cv.imwrite("result.png", background)   #writes the final image 




    

