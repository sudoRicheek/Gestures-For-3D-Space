import cv2
import pyautogui

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import numpy as np
import os
import time


CWD = os.getcwd()
MODEL_PATH = os.path.join(CWD , "gestures_vgg16_finetuned_multilabel.h5")

classmodel = load_model(MODEL_PATH, compile=False)
print("Loaded Model from Disk")

isBgCaptured = False
threshold = 60
learningRate = 0
bgModel = None
framecount = 0
indices = {0 : 'cool', 1 : 'fist', 2 : 'ok', 3 : 'stop', 4 : 'yo'}

secondgesture = 0
firstgesture = 0
lengthgesture = 1
executeflag  = False

altflag = False
volflag = False

cap = cv2.VideoCapture(0)

def remove_background(frame):        
    foremask = bgModel.apply(frame, learningRate=learningRate)
    kernel = np.ones((3, 3), np.uint8)
    foremask = cv2.erode(foremask, kernel, iterations=1)
    finalres = cv2.bitwise_and(frame, frame, mask=foremask)
    return finalres


while(True):
    ret, img = cap.read()
    img = cv2.bilateralFilter(img, 5, 50, 100)
    img = cv2.flip(img,1)
    img = img[100:400, 100:400]
    cv2.imshow('Original Window', img)
    
    
    
    if isBgCaptured == True and framecount % 2 == 1:
        frame = remove_background(img)
        
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        value = (35, 35)
        blurred = cv2.GaussianBlur(grey, value, 0)
        _, thresh = cv2.threshold(blurred, threshold, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cv2.imshow("thresh", thresh)
        
        if np.count_nonzero(thresh.astype(np.float32))/900.0 > 3.0 :
         
            cv2.imwrite("test.jpg", thresh)
            
            img = image.load_img("test.jpg", target_size=(224, 224), color_mode='rgb')
            img_tensor = image.img_to_array(img)
            img_tensor = np.expand_dims(img_tensor, axis=0)
            img_tensor /= 255.
            
            prediction = classmodel.predict(img_tensor)
        
            predict = np.argmax(prediction)
            if prediction[0][predict] > 0.5 :
                gestureclass = indices[predict]
                
                secondgesture = firstgesture
                firstgesture = predict
                #print(gestureclass)
                
                if secondgesture != firstgesture :
                    lengthgesture = 1
                    executeflag = True
                else :    
                    lengthgesture += 1
                    
                if lengthgesture > 2 and executeflag == True:
                    if secondgesture == 0 and altflag:
                        pyautogui.press('tab')
                        print('tab')
                    
                    if secondgesture == 0 and volflag:
                        pyautogui.press('volumeup')
                        print('volumeup')
                        
                    if secondgesture == 3 and volflag:
                        pyautogui.press('volumedown')
                        print('volumedown')
                    
                    if secondgesture == 3 and not volflag:
                        if altflag :
                            pyautogui.keyUp('altleft')      
                            altflag = False
                            print('unpressed altleft')
                        else :
                            pyautogui.keyDown('altleft')
                            altflag = True
                            print('pressed altleft')
                        
                    if secondgesture == 2 :
                        if volflag :   
                            volflag = False
                            print('unpressed volcontrol')
                        else :
                            volflag = True
                            print('pressed volcontrol')
                            altflag = False
                            print('unpressed altleft')
                            
                    if secondgesture == 4 :
                        pyautogui.press('playpause')
                        print('playpause')
                        
                    executeflag = False
                        
    
    #KeyBoard stuff
    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == ord('b'):  # press 'b' to capture the background
        bgModel = cv2.createBackgroundSubtractorMOG2(0, 50, detectShadows = False)
        isBgCaptured = True
        time.sleep(1)
        print('Background captured')
    elif k == ord('r'):  # press 'r' to reset the background
        time.sleep(1)
        bgModel = None
        isBgCaptured = False
        print('Reset background')
    
    framecount += 1
            
        
cap.release()
cv2.destroyAllWindows()