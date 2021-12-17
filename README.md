# YoutubeMemberAlert
Gメールに届いた内容からメンバー限定配信をチェック


## 導入方法
- https://plaza.rakuten.co.jp/redstoneteikou/diary/202007280000/
- 対象チャンネルのメンバー加入必須
- メール本文の検索構文を工夫すれば通常配信の検知も並列して可能

* 設定
  * config.pyに記載してあげてください
  * config.txtには配信者さんのuser_idを記載。
  * アラート音はsample.wavを置き換えれば自由に調整できます
* 付属のバッチファイル叩けば実行してくれます
* タスクスケジューラに5～15分に一度指定をしておくと便利


## 実行してもダメな時は
* exist.txtの数値を0にしてみてください
* 改行無し


## 関連プロジェクト
ツイキャス通知
- https://github.com/sokomin/TwicasAutoAlert


