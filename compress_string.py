

def compress(input_str):
    op = ''
    currentcount = 0
    prevChar = None
    for char in input_str:
        if char!=prevChar:
            #print prevChar & its count
            if prevChar!=None:
                op = op +prevChar+str(currentcount)
            currentcount=1
        else:
            currentcount+=1

        prevChar = char

    compressed_output_str = op+prevChar+str(currentcount)
    return compressed_output_str

if __name__=='__main__':
    ip = 'abbbccddaaab'
    print compress(ip)


