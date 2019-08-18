import cv2
import numpy as np

def sketch(image):
    #converting_image_to_grayscale
    img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #blurring_image_to_remove_noise
    img_blur=cv2.GaussianBlur(img_gray,(3,3),0)
    #extracting_edges
    edges=cv2.Canny(img_blur,10,80)
    #applying_threshold_inverse
    ret,mask=cv2.threshold(edges,50,255,cv2.THRESH_BINARY_INV)
    return mask

# capturing_webcam
cap=cv2.VideoCapture(0)

# constant_image_capture_from_video
while True:
    ret,frame=cap.read()
    cv2.imshow('Live_Sketch',sketch(frame))
    # Key13==ENTER_KEY
    if cv2.waitKey(1)==13:
        break

# releasing_webcam
cap.release()
# destroying_window
cv2.destroyAllWindows()