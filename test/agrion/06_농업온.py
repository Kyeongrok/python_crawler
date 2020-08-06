import requests, time, json
from libs.agrion.parser import parse
from threading import Thread
from libs.singleExcelSaver import save
from libs.jsonFileSaver import save as json_save

page_counts = 53
threads = [None] * page_counts
results = [None] * page_counts

finished_thread_count = 0

def gogo(page_idx, results):
    url = 'https://www.agrion.kr/portal/dma/opendata/open/list.do'
    data = requests.post(url, data={
        'pageIndex':page_idx,
        'pageSize':10,
        'dataType':'open'
    })
    res = parse(data.content)
    results[page_idx] = res
    print('thread {} finished'.format(page_idx))

for i in range(1, page_counts):
    threads[i] = Thread(target=gogo, args=(i, results))
    threads[i].start()
    print('thread {} started'.format(i))
#
time.sleep(page_counts / 3)
print(results)
result_count = sum(1 if x != None else 0 for x in results)
print(result_count)

cnt = 0
result_total = []
for result in results:
    cnt += 1
    print(cnt, end='')
    if result != None:
        print(len(result), result)
        result_total += result

json_save(result_total, '20200622.json')
