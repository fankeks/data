import cv2
face_cascade_db=cv2.CascadeClassifier('E:/anaconda/Library/etc/haarcascades/haarcascade_frontalface_default.xml')
norm=[]
no=[]
for i in range (1,31):
    if i<16:
        cap = cv2.VideoCapture('E:/kyrsach/'+str(i)+'.mp4')
    else:
        cap = cv2.VideoCapture('E:/kyrsach/'+str(i)+'.mov')
    success, img = cap.read()
    
    
    img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade_db.detectMultiScale(
        img_gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    x,y,w,h=-1,-1,-1,-1
    for(x,y,w,h) in faces: continue
    if ((x==-1)|(y==-1)|(w==-1)|(h==-1)):
        print('Лицо не найдено')
       
    else:
        img=cv2.resize(img_gray[y:y+h,x:x+w],(300,300))
        
        
    if i<16:
        norm.append(img)
        cap.release()
    else:
        no.append(img)
        cap.release()
while True:
   
    cv2.imshow('Result', norm[0])
    if cv2.waitKey(1) & 0xFF==ord(' '):
        break

cv2.destroyAllWindows()