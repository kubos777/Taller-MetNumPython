import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def main():

    n = 72
    a = 1
    b = 1.5625
    x = 2

    h = (b-a)/n
    t = a
    func = lambda t, x: f(t, x)
    t_l, x_l = rk4_f(func, t, x, h, n)
    dx_ = []

    for i in range(0, len(t_l)):
        dx_.append(func(t_l[i], x_l[i]))

    print(dx_)

    #plt.plot(t_l, dx_)
    plt.plot(t_l, x_l)
    #Axes3D.plot_surface(X=t_l, Y=dx_, Z=x_l)
    plt.show()

def f(t, x):
    return 2 + (x - t - 1)**2


def rk4_f(f, t, x, h, n):
    t_a = t
    t_list, x_list = [], []

    for j in range(1, n+1):
        t_list.append(t)
        x_list.append(x)

        K_1 = h*f(t, x)
        K_2 = h*f(t + 0.5*h, x + 0.5*K_1)
        K_3 = h * f(t + 0.5 * h, x + 0.5 * K_2)
        K_4 = h * f(t + h, x+K_3)

        x = x + (1/6)*(K_1 + 2*K_2 + 2*K_3 + K_4)
        t = t_a + j*h
        print(j, t, x)

    return t_list, x_list

if __name__ == '__main__':
    main()
