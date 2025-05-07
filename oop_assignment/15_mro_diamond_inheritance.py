class A:
    def show(self):
        print("A.show() called")

class B(A):
    def show(self):
        print("B.show() called")

class C(A):
    def show(self):
        print("C.show() called")

class D(B, C):
    pass

# Create an instance of D and call show()
d = D()
d.show()   # will follow MRO to resolve method
