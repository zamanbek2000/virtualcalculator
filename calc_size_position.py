import cv2
import numpy as np
import addon_function as my

values = np.loadtxt('data/values.txt', int)
x = values[0]
y = values[1]
h = values[2]
w = values[3]


def nothing(x):
    pass


cap = cv2.VideoCapture(0)

# CREATE TRACKBARS
cv2.namedWindow('trackbars')
# cv2.createTrackbar('r','trackbars',400,800,nothing)
cv2.createTrackbar('x', 'trackbars', x, 800, nothing)
cv2.createTrackbar('y', 'trackbars', y, 600, nothing)
cv2.createTrackbar('h', 'trackbars', h, 200, nothing)
cv2.createTrackbar('w', 'trackbars', w, 200, nothing)
cv2.createTrackbar('reset', 'trackbars', 0, 1, nothing)

while cap.isOpened():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (800, 600))

    # GET VALUES OF EACH TRACKBARS
    # r=cv2.getTrackbarPos('r','trackbars')
    x = cv2.getTrackbarPos('x', 'trackbars')
    y = cv2.getTrackbarPos('y', 'trackbars')
    h = cv2.getTrackbarPos('h', 'trackbars')
    w = cv2.getTrackbarPos('w', 'trackbars')

    # FOR RESET
    if cv2.getTrackbarPos('reset', 'trackbars') == 1:
        x, y, h, w = 485, 20, 50, 65

    # cv2.line(frame,(r,0),(r,600),(0,0,255))

    values = [(x, y, h, w)]

    # DRAW CALC ON FRAME
    frame = my.draw_calc(frame, 15, -12)

    # SAVE VALUES OF X,Y,H,W
    np.savetxt('data/values.txt', values)

    if cv2.getTrackbarPos('reset', 'trackbars') == 1:
        break

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
