import matplotlib.pyplot as plt
# 追加部分 フォントを指定する。
plt.rcParams["font.family"] = "IPAexGothic"

plt.tick_params(labelbottom=False,
                labelleft=False,
                labelright=False,
                labeltop=False)

plt.tick_params(bottom=False,
                left=False,
                right=False,
                top=False)

plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

plt.gca().spines['bottom'].set_linewidth(1.5)

plt.gca().spines['bottom'].set_position(('data',0))
