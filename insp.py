import cv2
import numpy as np

def start():
    # Resolution of the videoq
    down_scale = 4
    h = 1920 // down_scale
    w = 1920 // down_scale

    # This can be set to False so that every frame will be
    # shown. In this case the video is flickery for an
    # unknown reason.
    only_even_frames = True

    # Amount to rotate the image every frame. Unit is degrees.
    angle = 0.1

    # Amount to zoom into the image every frame.
    # Can be less than 1 for zooming out.
    zoom = 0.995

    # The number of randomly generated pixels to
    # place at random locations every frame.
    num_noise = 100

    # The area where the random noise pixels will
    # be contained within
    noise_area_size = 10

    # Value for kernel except for the center
    ker_outside = 0.11
    ker_center = -10

    kernel = np.array(
        [[ker_outside, ker_outside, ker_outside, ker_outside, ker_outside],
         [ker_outside, ker_outside, ker_outside, ker_outside, ker_outside],
         [ker_outside, ker_outside, ker_center, ker_outside, ker_outside],
         [ker_outside, ker_outside, ker_outside, ker_outside, ker_outside],
         [ker_outside, ker_outside, ker_outside, ker_outside, ker_outside]])

    # The numpy array for the image that will be
    # used for every frame
    img = np.zeros((h, w, 3), np.uint8)

    # Used for parameters for opencv rotation matrix function
    (h, w) = img.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # Only used to check if the current
    # frame is even
    counter = 0

    while True:
        # Both the rotation and the zoom
        M = cv2.getRotationMatrix2D((cX, cY), angle, zoom)
        rotated = cv2.warpAffine(img, M, (w, h))
        img = rotated

        # Generate the x coordinates for the location
        # of the noise pixels
        x_low = 0 + (w // 2) - noise_area_size
        x_high = w - (w // 2) + noise_area_size
        x = np.random.randint(x_low, x_high, num_noise)

        # Generate the y coordinates for the location
        # of the noise pixels
        y_low = 0 + (h // 2) - noise_area_size
        y_high = h - (h // 2) + noise_area_size
        y = np.random.randint(y_low, y_high, num_noise)

        # Determines which random color the noise pixels
        # will be for this frame.
        r = np.random.randint(0, 256)
        g = np.random.randint(0, 256)
        b = np.random.randint(0, 256)

        # Add the random noise pixels to the image.
        img[y, x, :] = [r, g, b]

        # Apply the kernel to the image
        img = cv2.filter2D(img, -1, kernel)

        if only_even_frames:
            if counter % 2 == 0:
                cv2.imshow("test", img)
        else:
            cv2.imshow("test", img)

        # Increase this number to slow down the
        # live video. Decrease (min of 1) to increase
        # the speed of the video.
        c = cv2.waitKey(10)

        # Press the q key to stop the video
        if c & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

        counter += 1

if __name__ == "__main__":
    start()
    