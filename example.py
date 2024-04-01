from FigFashion import FigFon
import numpy as np
from matplotlib import pyplot as plt


def example():
    """test function for page-wide(two column) figure"""
    def double_plot(row, col, isHigh=1):
        size = 10
        x = np.arange(size)
        y = np.c_[x, x ** 1.2, x ** 1.5]
        fig, axeses = FigFon.get_figure_axes(SubFigSize=(row, col), HeightScale=isHigh)
        for axes in axeses.flat:
            axes.plot(x, y)
            axes.set_xlabel("xlabel 2468 宋体Times New Roman")
            axes.set_ylabel("英文： 2468")
            # axes.set_title("TITLE")
        plt.savefig("figs/double" + row.__str__() + col.__str__() + "_" + isHigh.__str__() + ".png")
        plt.show()

    """test function for one column (half page wide) figure"""
    def single_plot(row, col, isHigh=1):
        size = 10
        x = np.arange(size)
        y = np.c_[x, x ** 1.2, x ** 1.5]
        fig, axeses = FigFon.get_figure_axes(
            SubFigSize=(row, col),
            HeightScale=isHigh,
            Column=1,
            Border=(0, 0, 1, 1)
        )
        axeses = [axeses] if isinstance(axeses, plt.Axes) else axeses.flat
        for axes in axeses:
            axes.plot(x, y)
            axes.set_xlabel("xlabel 2468 宋体Times New Roman")
            axes.set_ylabel("英文： 2468")
        legends1 = ["legend1", "legend2", "legend3"]
        plt.legend(legends1)
        plt.savefig("figs/single" + row.__str__() + col.__str__() + "_" + isHigh.__str__() + ".png")
        plt.show()

    def shared_plot(row, col, isHigh=1):
        size = 10
        x = np.arange(size)
        y = np.c_[x, x ** 1.2, x ** 1.5]
        fig, axeses = FigFon.get_figure_axes(
            SubFigSize=(row, col),
            HeightScale=isHigh,
            sharey="all",
            sharex="all",
            Column=1

        )
        lines = []
        for axes1 in axeses:
            for axes in axes1:
                line = axes.plot(x, y)
                lines += line
                axes.set_title("(a)")

        axeses[-1, 0].set_xlabel("xlabel1 ")
        axeses[-1, 1].set_xlabel("xlabel2 坐标轴")
        axeses[2, 0].set_ylabel("ylabel ")
        axeses[1, 0].set_ylabel("ylabel2 $ylabel$")
        legends1 = ["legend1", "legend2", "legend3", "legend4"] * 3
        legends2 = ["a", "b", "c", "d"] * 3
        FigFon.set_shared_legend(lines, legends2)
        # plt.savefig("figs/share_double" + row.__str__() + col.__str__() + "_" + isHigh.__str__() + ".png")
        plt.show()

    FigFon.set_fashion("IEEE")
    shared_plot(3, 2, 1)


if __name__ == "__main__":
    example()
