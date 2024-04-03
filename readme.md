# 프로젝트 이름 : 찾아라 라이징 맛집
    - 한주간 포스팅된 네이버 블로그 자료들을 크롤링하여 소개된 가게들의 이름과 위치정보를 기록한 후 각각 몇 번 소개되었는지를 기록하여 데이터베이스화 하고, 기존에 등록된 가게들의 변화와 새롭게 주목받는 점포들을 관찰한다.

# 팀원명 : 김기현, 김연중, 김인호

### 각 지역구의 맛집 크롤링
    - 네이버 블로그에서 합정, 홍대, 연남 지역구들을 각 태그별로 검색
      - 동일한 가게이름 count
      - 블로그 안의 iframe 내 가게 이름, 주소 크롤링
        -  Search_naverblog.png
        -  inner_blog.png
  ### 어려웠던 점
    - ㅇ
## 프로젝트 구현 방식
 - selenium

# 데이터 셋
  - 크롤링한 데이터
    - march_week4_Hapjung.csv
    - march_week4_Hongdae.csv
    - march_week4_Yunnam.csv
  - DB의 테이블 형태
    - Table_Hapjung.png