# 研究計画の図を自動生成する

- こんな人たち向け
  - パワポで図を作るのはうんざり
  - Linuxじゃパワポ使えないよ！
- ファイルの説明
  - make_plan.py : プログラム本体．これを実行する．
  - plan_sample.json : jsonのサンプル．
  - plan_template.json : jsonのテンプレート．
  - setting.py : 軸の設定．インポート用．
- 使い方
  - 準備
    - テンプレートやサンプルをもとにplan.jsonを作る
      - 図の計画の矢印はplan.jsonに書いた順番に下から描画されるので書く順番は適当に変えてください
  - 実行
    - python make_plan.py