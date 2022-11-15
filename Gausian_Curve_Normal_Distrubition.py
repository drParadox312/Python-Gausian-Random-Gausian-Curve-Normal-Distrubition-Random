import matplotlib.pyplot as plot

x_axis_length = 100
x_axis_min = 0
x_axis_max = 100

skewness = 0
kurtosis = 1


# t range between 0.0 - 1.0
def get_normalized_unmodified_gausian_random(t:float) -> float:
    v = 1.0 - (1.0 - ((float(abs(0.5 - t)) - 0.5)/0.5)**2)**2
    return v

# t range between 0.0 - 1.0
# skewness range between -1.0 - 1.0
# krutosis range between 0.0 - positive infinity
def get_normalized_modified_gausian_random(t:float, skewness:float, kurtosis:float) -> float:
    skewness = min(1.0, max(-1.0, skewness))
    t = min(1.0, max(0.0, t - skewness * 0.5))
    v = 1.0 - (1.0 - ((float(abs(0.5 - t)) - 0.5)/0.5)**2)**2
    kurtosis = max(0.0, kurtosis)
    v = v**kurtosis
    return v


def draw_graph() -> None:
    x_label_range = x_axis_max - x_axis_min
    x_axis = []
    y_axis = []
    for i in range(x_axis_length):
        t = float(i) / float(x_axis_length)
        x = x_axis_min + x_label_range * t
        x_axis.append(x)
        y = get_normalized_modified_gausian_random(t, skewness, kurtosis)
        y_axis.append(y)
    plot.plot(x_axis, y_axis, color="g")
    plot.show()


while(True):
    draw_graph()

