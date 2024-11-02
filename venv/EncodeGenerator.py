import os
import cv2
import face_recognition
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{'databaseURL':"https://faceattendancerealtime-ffe1f-default-rtdb.firebaseio.com/",
                                    'storageBucket': "faceattendancerealtime-ffe1f.appspot.com"})

# Define the path to your "images" folder
folder_path = "D:\\Projects\\face recognition using real time database\\images"

# List all items in the "images" folder
path_list = os.listdir(folder_path)
print("Images found:", path_list)

img_list = []
student_ids = []

# Loop through each image in the folder
for path in path_list:
    # Full path to the image file
    file_path = os.path.join(folder_path, path)

    # Read the image using OpenCV and add it to img_list
    img_list.append(cv2.imread(file_path))

    # Extract the student ID (filename without extension) and add it to student_ids
    student_ids.append(os.path.splitext(path)[0])

    # Define the Firebase Storage path for the image
    # Upload each image to the `images` folder in Firebase Storage
    bucket = storage.bucket()
    blob = bucket.blob(f"images/{path}")
    blob.upload_from_filename(file_path)

    # Debug print statements
    print("Uploaded:", path)
    print("Student ID:", os.path.splitext(path)[0])

# Print all student IDs for verification
print("Student IDs:", student_ids)

def findEncodings(imagesList):
     encodeList = []
     for img in imagesList:
         img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
         encode = face_recognition.face_encodings(img)[0]
         encodeList.append(encode)

     return encodeList
print("Encoding Started...")
encodeListKnown = findEncodings(img_list)
encodeListKnownWithIds = [encodeListKnown, student_ids]
print("Encoding Complete")

file = open("EncodeFile.p",'wb')
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File Saved")


