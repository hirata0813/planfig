import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
import json

import setting

# 範囲内に存在する日時を列挙
def daterange(start, end):
    for n in range((end - start).days):
        yield start + timedelta(n)

# 矢印とそのテキストを作る
def make_arrow(text, start, end, y):
    start_point = [start, y]
    end_point = [end, y]

    plt.annotate('', xy=end_point, xytext=start_point,
                    arrowprops=dict(shrink=0, width=0.5, headwidth=4, 
                                    headlength=4, connectionstyle='arc3',
                                    facecolor='k', edgecolor='k')
                    )

    t = plt.text(start_point[0] + (end_point[0] - start_point[0]) / 2, start_point[1] + 5, text, size=16, ha='center')
    t.set_bbox(dict(facecolor='white', alpha=1, edgecolor='white'))

# y座標上限の初期値
y_max = 100

# jsonファイルの読み込み
f = open('plan.json', 'r')

# jsonを辞書に変換
plan_dict = json.load(f)

# 日時の範囲
start_range = datetime.strptime(plan_dict['range']['start'], '%Y-%m-%d').date()
end_range = datetime.strptime(plan_dict['range']['end'], '%Y-%m-%d').date()

# 1本目のy座標
y = 10

# 計画のプロット
for p in plan_dict: 
    if 'plan' in p:
        plan_title = plan_dict[p]['title']
        plan_start = datetime.strptime(plan_dict[p]['start'], '%Y-%m-%d').date()
        plan_end = datetime.strptime(plan_dict[p]['end'], '%Y-%m-%d').date()

        make_arrow(plan_title, plan_start, plan_end, y)

        y += 15
        if y >= y_max * 0.8:
            y_max = y

# 始点の縦線
plt.plot([start_range, start_range], [0,y_max], lw=1.5, color="k")
# 終点
# plt.plot([end_range, end_range], [0,y_max], lw=1.5, color="k")

# 始点のx月のラベル
plt.text(start_range - timedelta(5), -(y_max * 0.07), '{}月'.format(start_range.month), size=13)

# x軸の両端用のオフセット
date_offset = timedelta(7)

# x軸の範囲
plt.xlim(start_range - date_offset, end_range + date_offset*3)

# 範囲内のx月のラベルと点線
for d in daterange(start_range, end_range):
    if d.day == 1:
        plt.plot([d, d], [-y_max * 0.1,y_max], ls=":", lw=1.0, color="k")
        plt.text(d + timedelta(12), -(y_max * 0.07), '{}月'.format(d.month), size=13)

# イベントのプロット
for p in plan_dict: 
    if 'event' in p:
        event_title = plan_dict[p]['title']
        event_date = datetime.strptime(plan_dict[p]['date'], '%Y-%m-%d').date()

        plt.plot([event_date, event_date], [0,y_max], lw=1.5, color="k")
        plt.text(event_date, y_max + 5, event_title, size=13, ha='center')

# y軸の範囲
plt.ylim(-(y_max * 0.2), y_max)

# 表示
plt.show()