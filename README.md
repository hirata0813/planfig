# 研究計画の図を自動生成する

- こんな人たち向け
  - パワポで図を作るのはうんざり
  - Linuxじゃパワポ使えないよ！
- 使用したライブラリ
  - numpy
  - matplotlib
  - datetime
  - json
- ファイルの説明
  - make_plan.py : プログラム本体．これを実行する．
  - plan_sample.json : jsonのサンプル．
  - plan_template.json : jsonのテンプレート．
  - setting.py : 軸の設定．インポート用．
- 使い方
  - 準備
    - テンプレートやサンプルをもとにplan.jsonを作る．
      - range: 図に描画する範囲(x軸のもとになる)
      - plan: 計画の項目
      - event: イベント
      - 図の計画の矢印はplan.jsonに書いた順番に下から描画されるので書く順番は適当に変えてください．
    - matplotlibの日本語対応
      - matplotlibは日本語に対応させておいてください．豆腐が出ます．
      - 参考
        - https://qiita.com/yniji/items/3fac25c2ffa316990d0c
  - 実行
    - python make_plan.py
  - 保存
    - 実行するとプロットしたグラフが出るのでウィンドウの大きさをいい感じに変更して保存ボタンで保存する．