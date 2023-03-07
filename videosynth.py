import numpy as np
import cv2

#starting image; resolution hxw
h = 480 
w = 480 
img = np.ones((h, w, 3), np.uint8)

#noise generator
def noise_gen():
    '''
    Simple noise generator function
        Paramters:
        Returns:
    '''
    x=np.random.randint(0, 480, 100)
    y=np.random.randint(0, 480, 100)
    b=np.random.randint(0,255)
    g=np.random.randint(0,255)
    r=np.random.randint(0,255)
    img[x, y, :]=[b, g, r]

#blue wave generator
counter_blue=0
def blue_wf():
    global counter_blue
    img[0:counter_blue, :, 0]+=1
    counter_blue+=1
    
while True:
    #noise_gen()
    blue_wf()
    cv2.imshow('image', img)
    c = cv2.waitKey(1)
    if c & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

