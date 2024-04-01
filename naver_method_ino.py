

def make_search_url(target_date, loc, category, page): # 선택날짜, 장소, 종류
    # 키워드
    date = target_date
    loc = loc
    food_catecory =  category

    # url 조합
    base_url = f'https://section.blog.naver.com/Search/Post.naver?pageNo={page}&rangeType=PERIOD&orderBy=sim&'
    date = f'startDate={target_date}&endDate={target_date}&'
    loc_cate = f'keyword=%23{loc}%20%23{food_catecory}'
    url_layout = base_url + date + loc_cate

    return url_layout