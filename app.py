# Import necessary libraries
import cv2
import face_recognition
import numpy as np
import os
import json
from datetime import datetime

# Load the embeddings
embeddings = np.loadtxt("embeddings/embeddings.txt")

# Initialize the camera
cap = cv2.VideoCapture(0)

# Load the attendance log
if not os.path.exists("attendance.json"):
    with open("attendance.json", "w") as f:
        json.dump({}, f)
with open("attendance.json", "r") as f:
    attendance = json.load(f)
    
# Recognize the faces and mark attendance
while True:
    ret, frame = cap.read()
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(embeddings, face_encoding)
        if True in matches:
            index = matches.index(True)
            name = "user_" + str(index+1)
            if name not in attendance:
                attendance[name] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("attendance.json", "w") as f:
                    json.dump(attendance, f)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

