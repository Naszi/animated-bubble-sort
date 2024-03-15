import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def double_short_animation(data):
    n = len(data)
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(n), data, color='red')

    def update_fig(data, rects):
        for rect, val in zip(rects, data):
            rect.set_height(val)

    anim = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects,), frames=bubble_sort_generator(data),
                                   repeat=False, blit=False, interval=100)
    plt.show()


def bubble_sort_generator(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                yield data.copy()


# Példa adatok
data = np.random.randint(1, 150, 50)

# Buborékrendezés animálása
double_short_animation(data)