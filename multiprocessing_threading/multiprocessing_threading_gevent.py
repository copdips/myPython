import urllib.request
import requests
import time
import multiprocessing
import threading
import queue

def startTimer():
    return time.time()

def ticT(startTime):
    useTime = time.time() - startTime
    return round(useTime, 3)

#def tic(startTime, name):
#    useTime = time.time() - startTime
#    print('[%s] use time: %1.3f' % (name, useTime))

def download_urllib(url):
    req = urllib.request.Request(url,
            headers={'user-agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req)
    data = res.read()
    try:
        data = data.decode('gbk')
    except UnicodeDecodeError:
        data = data.decode('utf8', 'ignore')
    return res.status, data

def download_requests(url):
    req = requests.get(url,
            headers={'user-agent': 'Mozilla/5.0'})
    return req.status_code, req.text

class threadPoolManager:
	def __init__(self,urls, workNum=10000,threadNum=20):
		self.workQueue=queue.Queue()
		self.threadPool=[]
		self.__initWorkQueue(urls)
		self.__initThreadPool(threadNum)

	def __initWorkQueue(self,urls):
		for i in urls:
			self.workQueue.put((download_requests,i))

	def __initThreadPool(self,threadNum):
		for i in range(threadNum):
			self.threadPool.append(work(self.workQueue))

	def waitAllComplete(self):
		for i in self.threadPool:
			if i.isAlive():
				i.join()

class work(threading.Thread):
	def __init__(self,workQueue):
		threading.Thread.__init__(self)
		self.workQueue=workQueue
		self.start()
	def run(self):
		while True:
			if self.workQueue.qsize():
				do,args=self.workQueue.get(block=False)
				do(args)
				self.workQueue.task_done()
			else:
				break

urls = ['http://www.ustchacker.com'] * 10
urllibL = []
requestsL = []
multiPool = []
threadPool = []
N = 20
PoolNum = 100

for i in range(N):
    print('start %d try' % i)
    urllibT = startTimer()
    jobs = [download_urllib(url) for url in urls]
    #for status, data in jobs:
    #    print(status, data[:10])
    #tic(urllibT, 'urllib.request')
    urllibL.append(ticT(urllibT))
    print('1')

    requestsT = startTimer()
    jobs = [download_requests(url) for url in urls]
    #for status, data in jobs:
    #    print(status, data[:10])
    #tic(requestsT, 'requests')
    requestsL.append(ticT(requestsT))
    print('2')

    requestsT = startTimer()
    pool = multiprocessing.Pool(PoolNum)
    data = pool.map(download_requests, urls)
    pool.close()
    pool.join()
    multiPool.append(ticT(requestsT))
    print('3')

    requestsT = startTimer()
    pool = threadPoolManager(urls, threadNum=PoolNum)
    pool.waitAllComplete()
    threadPool.append(ticT(requestsT))
    print('4')

import matplotlib.pyplot as plt
x = list(range(1, N+1))
plt.plot(x, urllibL, label='urllib')
plt.plot(x, requestsL, label='requests')
plt.plot(x, multiPool, label='requests MultiPool')
plt.plot(x, threadPool, label='requests threadPool')
plt.xlabel('test number')
plt.ylabel('time(s)')
plt.legend()
plt.show()
