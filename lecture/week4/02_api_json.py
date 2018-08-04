import json

json_str = """
{
"lastBuildDate": "Sat, 04 Aug 2018 11:02:00 +0900",
"total": 6433952,
"start": 1,
"display": 10,
"items": [
{
"title": "천안<b>에어컨</b>청소 에스그린에서 합리적으로!",
"link": "http://blog.naver.com/j0110294?Redirect=Log&amp;logNo=221326789015",
"description": "아니라서 <b>에어컨</b>이 없으면 안될 것 같더라고요 ㄱ- 그래서 오늘은 <b>에어컨</b> 청소에 대한 꿀팁을 가져왔답니다! 더 알뜰하게 오래 사용할 수 있는 방법 지금 알려드릴게요 번화한 깨닫게 하였다. 유씨가 영양이 어찌... ",
"bloggername": "래퍼의 흔들리는 블로그",
"bloggerlink": "http://blog.naver.com/j0110294",
"postdate": "20180726"

},
{
"title": "광주<b>에어컨</b>청소 행복한 하루",
"link": "http://blog.naver.com/tkfkdwjstk70?Redirect=Log&amp;logNo=221332116675",
"description": "이런날씨 속에서 제일 힐링이 되는것이바로 시원한 <b>에어컨</b>을 틀면서TV보는게 제일 크나큰 낙인것... 얼마전 <b>에어컨</b>에 문제가 생겨서광주<b>에어컨</b>청소 청소박사119라는업체에 도움을 받게 되었어요! 근데 이날 입이... ",
"bloggername": "HP바이오",
"bloggerlink": "http://blog.naver.com/tkfkdwjstk70",
"postdate": "20180803"

},
{
"title": "<b>에어컨</b>이 빛나는 밤★ 이번달 전기요금 예측해보기",
"link": "http://blog.naver.com/maybell013?Redirect=Log&amp;logNo=221330372421",
"description": "우리집에서 <b>에어컨</b>사용방법을 포스팅해보겠음! 저번 포스팅에도 썼듯 우리집 당월지침이 10691인데...... 요며칠은 밤에 <b>에어컨</b> 못끄고 자는데 이다지도 양호하다니 왜지?... (이럴리없다 의심중) 일단 우리집은... ",
"bloggername": "Hello, Maybell♥",
"bloggerlink": "http://blog.naver.com/maybell013",
"postdate": "20180801"

},
{
"title": "엘지 휘센<b>에어컨</b>설치와 시간 비용",
"link": "http://blog.naver.com/com012?Redirect=Log&amp;logNo=221330216529",
"description": "오늘은 엘지휘센<b>에어컨</b>을 설치하는 과정과 설치비시간 그리고 설치비에 대해서 포스팅을 해보도록 하겠습니다. 원래는 요즘 인기모델인 삼성의 무풍<b>에어컨</b>과 엘지휘센<b>에어컨</b>중에 고민이 많았습니다.... ",
"bloggername": "차돌이와예쁜이",
"bloggerlink": "http://blog.naver.com/com012",
"postdate": "20180731"

},
{
"title": "안산<b>에어컨</b>설치로 폭염 탈출하기!",
"link": "http://blog.naver.com/bangsilko?Redirect=Log&amp;logNo=221331179277",
"description": "요즘은 <b>에어컨</b>이 없으면 살아 갈수 없는 환경인거 같아요.<b>에어컨</b>을 자주 사용하지 않 고 선풍기로만 여름을 지내던 저희집도 더 이 상 버틸수가없어서 설치를 결심하게 됬어요ㅠ 최대한 빨리 설치를 하자는... ",
"bloggername": "♥ KATE ♥",
"bloggerlink": "http://blog.naver.com/bangsilko",
"postdate": "20180802"

},
{
"title": "이동식 미니 <b>에어컨</b> 구입하시려구요?",
"link": "http://blog.naver.com/daily__y?Redirect=Log&amp;logNo=221330621315",
"description": "이동식 미니 <b>에어컨</b>?! 안녕하세요, 꿈꾸는 세상 드림입니다. 오늘은 서울이 39도라는데 111년만에 역대... 안그래도 제 방이 끝쪽이라 거실 <b>에 어 컨</b> 바람이 하나도 안오거든요. 그냥 찜통이에요.. 그래서 제 방에... ",
"bloggername": "꿈꾸는세상",
"bloggerlink": "http://blog.naver.com/daily__y",
"postdate": "20180801"

},
{
"title": "<b>에어컨</b> 전기세 계산, 측정하기",
"link": "http://blog.naver.com/jc7083sky?Redirect=Log&amp;logNo=221330178659",
"description": "<b>에어컨</b>없이는 생활이 불가능할정도 인데요. 평균 밖에 온도는 대략.. 네 뭐 42도 정도... 실내온도는? 30도에서 32도..? 이쯤되니 거의 24시간 돌아가는 저의 <b>에어컨</b> 전기세가 걱정되더군요 -_- 그래서... ",
"bloggername": "남쪽물고기",
"bloggerlink": "http://blog.naver.com/jc7083sky",
"postdate": "20180731"

},
{
"title": "안양<b>에어컨</b>설치 싸고 빨라서 좋아",
"link": "http://blog.naver.com/d_d10vey0u?Redirect=Log&amp;logNo=221331975332",
"description": "답은 <b>에어컨</b> 밑으로 가는 것밖에 없더라구요. <b>에어컨</b>을 빵빵하게 틀어놓은 식당이나 상점을 지나갈 땐 순간적으로 시원함이 몰려와 오~하는 소리도 절로 나더라구요. 정말 못 참겠을 땐 근처 마트나 은행으로... ",
"bloggername": "딸기 샤베트 노란색 레몬에이드",
"bloggerlink": "http://blog.naver.com/d_d10vey0u",
"postdate": "20180803"

},
{
"title": "<b>에어컨</b> 자가 설치 DIY 후기 (삼성 스탠드<b>에어컨</b> 17평형)",
"link": "http://blog.naver.com/jos77?Redirect=Log&amp;logNo=221331563924",
"description": "<b>에어컨</b>을 직접 설치해보았습니다 한 여름이 무덥네요... 작년에 샀던 이동식 <b>에어컨</b>이 6월까지는 쓸만했는데 7월 되면서 30도 넘는 폭염을 견디지 못하더군요 ㅠ.ㅠ 면적이 10평(30㎡)정도 되긴하지만 경험상 그... ",
"bloggername": "허접한 보물창고",
"bloggerlink": "http://blog.naver.com/jos77",
"postdate": "20180802"

},
{
"title": "<b>에어컨</b>없이 111년만의 폭염을 견디는 일상~",
"link": "http://blog.naver.com/eye4y?Redirect=Log&amp;logNo=221332234125",
"description": "2년전 미사강변도시 입주하기전에 <b>에어컨</b>을 버리고 이사왔는데요.. 여름 끝자락에 입주해서 <b>에어컨</b> 설치를 미루다가 작년에는 그리 덥지 않아서 다급하게 <b>에어컨</b> 구입 및 설치를 미루다가 이 사태가 왔습니다... ",
"bloggername": "성주는 즐거워~~",
"bloggerlink": "http://blog.naver.com/eye4y",
"postdate": "20180803"

}
]
}
"""

json_obj = json.loads(json_str)

result = json_obj['start']
print(result, json_obj['display'])

items = json_obj['items']

for item in items:
    print(item['title'])
