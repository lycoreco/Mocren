
from typing import TypedDict

# テスト対象のサイトの型定義
class TestSite(TypedDict):
    name: str  # サイト名 (JSON に保存するときの ID でもあるので、一意にすること)
    url: str  # テスト対象の URL
    normal_status_code: int  # 正常時のステータスコード
    normal_response_data: str  # 正常時のレスポンスの中に含まれる文字列

# テスト対象のサイトの設定
test_sites: list[TestSite] = [
    {
        'name': 'つくみ島だより',
        'url': 'https://blog.tsukumijima.net/',
        'normal_status_code': 200,
        'normal_response_data': '<meta property="og:title" content="つくみ島だより">',
    },
    {
        'name': 'つくみ島道具箱',
        'url': 'https://tools.tsukumijima.net/',
        'normal_status_code': 200,
        'normal_response_data': '<title>つくみ島道具箱 | いろんなツールを置いてます</title>',
    },
    {
        'name': 'つくみ島道具箱 - アクセスカウンター',
        'url': 'https://tools.tsukumijima.net/dream/admin.cgi',
        'normal_status_code': 200,
        'normal_response_data': '<form action="./admin.cgi" method="post">',
    },
    {
        'name': 'つくみ島道具箱 - Twitter API のアクセストークンを確認するやつ',
        'url': 'https://tools.tsukumijima.net/twittertoken-viewer/',
        'normal_status_code': 200,
        'normal_response_data': '<title>Twitter API のアクセストークンを確認するやつ | つくみ島道具箱</title>',
    },
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
    {
        'name': 'namami',
        'url': 'https://jikkyo.tsukumijima.net/namami/',
        'normal_status_code': 200,
        'normal_response_data': '<a href="/namami/tv">テレビ</a></li><li><a href="/namami/radio">ラジオ</a></li><li><a href="/namami/bs">BS</a>',
    },
    {
        'name': 'namami - getchannels API',
        'url': 'https://jikkyo.tsukumijima.net/namami/api/v2/getchannels',
        'normal_status_code': 200,
        'normal_response_data': '<channels status="ok">',
    },
    {
        'name': 'TVTest オンラインヘルプ',
        'url': 'https://docs.tsukumijima.net/TVTest/',
        'normal_status_code': 200,
        'normal_response_data': '<title>TVTest (デジタル放送汎用視聴プログラム実装研究資料) ヘルプ - TVTest ヘルプ</title>',
    },
    {
        'name': 'site.tsukumijima.net',
        'url': 'https://site.tsukumijima.net/robots.txt',
        'normal_status_code': 200,
        'normal_response_data': 'Disallow: /',
    },
    {
        'name': 'KonomiTV API',
        'url': 'https://app.konomi.tv/api/',
        'normal_status_code': 404,
        'normal_response_data': '{"detail":"Not Found"}',
    },
    {
        'name': 'Akebi Keyless Server',
        'url': 'https://akebi.konomi.tv/',
        'normal_status_code': 404,
        'normal_response_data': '<center>Akebi Keyless Server (<a href="https://github.com/tsukumijima/Akebi" target="blank">https://github.com/tsukumijima/Akebi</a>)</center>',
    },
    {
        'name': 'shamimomo.net',
        'url': 'https://shamimomo.net/',
        'normal_status_code': 200,
        'normal_response_data': '<title>shamimomo.net</title>',
    },
    {
        'name': 'shamimomo.net - アクセスカウンター',
        'url': 'https://shamimomo.net/dream/admin.cgi',
        'normal_status_code': 200,
        'normal_response_data': '<form action="./admin.cgi" method="post">',
    },
    {
        'name': 'YouTubeMP3もどき',
        'url': 'https://receive.shamimomo.net/YouTubeMP3modoki/',
        'normal_status_code': 200,
        'normal_response_data': '<title>YouTubeMP3もどき</title>',
    },
    {
        'name': 'YouTubeMP3もどき - アクセスカウンター',
        'url': 'https://receive.shamimomo.net/dream/admin.cgi',
        'normal_status_code': 200,
        'normal_response_data': '<form action="./admin.cgi" method="post">',
    },
    {
        'name': 'YouTubeMP3もどき (Satellite Server)',
        'url': 'https://receive-satellite.shamimomo.net/YouTubeMP3modoki/',
        'normal_status_code': 200,
        'normal_response_data': '<title>YouTubeMP3もどき</title>',
    },
]
