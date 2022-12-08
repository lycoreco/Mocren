#!/usr/bin/env python3

import argparse
import datetime
import json
import pathlib
import requests
import shutil
import sys

from MocrenConfig import MENTION_TO, WEBHOOK_URL
from MocrenTestSites import test_sites


# 前回のデータを保存する JSON のパス
JSON_PATH = pathlib.Path(sys.argv[0]).parent / 'Mocren.json'

# バージョン情報
VERSION = '1.0.0'


# Discord に通知を投げる関数
def SendDiscord(message: str):
    requests.post(WEBHOOK_URL, json={
        'username': 'Mocren',
        'content': (f'<@{MENTION_TO}> ' if MENTION_TO is not None else '') + message,  # メンション先を設定
    })


def main():

    # ターミナルの横幅
    # conhost.exe だと -1px しないと改行されてしまう
    terminal_columns = shutil.get_terminal_size().columns - 1

    # 引数解析
    parser = argparse.ArgumentParser(
        description='Mocren: Monitor Cross-site and Report Errors via Network',
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument('-v', '--version', action='version', help='バージョン情報を表示する', version='Mocren version ' + VERSION)
    parser.parse_args()

    print('=' * terminal_columns)
    print('***** Mocren *****')
    print('=' * terminal_columns)

    # まだ JSON がなければ初期値を設定
    if JSON_PATH.exists() is False:
        initial_save_data = {'LastUpdatedAt': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}
        for test_site in test_sites:
            initial_save_data[test_site['name']] = True  # 初期値は True (テスト成功)
        with open(JSON_PATH, mode='w', encoding='utf-8') as fp:
            json.dump(initial_save_data, fp, ensure_ascii=False, indent=4)

    # 今回 JSON に保存するデータが入る辞書
    with open(JSON_PATH, mode='r', encoding='utf-8') as fp:
        save_data = json.load(fp)

    # 前回の更新時刻
    print(f'Last Updated Time : {save_data["LastUpdatedAt"]}')
    print(f'Current Time      : {datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")}')
    print('-' * terminal_columns)

    for test_site in test_sites:

        # ---------- テスト開始 ----------

        # テストが成功したときのみ True にする
        save_data[test_site['name']] = False

        # テスト対象のサイトにリクエスト
        ## リダイレクトはフォローしない
        ## タイムアウトは 10 秒
        try:
            response = requests.get(test_site['url'], allow_redirects=False, timeout=10)

        # 接続がタイムアウトになった
        except requests.exceptions.Timeout:

            # 前回のテストが正常だった場合のみ通知
            if save_data[test_site['name']] is True:
                SendDiscord(f'{test_site["name"]} ({test_site["url"]}) で ⚠**Timeout Error**⚠ が発生しています。')

            print(f'{test_site["name"]}: Timeout Error')
            continue

        # 接続がエラーになった
        except requests.exceptions.ConnectionError:

            # 前回のテストが正常だった場合のみ通知
            if save_data[test_site['name']] is True:
                SendDiscord(f'{test_site["name"]} ({test_site["url"]}) で ⚠**Connection Error**⚠ が発生しています。')

            print(f'{test_site["name"]}: Connection Error')
            continue

        # テスト対象のサイトのステータスコードが正常時と一致しない
        if response.status_code != test_site['normal_status_code']:

            # 前回のテストが正常だった場合のみ通知
            if save_data[test_site['name']] is True:
                SendDiscord(f'{test_site["name"]} ({test_site["url"]}) で ⚠**HTTP Error {response.status_code}**⚠ が発生しています。')

            print(f'{test_site["name"]}: HTTP Error {response.status_code} ({test_site["normal_status_code"]} was expected)')
            continue

        # テスト対象のサイトのレスポンスが正常時のレスポンスデータの一部と一致しない
        if test_site['normal_response_data'] not in response.text:

            # 前回のテストが正常だった場合のみ通知
            if save_data[test_site['name']] is True:
                SendDiscord(f'{test_site["name"]} ({test_site["url"]}) で ⚠**Response Data Error**⚠ が発生しています。')

            print(f'{test_site["name"]}: Response Data Error (HTTP status code: {response.status_code}))')
            continue

        # ---------- テスト終了 ----------

        # ここまでのテストに通過していれば、成功している
        save_data[test_site['name']] = True

        # 前回のテストが失敗だった場合のみ通知
        if save_data[test_site['name']] is False:
            SendDiscord(f'{test_site["name"]} ({test_site["url"]}) が復旧しました。')

        print(f'{test_site["name"]}: Success (HTTP status code: {response.status_code})')
        print('-' * terminal_columns)

    # ---------- 後処理 ----------

    # 前回の更新時刻を更新
    save_data['LastUpdatedAt'] = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    # 次回実行時用にデータを保存しておく
    with open(JSON_PATH, mode='w', encoding='utf-8') as fp:
        json.dump(save_data, fp, ensure_ascii=False, indent=4)

    print('Completed.')
    print('=' * terminal_columns)


if __name__ == '__main__':
    main()
