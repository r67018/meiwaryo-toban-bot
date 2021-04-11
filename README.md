# 明和寮当番bot
## 使い方
botに以下のコマンドを送信して下さい
- 今日の当番を知りたい時
  - 「今日」
  - 「きょう」
  - 「きょお」
  - 「きょー」

- 明日の当番を知りたい時
  - 「明日」
  - 「あした」
  - 「芦田愛菜」
  - 「あしだなま」

- おみくじを引く時
  - 「おみくじ」
  
- その他
  - 探してみてね

## 設定
- **UTF-8の環境で実行してください**
- **Windowsで設定する場合はWSL上で行った方がいいです**
1. このリポジトリをローカルに clone
```
git clone https://github.com/swk67018/meiwaryo-toban-bot.git
```
2. Herokuのリモートリポジトリを追加する
```
git remote add heroku HerokuのGitURL
```
3. アクセストークンとチャンネルシークレットを設定する
```
heroku config:set YOUR_CHANNEL_ACCESS_TOKEN="LineBotのアクセストークン"
heroku config:set YOUR_CHANNEL_SECRET="LineBotのチャンネルシークレット"
```
4. `setting/src`に移動し, 下のコマンドを貼り付ける,
```
g++ -c set_info.cpp information.cpp
g++ set_info.o information.o -o main
./main
```
5. 設定用のプログラムが起動するのでそれに沿って進める
6. ルートディレクトリに移動し, Git に push
```
cd ../..
git add .
git commit -m "initial setting"
git push heroku main
```
7. LineBot の Webhook URL に`HerokuのWebURL/callback` を書き込み保存

## 使用したもの
  - [Python](https://www.python.org/)
  - [Heroku](https://jp.heroku.com/)
  - [Git](https://git-scm.com/)

## フィードバック
  DMで教えてね♡
