# Import required packages
import cv2
import pytesseract


# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Read image from which text needs to be extracted
img = cv2.imread("base.jpeg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
#detecting characters
#hImg,wImg,_=img.shape
#oxes=pytesseract.image_to_boxes(img)
#for b in boxes.splitlines():
 #   b=b.split(' ')
  #  print(b)
   # x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    #cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,225),3)
    #cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,225),2)


#detecting words
hImg,wImg,_=img.shape
boxes=pytesseract.image_to_data(img)
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b=b.split()
        print(b)
        if len(b)==12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,225),3)
            cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,225),2)
cv2.imshow('Result',img)

key = cv2.waitKey(0) 
