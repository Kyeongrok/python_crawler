import re
from bs4 import BeautifulSoup
from libs.patternMatcher import findMatchedTexts

def getMatchedText(pattern, text):
    matches = re.findall(pattern, text)
    result = []
    for match in matches:
        result.append(match)
    return result

def get_row(tr):
    tds = tr.find_all('td')
    atag = str(tds[0].find('a')).split('<span class="tit_info">')

    first = ''
    try:
        first = re.compile('\t.*\t').sub('', atag[0]).split('\n')[1]
        first = first.replace('R&amp;amp;amp;amp;D ', '')
    except:
        print('----------')

    second = ''
    try:
        second = atag[1].split('</span>')[0]
        second = second.replace('R&amp;amp;D ', '')
    except:
        print('---------')
    # print(tds[1], tds[2], tds[3])

    api_id = ''
    try:
        id_a = tds[0].find('h4').find('a')['href']
        api_id = findMatchedTexts(id_a, "javascript:view\('[0-9]+")[0]
        api_id = api_id.replace("javascript:view('", "")
    except Exception as e:
        print('----api id exception -----')

    service_types = []
    try:
        service_types_spans = tds[5].find('div', {'class':'datatype'}).find_all('span')
        service_types = [span.text for span in service_types_spans ]

    except Exception as e:
        print('----- serivce types exception -------')

    return {'api_id':api_id, 'title':first, 'subtitle':second,
            'count':tds[3].text, 'service_types':service_types}


def parse(string):
    bsobj = BeautifulSoup(string, "html.parser")
    tbody = bsobj.find("table", {'class':'list rtable tablesaw'}).find('tbody')
    trs = tbody.find_all('tr')
    result = [get_row(i) for i in trs]
    return result
