import random

blue1 = ["#AABCDB", "#7698C3", "#487DB2"]
blue2 = ["#C0D6EA", "#A6C7E2", "#86B7DB"]

pink = ["#E0BBD0", "#D59EBE", "#CA81A9"]

red = ["#D0908F", "#BE6C6D", "#AA3A49"]

yellow = ["#EFC99B", "#E8B574", "E19D49"]

purple = ["#B5A8CA", "#9A8AB4", "#826BA2"]

rainbow = ["#6E8FB2", "#7DA494", "#EAB67A", "#E5A79A",
           "#C16E71", "#ABC8E5", "#D8A0C1", "#9F8DB8", "#D0D08A"]


def random_color(lst, num):
    return random.sample(lst, num)


if __name__ == '__main__':
    lst1 = random_color(blue1, 2)
    print(lst1)
