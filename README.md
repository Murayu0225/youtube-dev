## YouTube Dev

YouTube APIのいろいろを試してます。

![Alt](https://repobeats.axiom.co/api/embed/e6566cf7565af1ce363bad3afb53140b17e369e1.svg "Repobeats analytics image")

### 課題

- [ ] delete.pyを完成させる
  - 現在のdelete.pyは実際は動作していない。(なぜ、YouTubeの審査を通ったかは不明笑)
  - クローンさせたら日時がその日のデータになってしまうので何度30日経過したtxtファイルの削除プログラムを実行させも消えないです。

- [ ] txtファイルに日時を入れる
  - 一つ目の課題の解決のために行います。
  - 同じ日に行うとファイル名が重なるのでハイフン等で回数を記録させます。適当に、ifとかでファイル名があるか確認&数値をループさせて空いてるのを探させようかなと思ってる。
