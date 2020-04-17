a = input("Enter number 1__:")
b = input("Enter number 2__:")
c = input("Enter number 3__:")

def asortD():
    if a > b:
        if a > c:
            print(a+"__Is the largerst")
        if b > c:
            print(b+"__Is the Second largest")
            print(c+"__Is the smallest")
        else:
            print(c+"__Is the Second largest")
            print(b+"__Is the smallest")
#   $ b sort
def bsortD():
    if b > a:
        if b > c :
            print(b+"__Is the largerst")
        if a > c:
            print(a+"__Is the Second largest")
            print(c+"__Is the smallest")
        else:
            print(c+"__Is the Second largest")
            print(a+"__Is the smallest")
      
def csortD():
    if c > a:
        if c > b:
            print(c+"__Is the largerst")
        if a > b:
            print(a+"__Is the Second largest")
            print(b+"__Is the smallest")
        else:
            print(b+"__Is the Second largest")
            print(a+"__Is the smallest")

if a > b:
    if a > c:
        asortD()
if b > a:
    if b > c:
        bsortD()
if c > a:
    if c > b:
        csortD()
