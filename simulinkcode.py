import requests as rq
import subprocess as sp
import glob
class gitcollect:

    def __init__(self,url="https://api.github.com/search/repositories?l=MATLAB&q=simulink"):
        self.clonekey=[]
        self.movelist=glob.glob("./**/*.slx",recursive=True)
        self.url=url
    def keyget(self,page=0):
        error=0
        flag=0
        a=rq.get(self.url).json()
        try:
            totalcount=a["total_count"]
        except KeyError:
            print("API LIMITED")
            flag=1
        if(flag!=1):
            repeatcount=int(totalcount/30)
            a=[]

            for i in range(page,page+10):
                a.append(rq.get(self.url+"&page=%d",i+1).json())
            for i in range(10):
                for j in range(30):
                    print("i:"+str(i)+"j;"+str(j))
                    try:
                        self.clonekey.append(a[i]["items"][j]["html_url"]+".git")
                    except KeyError:
                        print("Keyerror")
                        error+=1
                    except IndexError:
                        print("out of range")
                        error+=1
            print("error"+str(error))

    def clone(self):
        j=0
        for i in self.clonekey:
            cmd="git clone "+i+" ./test/sample"+str(j)
            sp.call(cmd.split())

    def move(self):
        for i in self.movelist:
            cmd="mv "+i+" ./test/"
            sp.call(cmd.split())

    def main(self):
        sp.call("mkdir test".split())
        for i in range(10):
            self.keyget(i*10)
            print("keyget time"+str(i))

        self.clone()
        self.move()
        print("finish")
        # self.move()

if __name__ == '__main__':
    a=gitcollect()
    a.main()
