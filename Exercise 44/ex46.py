class parent(object):

    def altered(self):
        print "PARENT altered"


class child(parent):

    def altered(self):

        print "Child before parent"
        super(child,self).altered()
        print "Child after parent"

dad=parent()
son=child()

dad.altered()
son.altered()
