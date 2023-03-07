import numpy as np
import cv2

#starting image; resolution hxw
h = 480 
w = 480 
img = np.ones((h, w, 3), np.uint8)

#noise generator
def noise_gen():
    x=np.random.randint(0, 480, 10000)
    y=np.random.randint(0, 480, 10000)
    b=np.random.randint(0,255)
    g=np.random.randint(0,255)
    r=np.random.randint(0,255)
    img[x, y, :]=[b, g, r]

while True:
    noise_gen()
    cv2.imshow('image', img)
    c = cv2.waitKey(1)
    if c & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

