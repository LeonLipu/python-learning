def hello(*args,**kwargs):
    #print "this is hello function"+" brahmananda"
    # this geneirc way to handle all arguments and deafult value 
    print type(args)
    print args[1]
    prema="brahmanda"
    print '{0} is hunk'.format(prema)
    print kwargs
    print kwargs['name']


hello("koi","hota","jisiko apana",name ="lipu" ,age ="48")
