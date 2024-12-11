import face_recognition
import os
import numpy as np


if not os.path.exists("embeddings"):
    os.makedirs("embeddings")


image_paths = [os.path.join("dataset", f) for f in os.listdir("dataset")]
images = []
for image_path in image_paths:
    image = face_recognition.load_image_file(image_path)
    images.append(image)

embeddings = []
for image in images:
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    if len(face_encodings) == 1:
        embeddings.append(face_encodings[0])

np.savetxt("embeddings/embeddings.txt", embeddings)
