import random

blue1 = ["#AABCDB", "#7698C3", "#487DB2"]

blue2 = ["#C0D6EA", "#A6C7E2", "#86B7DB"]   # 浅一些

green = ["#92C6A0", "#6DBB86", "#428B69"]

pink = ["#E0BBD0", "#D59EBE", "#CA81A9"]

red = ["#D0908F", "#BE6C6D", "#AA3A49"]

yellow = ["#EFC99B", "#E8B574", "E19D49"]

purple = ["#B5A8CA", "#9A8AB4", "#826BA2"]

rainbow = ["#6E8FB2", "#7DA494", "#EAB67A", "#E5A79A",
           "#C16E71", "#ABC8E5", "#D8A0C1", "#9F8DB8", "#D0D08A"]
Macaroon = ["#ffadbb", "#fdc7cd", "#fed7da", "#c9d4f7", "#acbfeb",
            "#f6d6c3", "#fcedbe", "#f7cf83", "#ef836c", "#f8c9d5",
            "#ee84a8", "#d35b7e", "#fbf1d7", "#fad6b5", "#faadac",
            "#fcdfe5", "#daf1ee", "#b6e3e7", "#ffd5d9", "#ffc8d0",
            "#e1f9e8", "#d1e9f4", "#c2d7f3", "#778ccc", "#feceba",
            "#fe98a7", "#fd8c67", "#fdb78e", "#fef0b9", "#fad354",
            "#feb2da", "#d495e0", "#ad8fdc", "#8475c5", "#86dcf4",
            "#71bcec", "#9adbc5", "#a1dee0", "#dfde6c", "#fcc351",
            "#fd8d6e", "#fa86a9", "#eeeaeb", "#c5a6c4", "#fac4d5",
            "#fa9daf", "#b0d097", "#f7e8c9", "#ffbdb9", "#f17172",
            "#cee9dc", "#a4ceb7", "#C09f7e"]

Morandi = ["#E8D3C0", "#D89C7A", "#D6C38B", "#CFC3A9", "#849B91",
           "#E1CCB1", "#D4BAAD", "#C2CEDC", "#B0B1B6", "#E4E6E1",
           "#979771", "#91AD9E", "#686789", "#B77F70", "#E5E2B9",
           "#BEB1A8", "#A79A89", "#8A95A9", "#9FABB9", "#9AA690",
           "#91A0A5", "#99857E", "#7D7465", "#88878D", "#B4746B",
           "#E6D6D9", "#676662", "#AB545A", "#724E52", "#BCA295",
           "#AEA9A6", "#CEB797", "#9A7549", "#BCA289", "#D3D2D0",
           "#ECCED0", "#B57C82", "#F4D1D7", "#FEECD8"]


def random_color(lst, num):
    return random.sample(lst, num)


def show_color(lst):
    # 设置图形大小
    plt.figure(figsize=(10, 6))
    # 依次绘制每个颜色
    for i, color in enumerate(lst):
        plt.fill_between([i, i + 1], 0, 1, color=color)
    # 隐藏x轴和y轴的刻度
    plt.xticks([])
    plt.yticks([])


if __name__ == '__main__':
    lst1 = random_color(blue1, 2)
    print(lst1)
    import matplotlib.pyplot as plt

    show_color(blue1)
    # show_color(blue2)
    # 显示图形
    plt.show()
