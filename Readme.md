
# Mocren

**Mocren**: **Mo**nitor **C**ross-site and **R**eport **E**rrors via **N**etwork

個人的なサイトの死活監視ツール。

## 導入

事前に Python 3.10 / pip / Git がインストールされていることが前提。

```Shell
pip3 install requests
git clone https://github.com/lycoreco/Mocren.git
cd Mocren/
cp MocrenConfig.example.py MocrenConfig.py
```

## 設定

`MocrenConfig.py` は設定ファイルになっている。

`MENTION_TO` にはメンション先の Discord アカウントの ID を指定する。  
ID は Discord の設定から開発者モードを有効化し、自分のユーザーアイコンを右クリックで出てくる [IDをコピー] から取得できる。
`MENTION_TO = None` に設定するとメンションされない。

`WEBHOOK_URL` には Discord の Webhook URL を設定する。  
Discord の Webhook URL は別途取得すること。`https://discord.com/api/webhooks/～` のような URL になる。

## 実行

Mocren は常時起動機能を持たない。継続的に実行させたい場合は、Cron やタスクスケジューラなどに Mocren を登録する必要がある。  
以下に Cron で1分おきに Mocren を実行させる例を示す（`ubuntu` は一般ユーザー）。

```
*/1 * * * * sudo -u ubuntu /usr/bin/python3.10 /home/ubuntu/Mocren/Mocren.py
```

## License

[MIT License](License.txt)
