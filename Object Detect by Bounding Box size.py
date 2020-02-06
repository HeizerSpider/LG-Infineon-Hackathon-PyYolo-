import subprocess

def main():
    file_ = open('shell_output.txt', 'w+')
    subprocess.run('./run_obj_det.sh', shell=True, stdout=file_)
    file_.close()

def reader():
    fh= open("shell_output.txt", "r")


    mylines=[]
    bbline=[]
    value=0
    for lines in fh:
        mylines.append(lines)
    # print(mylines)
    for x in range(len(mylines)):
        if mylines[x][0:6]=="person":
            bb=mylines[x+1]
            # print(bb)
            for i in bb:
                bbline.append(i)
            # print(bbline)
            for h in range(0,len(bbline)-2):
                if bbline[h]+bbline[h+1]+bbline[h+2]=="Top":
                    numbers=['0','1','2','3','4','5','6','7','8','9']
                    if bbline[h+5] not in numbers:
                        value=int(bbline[h+4])
                    elif bbline[h+6] not in numbers:
                        value=int(bbline[h+4]+bbline[h+5])
                    else:
                        value=int(bbline[h+4]+bbline[h+5]+bbline[h+6])
                # print(value)
            if value>200:
                print("Unsafe")
                status = 'Unsafe'
            else:
                print("Safe")
                status = 'Safe'
            bbline=[]
    fh.close()
    return status


if __name__=="__main__":
    main()
    reader()
