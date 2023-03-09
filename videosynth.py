import numpy as np
import cv2

'''
starting image; resolution hxw
'''
h = 480 
w = 720 
img = np.zeros((h, w, 3), np.uint8)
filtered = np.zeros((h, w, 3), np.uint8)
preprocessing=np.zeros((1, w, 3), np.uint8)
cv2.namedWindow('Video')
cv2.namedWindow('Processing')

f=0
def sinwave(freq=0.03, ampl=255):
    '''
    Simple sine wave function
    can be used to modulate color intensity?
        Parameters: 
                freq (float): Frequency of sine wave; usefull values between 0.001 and 0.1?
                ampl (int): Amlitude of sine wave; should be between 0 and 255
        Returns: 
                jj (int): oscillating value between 0 and amplitude
    '''
    global f
    jj=int(((np.sin(f)+1)/2)*ampl)
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
    x=np.random.randint(0, h, 100)
    y=np.random.randint(0, w, 100)
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
    speed=cv2.getTrackbarPos('Blue', 'Processing')
    if speed==0:
        pass
    elif speed>=1:
        img[0:counter_blue_top, :, 0]+=speed
        counter_blue_top+=1
    else:
        img[counter_blue_bottom:479, :, 0]-=abs(speed)
        counter_blue_bottom-=1

'''Filter kernel for video feedback simulation'''
fb_ker_outside = 0.11
fb_ker_center = -10
feedback_kernel = np.array(
    [[fb_ker_outside, fb_ker_outside, fb_ker_outside, fb_ker_outside, fb_ker_outside],
     [fb_ker_outside, fb_ker_outside, fb_ker_outside, fb_ker_outside, fb_ker_outside],
     [fb_ker_outside, fb_ker_outside, fb_ker_center, fb_ker_outside, fb_ker_outside],
     [fb_ker_outside, fb_ker_outside, fb_ker_outside, fb_ker_outside, fb_ker_outside],
     [fb_ker_outside, fb_ker_outside, fb_ker_outside, fb_ker_outside, fb_ker_outside]])
#img = cv2.filter2D(img, -1, feedback_kernel)

''' Parameters for opencv rotation matrix function'''
(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)
def faux_feedback(angle=0, zoom=1):
    '''
    Combination of rotation and zoom simulating analog camera feedback
        Parameters: 
                angle (int): Angle of rotation
                zoom (float): zoom in (or out) 1.5<zoom>0.5
        Returns:
    To do: add modulation
    '''
    global img
    angle=cv2.getTrackbarPos('Rotation', 'Processing')
    zoom=0.01*cv2.getTrackbarPos('Zoom', 'Processing')+0.5
    M = cv2.getRotationMatrix2D((cX, cY), angle, zoom)
    rotated = cv2.warpAffine(img, M, (w, h))
    img = rotated

def reset():
    '''
    reset function to return to black image and start over synthesis
    '''
    global img, counter_blue_bottom, counter_blue_top, f
    img = np.ones((h, w, 3), np.uint8)
    counter_blue_top=0
    counter_blue_bottom=479
    f=0

BGRfilter_array=np.ones((h, w, 3), np.float16)
def color_filter():
    '''
    Postprocessing BGR color filter
    '''
    global filtered
    b_filter=cv2.getTrackbarPos('B', 'Processing')/100
    g_filter=cv2.getTrackbarPos('G', 'Processing')/100
    r_filter=cv2.getTrackbarPos('R', 'Processing')/100
    BGRfilter_array[:, :, 0]=b_filter
    BGRfilter_array[:, :, 1]=g_filter
    BGRfilter_array[:, :, 2]=r_filter
    img_asfloat=img.astype(float)
    filtered_asfloat=np.multiply(BGRfilter_array, img_asfloat)
    filtered=filtered_asfloat.astype(np.uint8) 
    

def nothing(p):
    pass

cv2.createTrackbar('Blue', 'Processing', 5, 20, blue_wf)
cv2.createTrackbar('Zoom', 'Processing', 50, 100, nothing)
cv2.createTrackbar('Rotation', 'Processing', 50, 100, nothing)
cv2.createTrackbar('B', 'Processing', 100, 100, nothing)
cv2.createTrackbar('G', 'Processing', 100, 100, nothing)
cv2.createTrackbar('R', 'Processing', 100, 100, nothing)

'''
The Synthesizer is split into two parts consisting of (so far):
    Preprocessing; the actual self modulating image synthesis containing:
            Random noise generator
            Color generator
            Simulating feedback
    Postprocessing: does not influence image modulation
            BGR-filter
'''
frame_counter = 0
while True:
    noise_gen()
    blue_wf()
    faux_feedback()
    color_filter()
    if frame_counter % 2 == 0:
        cv2.imshow('Video', filtered)
    c = cv2.waitKey(10)
    if c & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
    if c & 0xFF == ord("r"):
        reset()
    if c & 0xFF == ord("s"):
        cv2.imwrite('recordings/01.jpg', filtered)
    frame_counter += 1
