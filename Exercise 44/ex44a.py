class parent(object):

    def implicit(self):
        print "PARENT Implicit"

class child(parent):

    pass

father=parent()
son=child()

father.implicit()
son.implicit()