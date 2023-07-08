import cv2

path="C:\\Users\\Lenovo\\Documents\\rolex.mp4"
vid=cv2.videocapture(path)

while (vid.isOpened()):
    ret,frame=vid.read()
    frame=cv2.resize(frame,(640,640))
    if ret== True :
        #type your code here 
        cv2.imshow("result",frame)
        k=cv2.waitKey(1)
        if k==ord('q'):
            break

vid.release()
cv2.destroyAllWindows()