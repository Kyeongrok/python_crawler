import requests, re, time
from libs.agrion.parser import parse
from threading import Thread

page_counts = 107
threads = [None] * page_counts
results = [None] * page_counts

finished_thread_count = 0

def gogo(page_idx, results):
    data = requests.post('https://www.agrion.kr/portal/dma/opendata/open/list.do', data={
        'pageIndex':page_idx,
        'pageSize':10,
        # 'dataType':'open'
    })
    res = parse(data.content)
    results[page_idx] = res
    print('thread {} finished'.format(page_idx))


for i in range(1, page_counts):
    threads[i] = Thread(target=gogo, args=(i, results))
    threads[i].start()
    print('threand {} started'.format(i))


time.sleep(30)
print(results)


result_count = sum(1 if x != None else 0 for x in results)
print(result_count)

