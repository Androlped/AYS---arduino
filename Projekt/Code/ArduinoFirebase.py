from pickle import FALSE
import serial.tools.list_ports
import time
import pyrebase

firebaseConfig={
  'apiKey': "AIzaSyAb60puRZRZLgtstDoW_OuGWqOV5DK5UXg",
  'authDomain': "arduinoconsole-d6a04.firebaseapp.com",
  'databaseURL': "https://arduinoconsole-d6a04-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "arduinoconsole-d6a04",
  'storageBucket': "arduinoconsole-d6a04.appspot.com",
  'messagingSenderId': "41596064593",
  'appId': "1:41596064593:web:7d79d9b95688657b73b970"
}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

#Database

#Create
data1={
    'toBeEvaluated':False}
data2={
    'toBeEvaluated':True}
data3={
    'toBeEvaluated':False}

#db.child("Students").push(data)
db.child("Students").child("Anders").set(data1)
db.child("Students").child("Kristoffer").set(data2)
db.child("Students").child("Valentin").set(data3)

#-------------------Serial ---------------
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("select Port: COM")

for x in range(0,len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])

serialInst.baudrate = 115200
serialInst.port = portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        #print("Here") 
        print(packet.decode('utf').rstrip('\n\r'))
        #print("Here")


        """
        if(notDataFire):
            if "Anders" in packet.decode('utf').rstrip('\n'):
                print("It's Alive")
                studentToBeEvaluated="Anders"
            if "Kristoffer" in packet.decode('utf').rstrip('\n'):
                print("It's Alive")
                studentToBeEvaluated="Kristoffer"
            if "Valentin" in packet.decode('utf').rstrip('\n'):
                print("It's Alive")
                studentToBeEvaluated="Valentin"
            print(studentToBeEvaluated)
            print(type(studentToBeEvaluated))
        else:
        """
        studentToBeEvaluated=packet.decode('utf').rstrip('\n\r')
        students=db.child("Students").get()
        for student in students.each():
            if studentToBeEvaluated==student.key(): #these are not same type?

                db.child("Students").child(student.key()).update({'toBeEvaluated':True})
            
           # else: 
            #    db.child("Students").child(student.key()).update({'toBeEvaluated':False})
            db.child("Students").update({'arduinoInput':studentToBeEvaluated})





"""


serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf').rstrip('\n'))
        studentToBeEvaluated=packet.decode('utf').rstrip('\r\n')
        students=db.child("Students").get()
        for student in students.each():
            if studentToBeEvaluated==student.key():
                db.child("Students").child(student.key()).update({'toBeEvaluated':True})
                
            else: 
                db.child("Students").child(student.key()).update({'toBeEvaluated':False})
            db.child("Students").update({'arduinoInput':studentToBeEvaluated})

"""


