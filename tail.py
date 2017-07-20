import sys

if __name__=='__main__':

    for i in range(1,len(sys.argv),2):
        no_of_lines = int(sys.argv[i])
        filename =sys.argv[i+1]

        fo = open(filename,"rw+")

        lines = fo.readlines()
        lines =lines[0:len(lines)-1]

        if no_of_lines>=0:
            ans = lines[0:no_of_lines]
        else:
            ans = lines[no_of_lines:]

        print fo.name

        for line in ans:
            print line

        fo.close()