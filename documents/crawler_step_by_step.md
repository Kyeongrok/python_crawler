# 단계별 크롤러 만들기
* 네이버 금융에서 종목별로 종목이름, 가격 수집
1. 프로젝트 만들기
2. libs package만들기
3. libs/naverFinanceCrawler.py
4. getCompanyInfo(code) 만들기 in naverFinanceCrawler.py
5. 함수의 return {"name":"", "price":""}로 만들기
6. stage.py만들기
7. stage.py에 getCompanyInfo import하기
8. 위 함수 잘 작동 되는지 print해보기
9. naver finance의 특정 종목 url복사하기
10. crawler에 import requests하기
11. request.get()으로 data받아오기
12. BeautifulSoup() import하기
13. data를 bsObj로 만들기
14. naver finance의 해당 종목 페이지로 가기
15. 뽑아내고 싶은 위치 개발자도구로 찾기
16. 개발자 도구로 찾은 위치를 .find()에 넣기
17. 원하는 데이터가 잘 찾아졌는지 print()하기
18. 원하는 영역의 데이터에서 .text로 텍스트만 뽑아내기
19. 위에서 만든 {"name":"", "price":""}에 name이 나오게 넣기
20. 종목코드표 url찾기
21. 모든 종목코드를 return하는 function을 libs에 만들기
22. []를 return하게 함수 만들기
23. 만든 libs의 함수가 잘 호출되는지 stage에서 call해보기
24. code를 수집하는 function완성하기
25. stage에서 codes에 수집한 코드들을 넣기
26. 반복문으로 하나씩 꺼내서 print하기
27. 위에서 만든 함수와 연결하기
28. 하드 코딩 되어있는 부분 parameter를 활용하게 바꾸기
29. try except로 에러 처리하기
30. 완료
