#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
print(cv2.__version__)


# In[26]:


import cv2


# In[45]:


face_cap = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
# print(face_cap.empty())
# print(video_cap.isOpened())




video_cap=cv2.VideoCapture(0)
while True :
    ret, video_data = video_cap.read()
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    faces= face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("video_live",video_data)
    # if cv2.waitKey(10)== ord("a"):
    #      break
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break
video_cap.release()        



# In[31]:


video_cap=cv2.VideoCapture(0)
print(video_cap.isOpened())


# In[32]:


ret,frame=video_cap.read()
print(ret)


# In[37]:


import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to read frame")
        break

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# In[35]:


import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
print("ret =", ret)

cap.release()


# In[34]:


import cv2
print("OpenCV imported")


# In[38]:


import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
print("Frame read:", ret)

cv2.imshow("Test", frame)
print("After imshow")

cv2.waitKey(1000)

cap.release()
cv2.destroyAllWindows()

print("Done")


# In[39]:


import cv2

cap = cv2.VideoCapture(0)

for i in range(100):
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()

print("Finished")


# In[40]:


import cv2

face_cap = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

print("Cascade loaded:", not face_cap.empty())


# In[41]:


import cv2

face_cap = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = face_cap.detectMultiScale(gray)

print("Faces found:", len(faces))

cap.release()


# In[ ]:




