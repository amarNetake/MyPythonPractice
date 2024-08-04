class myself:
    def __init__(self):
        self.first="amar" 
        self.last="netake"
     
    def create_email(self):
        self.email = self.first + self.last + self.yob + '@gmail.com'

    def yob(self):
        self.yob='1996'
        self.create_email()
    
    def write_to_file(self):
        self.file1 = open("codes/myfile.txt","a")
        self.file1.write("\n"+self.email)
        self.file1.close()

if(__name__=='__main__'):
    obj=myself()
    obj.yob()
    obj.write_to_file()