import numpy as np
import cv2

'''
starting image; resolution hxw
'''
h = 480 
w = 480 
img = np.ones((h, w, 3), np.uint8)

f=0
def sinwave(freq, ampl):
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

counter_blue=0
def blue_wf():
    '''
    Creates blue waves flowing over the image
        Paramters:
        Returns:
    To do: add modulation
    '''
    global counter_blue
    img[0:counter_blue, :, 0]+=1
    counter_blue+=1
    
while True:
    #noise_gen()
    #blue_wf()
    print(sinwave(0.1, 255))
    
    cv2.imshow('image', img)
    c = cv2.waitKey(1)
    if c & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

