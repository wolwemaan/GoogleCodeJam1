import re
#
# Work in progress. work with 3 of the 4 test data
# However two problems exist :
# a> incorrect count in testcase 3
# b> not counting more than one - once fixed, this may help with (a)

# 1 1 0 0 3
s ="IiOioIoO"
#s ="IIOiOo"
#s ="IoiOiO"
#s ="io"
#s ="IiOIOIoO"
m = 0
l = None
l = re.findall(r'(i.*o)+?', s)
if l:
    print("io", len(l))
    m+=len(l)
l = None
l = re.findall(r'(I.*o)+?', s)
if l:
    print("Io", len(l))
    m+=len(l)
l = None
l = re.findall(r'(i.*O)+?', s)
if l:
    print("iO", len(l))
    m+=len(l)
l = None
l = re.findall(r'(I.*O)+?', s)
if l:
    print("IO", len(l))
    m+=len(l)
if m == (len(s) / 2):
    print ("legit")
else:
    print ("??")


#for t in l:
#    print (t)
#if l:
#    print("Hello World!", len(l) )
