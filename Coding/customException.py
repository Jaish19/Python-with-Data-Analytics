


def testingCustom(n):
    if n <0:
        raise JaiException("hey")
    else:
        print "number which you entered is", n


class JaiException(Exception):
    def __init__(self,dErrorArguements):
        Exception.__init__(self,"my exception was raised with arguments {0}")
        self.dErrorArguments = dErrorArguements

    def __str__(self):
        return "Jai"


if __name__ == '__main__':
    print "inside main"
    testingCustom(-9)




# CUSTOM_ERROR Exception

class JaiError(Exception):
    def __init__(self,run):
        self.run=run


try:
    if 5==8:
        print("its fine one")  
    else:
        raise JaiError("custom Error")     
except JaiError:
    print("welcome to error spot")


    

