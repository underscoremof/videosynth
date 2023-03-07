import numpy as np
import cv2

'''
starting image; resolution hxw
'''
h = 480 
w = 480 
img = np.ones((h, w, 3), np.uint8)

f=0
def sinwave(freq=0.03, ampl=255):
    '''
    Simple sine wave function
    can be used to modulate color intensity
        Parameters: 
                freq (float): Frequency of sine wave; usefull values between 0.001 and 0.1?
                ampl (int): Amlitude of sine wave; should be between 0 and 255
        Returns: 
                jj (int): oscillating value between 0 and amplitude
    '''
    global f
    jj=int(((np.sin(f)+1)/2)*ampl)
    #frequency
    f+=freq
    return jj

def noise_gen():
    '''
    Basic noise generator function
        Paramters:
        Returns:
    To do: add modulation
    '''
    x=np.random.randint(0, 480, 100)
    y=np.random.randint(0, 480, 100)
    b=np.random.randint(0,255)
    g=np.random.randint(0,255)
    r=np.random.randint(0,255)
    img[x, y, :]=[b, g, r]

counter_blue_top=0
counter_blue_bottom=479
def blue_wf(speed=5):
    '''
    Creates blue waves flowing over the image
        Paramters:
                speed (float): Speed and direction of the waves;
        Returns:
    To do: add modulation
    '''
    global counter_blue_top, counter_blue_bottom
    if speed==0:
        pass
    elif speed>=1:
        img[0:counter_blue_top, :, 0]+=speed
        counter_blue_top+=1
    else:
        img[counter_blue_bottom:479, :, 0]-=abs(speed)
        counter_blue_bottom-=1

def reset():
    '''
    reset function to return to black image
    '''
    global img, counter_blue_bottom, counter_blue_top, f
    #reset image
    img = np.ones((h, w, 3), np.uint8)
    #reset blue wave function
    counter_blue_top=0
    counter_blue_bottom=479
    #reset sine wave
    f=0

reset()
    
while True:
    cv2.imshow('image', img)
    noise_gen()
    #blue_wf()

    #cv2.imshow('image', img)
    c = cv2.waitKey(1)
    if c & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
    if c & 0xFF == ord("r"):
        reset()

