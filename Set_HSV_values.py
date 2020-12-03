import cv2
import numpy as np

# HSV VALUSE HELP TO EXTRACT HAND FROM IMAGE (BACKGROUND REMOVEL)

# READ HSV VALUES FROM FILE
hsv_values = np.loadtxt('data/hsv_values.txt', dtype=int)
[lh, ls, lv], [uh, us, uv] = hsv_values


def nothing(x):
    pass


cap = cv2.VideoCapture(0)

# CREATE TRACKBARS
cv2.namedWindow('trackbars')
cv2.createTrackbar('Min_Hue', 'trackbars', lh, 255, nothing)
cv2.createTrackbar('Min_Saturation', 'trackbars', ls, 255, nothing)
cv2.createTrackbar('Min_Value', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('Max_Hue', 'trackbars', uh, 255, nothing)
cv2.createTrackbar('Max_Saturation', 'trackbars', us, 255, nothing)
cv2.createTrackbar('Max_Value', 'trackbars', 255, 255, nothing)
cv2.createTrackbar('RESET', 'trackbars', 0, 1, nothing)

while cap.isOpened():
    # RESET VALUES OF HSV ARRAY
    if cv2.getTrackbarPos('RESET', 'trackbars') == 1:
        # hsv_values = np.array([[0,48,80], [20, 255, 255]])
        hsv_values = np.array([[0, 90, 23], [20, 255, 255]])
        np.savetxt('data/hsv_values.txt', hsv_values)
        # cv2.waitKey(70)
        break

    _, frame = cap.read()
    # CONVERT COLOR OF IMAGE FROM BGR TO HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # COLLECT VALUES OF CURRENT TRACKBARS POSITION
    lh = cv2.getTrackbarPos('Min_Hue', 'trackbars')
    ls = cv2.getTrackbarPos('Min_Saturation', 'trackbars')
    lv = cv2.getTrackbarPos('Min_Value', 'trackbars')
    uh = cv2.getTrackbarPos('Max_Hue', 'trackbars')
    us = cv2.getTrackbarPos('Max_Saturation', 'trackbars')
    uv = cv2.getTrackbarPos('Max_Value', 'trackbars')
    hsv_values = np.array([[lh, ls, lv], [uh, us, uv]])

    # APPLY FILTER
    mask = cv2.inRange(hsv, hsv_values[0], hsv_values[1])

    # DISPLAT IMAGE
    cv2.imshow('frame', frame)

    # DISPLAY DESIRED PART OF IMAGE (uncomment to see result)
    # cv2.imshow('res',res)
    # res=cv2.bitwise_and(frame,frame,mask=mask)

    # DISPLAY BINERY IMAGE
    cv2.imshow('mask', mask)

    np.savetxt('data/hsv_values.txt', hsv_values)
    if cv2.waitKey(1) == 113 or cv2.waitKey(1) == 27:
        break
