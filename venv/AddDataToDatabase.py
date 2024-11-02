import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{'databaseURL':"https://faceattendancerealtime-ffe1f-default-rtdb.firebaseio.com/"})

ref = db.reference('Students')

data={
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year":2017,
            "total_attendance":6,
            "standing":"G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"

        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year":2018,
            "total_attendance":9,
            "standing":"B",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"

        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year":2020,
            "total_attendance":7,
            "standing":"G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"

        }, "070707":
        {
            "name": "Fatima",
            "major": "A.I",
            "starting_year":2020,
            "total_attendance":9,
            "standing":"G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"

        },"242424":
        {
            "name": "Vashnavi",
            "major": "Data science",
            "starting_year":2021,
            "total_attendance":9,
            "standing":"G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"

        },





}

for key,value in data.items():
    ref.child(key).set(value)

