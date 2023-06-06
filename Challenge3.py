class Student:
    def __init__(self):
        self._name = ""
        self._rollNumber = ""

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setRollNumber(self, rollNumber):
        self._rollNumber = rollNumber

    def getRollNumber(self):
        return self._rollNumber
student = Student()
student.setName("Diksha Avachare")
student.setRollNumber("23")

print(student.getName())       
print(student.getRollNumber())  
