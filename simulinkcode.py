import requests as rq
import subprocess as sp
import glob


class gitcollect:

    def __init__(self,url="https://api.github.com/search/repositories?l=MATLAB&q=simulink"):
        self.clonekey=[]
        self.movelist=glob.glob("./**/**/*.mdl",recursive=True)
        self.url=url
        self.page=0

    def keyget(self,page=1):
        error=0
        flag=0
        errorcheck=None
        self.clonekey=[]
        a=rq.get(self.url+"&page={}".format(page)).json()
        try:
            totalcount=a["total_count"]
        except KeyError:
            print("API LIMITED")
            flag=1
        if(flag==0):
            for j in range(30):
                print("j;"+str(j))
                try:
                    self.clonekey.append(a["items"][j]["html_url"]+".git")
                except KeyError:
                    print("Keyerror")
                    error+=1
                except IndexError:
                    print("out of range")
                    error+=1
            print("error"+str(error))

    def clone(self):

        for i in self.clonekey:
            cmd="git clone {0} ./test/sample".format(i)+str(self.page)
            sp.call(cmd, shell=True)
            self.page+=1

    def move(self):
        for i in self.movelist:
            # cmd=["mv","-f","'"+i+"'", " './test/'"]
            cmd="mv -f {0}{1}{2} ./test/ ".format("'",i,"'")
            sp.call(cmd,shell=True)
            # print(i)

    def main(self):
        sp.call("mkdir test".split())
        for o in range(1,50):
            self.keyget(o)
            self.clone()


            #
            # self.clone()
            # # self.move()
            # print("finish")
            # self.move()

if __name__ == '__main__':
    a=gitcollect()
    a.main()

    a.move()
    # print(a.movelist)
