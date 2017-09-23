class parent(object):

    def ovverrides(self):
        print "PARENT Overrides"

class child(parent):

    def ovverrides(self):
        print "CHILD Overrides"


father=parent()
son=child()

father.ovverrides()
son.ovverrides()