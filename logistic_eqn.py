import numpy as np
import matplotlib.pyplot as plt


def logistic_eqn(x, a):
    return a * x * (1 - x)


if __name__ == "__main__":
    # dx/dt = ax(1 - x)
    # 横軸: t, 縦軸: x について、各点における接線をベクトル場として描画する
    a_ = [1.0, 2.0, 4.0, 8.0]
    x = np.linspace(-1, 2, 20)
    t = np.linspace(-1, 2, 20)
    X, T = np.meshgrid(x, t)

    fig = plt.figure(figsize=(18, 18))
    for n, a in enumerate(a_):
        DX = logistic_eqn(X, a)
        DT = np.ones_like(T)
        M = np.hypot(DX, DT)
        DX /= M
        DT /= M

        # Plot
        ax = fig.add_subplot(4, 2, 2 * n + 2)
        ax.quiver(T, X, DT, DX, color="black")
        # ax.quiver(T, X, DT, DX, M, pivot="mid", color="black")
        ax.set_xlabel("t")
        ax.set_ylabel("x")
        ax.set_xlim(-1, 2)
        ax.set_ylim(-1, 2)
        ax.set_title(f"dx/dt = ax(1 - x): a = {a}")

        # x = 0, 1 に水平線を描画
        ax.hlines(0, -1, 2, "r", linestyles="--")
        ax.hlines(1, -1, 2, "r", linestyles="--")

        ax = fig.add_subplot(4, 2, 2 * n + 1)
        y = logistic_eqn(x, a)
        ax.plot(x, y, "k")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_xlim(-1, 2)
        ax.set_ylim(-1, 2)
        ax.set_title(f"f(x) = ax(1 - x): a = {a}")
        ax.hlines(0, -1, 2, "b", linestyles="--")
        ax.vlines(0, -1, 2, "r", linestyles="--")
        ax.vlines(1, -1, 2, "r", linestyles="--")


    plt.tight_layout()
    plt.savefig("logistic_eqn.png")

