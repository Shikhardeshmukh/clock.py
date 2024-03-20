class student :
    #properties
    name = ""
    rollnumber = 2112

    #methods
    def getdata(self):
        self.name = input("enter name:")
        self.rollnumber = int(input("enter rollnumber:"))

    def setdata(self,N,R) :
        self.name = N
        self.rollnumber = R
    def showdata(self) :
        print("students name is",self.name)
        print("student roll number is",self.rollnumber)

s1 = student()
s2 = student()

s1.getdata()    #in getdata we get the data
s2.setdata("john",4675)  #in setdata we set or write data here only.

s1.showdata()   # show data shows the data given . printing data written in s1 getdata
s2.showdata()