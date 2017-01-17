#I understand inheritance
class Parent(object): #In example, they put Object inside this, I wonder
#If I can simply leave this as blank?
#Tell me Sanjay
    def implicit(self):
        print "This is parent"

class Child(Parent):
    def implicit(self):
        print "This is child"
        super(Child,self).implicit()
        print "This Child, after altering"


class Other(object):
    def overTop(self):
        print "Other override"
    def implicitTop(self):
        print "Other Implicit"
    def altered(self):
        print "Other altered"

class Children(object):
    def __init__(self):
        self.other = Other() # Okay this is calling from Other and creating instance
        #of the class
    def implicitTop(self):
        self.other.implicitTop()
    def overTop(self):
        print "Over ride"
    def altered(self):
        print "Before, Other altered"
        self.other.altered()
        print "After, Other altered"





def main():
#    d = Parent()
#    c= Child()
#    print d.implicit()
#    print c.implicit()
    Sanjay = Children()
    Sanjay.implicitTop()
    Sanjay.overTop()
    Sanjay.altered()
if __name__ == '__main__':
    main()
