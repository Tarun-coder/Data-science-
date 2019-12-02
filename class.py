class smartphone:

    def __init__(self,color,model,ram,camera,mfgh):
        self.color=color
        self.model=model
        self.ram=ram
        self.camera=camera
        self.mfgh=mfgh

    def info(self):
        print("Model is:",self.model)
        print("color is:",self.color)
        print("Ram is :",self.ram)
        print("Camera is:",self.camera)
        print("Manufacturer is:",self.mfgh)


    def operation(self):
        print("It make call, We can watch movies ,listen Music , Search Anything")
        

    def additional(self):
        print("It has various type of Sensor")
        print("1.Gyroscope , 2. FingerPrint sensor , 3.Eye detection , 4.Face Recognition")


phone_1 = smartphone("red","q1","2Gb","5mpx","MI")
phone_1.info()
phone_1.operation()
print("--------------------------------------------Additional Features------")
phone_1.additional()



        

