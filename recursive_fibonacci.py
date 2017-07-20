
opdict=None  #dictionary for storing fibonacci values of each length
def fab(length):

    global opdict
    if opdict == None:
        opdict={}

    if length == 1:
        opdict[length]=1
        return 1
    elif length ==0:
        return 0
    fn_1 = fab(length-1)
    fn_2 = fab(length-2)
    if length-1 not in opdict:
        opdict[length-1]=fn_1

    if length-2 not in opdict:
         opdict[length-2]=fn_1

    val =  fn_1+fn_2
    return val



if __name__=='__main__':

    length =7


    val =fab(length)

    opdict[length]=val
    #deleting the extra number at 0th index
    del opdict[0]

    #storing the values in opdict in a list series
    series =[]
    for key in opdict:
        series.append(opdict[key])

    print series