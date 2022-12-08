
# Mocren

📢 **Mocren**: **Mo**nitor **C**ross-site and **R**eport **E**rrors via **N**etwork.

> 個人的に運営している各サイトの死活監視ツール。  
> もしほかで使う場合は、適宜テスト対象のサイトの定義を変更すること。

## 導入

事前に Python 3.10 / pip / pipenv / Git がインストールされていることが前提。

```Shell
git clone https://github.com/lycoreco/Mocren.git
cd Mocren/
cp MocrenConfig.example.py MocrenConfig.py
PIPENV_VENV_IN_PROJECT="true" pipenv sync
```

## 設定

`MocrenConfig.py` は設定ファイルになっている。

`MENTION_TO` にはメンション先の Discord アカウントの ID を指定する。  
ID は Discord の設定から開発者モードを有効化し、自分のユーザーアイコンを右クリックで出てくる [IDをコピー] から取得できる。
`MENTION_TO = None` に設定するとメンションされない。

`WEBHOOK_URL` には Discord の Webhook URL を設定する。  
Discord の Webhook URL は別途取得すること。`https://discord.com/api/webhooks/～` のような URL になる。

`MocrecTestSites.py` には、正常に稼働しているかテストする、各サイトの定義を記述する。  
詳細は型定義を参照のこと。

## 実行

Mocren は常時起動機能を持たない。継続的に実行させたい場合は、Cron やタスクスケジューラなどに Mocren を登録する必要がある。  
以下に Cron で5分おきに Mocren を実行させる例を示す (`ubuntu` は一般ユーザー)。

```
*/5 * * * * /home/ubuntu/Mocren/.venv/bin/python /home/ubuntu/Mocren/Mocren.py
```

## License

[MIT License](License.txt)
