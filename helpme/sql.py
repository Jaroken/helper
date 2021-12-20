def insqllist(valuelist, doublequote = False, noquote= False):
    '''
        Turns a list of values into a single string that contains a list of strings to use in a SQL IN statement

                Parameters:
                        valuelist (list): A list of project ids
                        doublequote (bool): if True uses double quote between list items. Default, or False, is to use single quotes.
                        noquote (bool): if True do not use any quotes around itesm in list.

                Returns:
                        String (str): A string containing a SQL In list.
        '''
    str1 = " "
    z=[]
    if noquote == True:
        for x in valuelist:
            z.append(str(x)+", ")
        z.pop(-1)
        return("("+str1.join(z)+str(x)+")")
    if doublequote == True:
        for x in valuelist:
            z.append('"'+str(x)+'",')
        z.pop(-1)
        return("("+str1.join(z)+'"'+str(x)+'"'+")")
    if doublequote == False:
        for x in valuelist:
            z.append("'"+str(x)+"',")
        z.pop(-1)
        return("("+str1.join(z)+"'"+str(x)+"'"+")")
