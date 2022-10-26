
text = 'I am global!'

def foo():
    text = 'I am local!'
    print(locals())
     
foo()
print(globals())
