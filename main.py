import requests,sys,time
import threading

################################# BANNER #####################################
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
rr = '\033[39m'
colors=[r,g,y,b,m,c,w,rr]
import random
pp='''
                   _.-=-._     .-,     '''+random.choice(colors)+'''SOMETHING IS A JOKE!
                 .'       "-.,' /        '''+random.choice(colors)+'''-\_(^_^)_/-
                (          _.  <          
                 `=.____.="  `._\\  '''
for i in pp.split('\n'):
	print random.choice(colors)+i
print rr+'\n'

##############################################################################
try:link=sys.argv[1]
except:link=raw_input('Link : ')
print random.choice(colors)+"           HOST     :    "+rr,link



useragent=random.choice(open('user-agents.txt','rb').read().split('\n'))



agent={"User-Agent":useragent}
try:requests.get(link)
except:print r,"[[[[[[[[[[[[[[[[[[[[[ Host Is Down ]]]]]]]]]]]]]]]]]",rr;exit()
failed=[]
succed=[]
dirs=open('dirs.txt','rb').read().split('\n')
def scanner(i,o):
    time.sleep(1)
    ww=requests.get(link+'/'+i,headers=agent).status_code
    if ww == 200:
        succed.append( '\n      ',link+'/'+i+'           '+str(ww)+'         ')
    else:
        failed.append('\r       '+link+'/'+i+'           '+random.choice(colors)+str(ww)+'         '+rr)#sys.stderr.write(
c=0
l=float(len(dirs))
for i in dirs:
    c=c+1
    sys.stderr.write('\r'+str(float(float(c)/l))[0:4])
    t = threading.Thread(target=scanner, args=(i,i))
    t.start()
for i in succed:
    print i
