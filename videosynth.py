import numpy as np
import cv2

'''
starting image; resolution hxw
'''
h = 480 
w = 720 
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
    global h, w
    x=np.random.randint(0, h, 10)
    y=np.random.randint(0, w, 10)
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

''' Parameters for opencv rotation matrix function'''
(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)
angle = 180
zoom = 1.01
'''Filter kernel for video feedback simulation'''
fb_ker_outside = 0.11
fb_ker_center = -10
feedback_kernel = np.array(
    [[fb_ker_outside, fb_ker_outside, fb_ker_outside, fb_ker_outside, fb_ker_outside],
     [fb_ker_outside, fb_ker_outside, fb_ker_outside, fb_ker_outside, fb_ker_outside],
     [fb_ker_outside, fb_ker_outside, fb_ker_center, fb_ker_outside, fb_ker_outside],
     [fb_ker_outside, fb_ker_outside, fb_ker_outside, fb_ker_outside, fb_ker_outside],
     [fb_ker_outside, fb_ker_outside, fb_ker_outside, fb_ker_outside, fb_ker_outside]])

def faux_feedback():
    '''
    Combination of rotation and filtering image simulating analog camera feedback
        Parameters:
        Returns:
    '''
    global img
    M = cv2.getRotationMatrix2D((cX, cY), angle, zoom)
    rotated = cv2.warpAffine(img, M, (w, h))
    img = rotated
    img = cv2.filter2D(img, -1, feedback_kernel)

def reset():
    '''
    reset function to return to black image and start over synthesis
    '''
    global img, counter_blue_bottom, counter_blue_top, f
    img = np.ones((h, w, 3), np.uint8)
    counter_blue_top=0
    counter_blue_bottom=479
    f=0
reset()

while True:
    noise_gen()
    #blue_wf()
    faux_feedback()
    cv2.imshow('image', img)
    c = cv2.waitKey(10)
    if c & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
    if c & 0xFF == ord("r"):
        reset()
