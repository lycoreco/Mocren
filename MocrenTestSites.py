
from typing import TypedDict

# テスト対象のサイトの型定義
class TestSite(TypedDict):
    name: str  # サイト名
    url: str  # テスト対象の URL
    normal_status_code: int  # 正常時のステータスコード
    normal_response_data: str  # 正常時のレスポンスの中に含まれる文字列

# テスト対象のサイトの設定
test_sites: list[TestSite] = [
    {
        'name': '天気予報 API (livedoor 互換)',
        'url': 'https://weather.tsukumijima.net/',
        'normal_status_code': 200,
        'normal_response_data': '<title>天気予報 API（livedoor 天気互換）</title>',
    },
    {
        'name': '天気予報 API (livedoor 互換) - API (HTTP)',
        'url': 'http://weather.tsukumijima.net/api/forecast/city/400040',
        'normal_status_code': 200,
        'normal_response_data': '"title": "福岡県 久留米 の天気",',
    },
    {
        'name': '天気予報 API (livedoor 互換) - API (HTTPS)',
        'url': 'https://weather.tsukumijima.net/api/forecast/city/400040',
        'normal_status_code': 200,
        'normal_response_data': '"title": "福岡県 久留米 の天気",',
    },
    {
        'name': 'ニコニコ実況 過去ログ API',
        'url': 'https://jikkyo.tsukumijima.net/',
        'normal_status_code': 200,
        'normal_response_data': '<title>ニコニコ実況 過去ログ API</title>',
    },
    {
        'name': 'ニコニコ実況 過去ログ API - XML API',
        'url': 'https://jikkyo.tsukumijima.net/api/kakolog/jk1?starttime=1606431600&endtime=1606432500&format=xml',
        'normal_status_code': 200,
        'normal_response_data': '<chat thread="1606417201" no="2750" vpos="1440040" date="1606431601" mail="184" user_id="mmJyd4lCsV6e3loLXR0QvZnlnFI" premium="1" anonymity="1" date_usec="373180">六甲おろし歌って</chat>',
    },
    {
        'name': 'ニコニコ実況 過去ログ API - JSON API',
        'url': 'https://jikkyo.tsukumijima.net/api/kakolog/jk1?starttime=1606431600&endtime=1606432500&format=json',
        'normal_status_code': 200,
        'normal_response_data': '{"chat":{"thread":"1606417201","no":"2750","vpos":"1440040","date":"1606431601","mail":"184","user_id":"mmJyd4lCsV6e3loLXR0QvZnlnFI","premium":"1","anonymity":"1","date_usec":"373180","content":"六甲おろし歌って"}}',
    },
]
