import face_recognition
import cv2
import os
import numpy as np

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
base_dir = './imgs/'

#################### Guilherme ###################

guilherme_image = face_recognition.load_image_file(os.path.join(base_dir, "gui.jpg"))
guilherme_face_encoding = face_recognition.face_encodings(guilherme_image)[0]

guilherme1_image = face_recognition.load_image_file(os.path.join(base_dir, "gui1.jpg"))
guilherme1_face_encoding = face_recognition.face_encodings(guilherme1_image)[0]

guilherme2_image = face_recognition.load_image_file(os.path.join(base_dir, "gui2.jpg"))
guilherme2_face_encoding = face_recognition.face_encodings(guilherme2_image)[0]

guilherme3_image = face_recognition.load_image_file(os.path.join(base_dir, "gui3.jpg"))
guilherme3_face_encoding = face_recognition.face_encodings(guilherme3_image)[0]

#################### Luiza ###################

luiza_image = face_recognition.load_image_file(os.path.join(base_dir, "luiza.jpg"))
luiza_face_encoding = face_recognition.face_encodings(luiza_image)[0]

luiza1_image = face_recognition.load_image_file(os.path.join(base_dir, "luiza1.jpg"))
luiza1_face_encoding = face_recognition.face_encodings(luiza_image)[0]

#################### Marcos ###################

marcos_image = face_recognition.load_image_file(os.path.join(base_dir, "marcos.jpg"))
marcos_face_encoding = face_recognition.face_encodings(marcos_image)[0]

marcos1_image = face_recognition.load_image_file(os.path.join(base_dir, "marcos1.jpg"))
marcos1_face_encoding = face_recognition.face_encodings(marcos1_image)[0]

# marcos2_image = face_recognition.load_image_file(os.path.join(base_dir, "marcos2.jpg"))
# marcos2_face_encoding = face_recognition.face_encodings(marcos2_image)[0]

marcos3_image = face_recognition.load_image_file(os.path.join(base_dir, "marcos3.jpg"))
marcos3_face_encoding = face_recognition.face_encodings(marcos3_image)[0]

#################### Odalisio ###################

oda_image = face_recognition.load_image_file(os.path.join(base_dir, "oda.jpg"))
oda_face_encoding = face_recognition.face_encodings(oda_image)[0]

oda1_image = face_recognition.load_image_file(os.path.join(base_dir, "oda1.jpg"))
oda1_face_encoding = face_recognition.face_encodings(oda1_image)[0]

oda2_image = face_recognition.load_image_file(os.path.join(base_dir, "oda2.jpg"))
oda2_face_encoding = face_recognition.face_encodings(oda2_image)[0]

oda3_image = face_recognition.load_image_file(os.path.join(base_dir, "oda3.jpg"))
oda3_face_encoding = face_recognition.face_encodings(oda3_image)[0]

oda4_image = face_recognition.load_image_file(os.path.join(base_dir, "oda4.jpg"))
oda4_face_encoding = face_recognition.face_encodings(oda4_image)[0]


#################### Smith ###################

smith_image = face_recognition.load_image_file(os.path.join(base_dir, "smith.jpg"))
smith_face_encoding = face_recognition.face_encodings(smith_image)[0]

smith1_image = face_recognition.load_image_file(os.path.join(base_dir, "smith1.jpg"))
smith1_face_encoding = face_recognition.face_encodings(smith1_image)[0]

smith2_image = face_recognition.load_image_file(os.path.join(base_dir, "smith2.jpg"))
smith2_face_encoding = face_recognition.face_encodings(smith2_image)[0]

smith3_image = face_recognition.load_image_file(os.path.join(base_dir, "smith3.jpg"))
smith3_face_encoding = face_recognition.face_encodings(smith3_image)[0]

smith4_image = face_recognition.load_image_file(os.path.join(base_dir, "smith4.jpg"))
smith4_face_encoding = face_recognition.face_encodings(smith4_image)[0]

#################### Vini ###################

vini_image = face_recognition.load_image_file(os.path.join(base_dir, "vini.jpg"))
vini_face_encoding = face_recognition.face_encodings(vini_image)[0]

vini1_image = face_recognition.load_image_file(os.path.join(base_dir, "vini1.jpg"))
vini1_face_encoding = face_recognition.face_encodings(vini1_image)[0]

#################### Thiago Rodrigo ###################

rod_image = face_recognition.load_image_file(os.path.join(base_dir, "rod.jpg"))
rod_face_encoding = face_recognition.face_encodings(rod_image)[0]

rod1_image = face_recognition.load_image_file(os.path.join(base_dir, "rod1.jpg"))
rod1_face_encoding = face_recognition.face_encodings(rod1_image)[0]

#################################################

# Create arrays of known face encodings and their names
known_face_encodings = [
    guilherme_face_encoding, guilherme1_face_encoding, guilherme2_face_encoding, guilherme3_face_encoding,
    luiza_face_encoding, luiza1_face_encoding,
    marcos_face_encoding, marcos1_face_encoding, marcos3_face_encoding, #marcos2_face_encoding
    oda_face_encoding, oda1_face_encoding, oda2_face_encoding, oda3_face_encoding, oda4_face_encoding,
    smith_face_encoding, smith1_face_encoding, smith2_face_encoding, smith3_face_encoding, smith4_face_encoding,
    vini_face_encoding, vini1_face_encoding,
]

known_face_names = [
    "Guilherme", "Guilherme", "Guilherme", "Guilherme",
    "Luiza", "Luiza",
    "Marcos",
    "Odalisio", "Odalisio", "Odalisio", "Odalisio", "Odalisio",
    "Smith", "Smith", "Smith", "Smith", "Smith",
    "Vini", "Vini",
    "Thiago Rodrigo", "Thiago Rodrigo",
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

def recognize(frame):

    # Only process every other frame of video to save time
    if process_this_frame:
        # # Resize frame of video to 1/4 size for faster face recognition processing
        # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        #
        # # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        # rgb_small_frame = small_frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video

        # Teste para depois caso fique lento
        # face_locations = face_recognition.face_locations(rgb_small_frame)
        # face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        # top *= 4
        # right *= 4
        # bottom *= 4
        # left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    return frame
