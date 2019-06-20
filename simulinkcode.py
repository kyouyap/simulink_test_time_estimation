import requests as rq
import subprocess as sp
url="https://api.github.com/search/repositories?l=MATLAB&q=simulink"
clonekey=[]
def keyget(key):
    a=rq.get(url).json()
    totalcount=a["total_count"]
    repeatcount=int(totalcount/30)
    a=[]

    for i in range(repeatcount):
        a.append(rq.get(url+"&page=%d",i+1).json())
    for i in range(repeatcount):
        for j in range(30):
            print("i:"+str(i)+"j;"+str(j))
            try:
                key.append(a[i]["items"][j]["html_url"]+".git")
            except KeyError:
                print("Keyerror")

def clone(key):
    for i in key:
        cmd="git clone "+i+" ."
        sp.call(cmd.split())

def main(key):
    keyget(key)
    clone(key)
    print("finish")

if __name__ == '__main__':
    main(clonekey)
