from itertools import count

import cv2
import os
import imutils

personName = 'NombrePersonaX' #Esta variable aloja el nombre de la persona a la cual pertenece las fotos para entrnar el modelo
dataPath = '/home/yorch/Control-de-Accesso-con-Reconocimiento-Facial-Basada-en-IA/DATA/'
personPath = dataPath + '/' + personName
#print(personPath)

if not os.path.exists(personPath):
    print('Carpeta Creada: ', personPath)
    os.mkdir(personPath)

cap = cv2.VideoCapture(0)

facetype = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while True:
    ret, frame = cap.read()
    if ret == False: break
    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    faces = facetype.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count),rostro)
        count = count + 1
    cv2.imshow('frame', frame)

#Cantidad de fotos que va a tomar el codigo
    k = cv2.waitKey(1)
    if k == 27 or count >= 1300: # 1300 parametro a cambiar, puede ser 500 o 100 o 1000, etc
        break

cap.release()
cv2.destroyAllWindows()