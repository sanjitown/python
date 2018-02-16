from list import lists
import requests,time
import threading
def save(url,string):
    r=requests.get(url,stream=True)
    with open(string,'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)
def run():
    if __name__ == "__main__":
        bath_url=lists.split()
        head=''
        urls=[]
        for i in bath_url:
            url=head+i
            urls.append(url)

    threads=[]
    for i,bath in enumerate(urls):
        string = 'G:\p\\'+str(i)+ '.jpg'
        t=threading.Thread(target=save, args=(bath,string))
        threads.append(t)
    for j in range(1,20):
        for i in range(10*j,10*j+10):
            threads[i].start()
        for i in range(10*j,10*j+10):
            threads[i].join()
        #time.sleep(1)

run()
