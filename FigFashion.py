from matplotlib import pyplot as plt
from typing import List, Literal
import numpy as np
from matplotlib import rcParams
import os, sys
from .colors import colorsets

root = os.path.dirname(os.path.abspath(__file__))



class FigFon:
    """noting that
    all the figure size will be set as Golden ratio with width fixed as required,
    if the author needs the figure to be higher than standards,
    HeightScale should be defined when using get_figure_axes()  """

    def __init__(self):
        from matplotlib import font_manager
        font_path = root + "/fonts/times simsun.ttf"
        font_manager.fontManager.addfont(font_path)
        self.prop = font_manager.FontProperties(fname=font_path).get_name()

    @staticmethod
    def _set_fashion_IEEE():
        obj = FigFon()
        plt.style.use(root + "/styles/IEEE.mplstyle")
        rcParams["font.serif"] = obj.prop

    @staticmethod
    def _set_fashion_GB():
        obj = FigFon()
        plt.style.use(root + "/styles/GB.mplstyle")
        rcParams["font.serif"] = obj.prop

    @staticmethod
    def get_figure_axes(
            SubFigSize: tuple = (1, 1),
            HeightScale: float = 1,
            Column: int = 2,  # double columns or single
            FigName: str = "",
            sharex: str = False,
            sharey: str = False,
            share_legend: bool = False,
            Border: tuple = (0, 0, 1, 1)
    ) -> plt.figure:

        Width = [3.5, 7.16]
        Height = 2.5
        if Column == 1:
            HeightScale = SubFigSize[0] / SubFigSize[1] * HeightScale
            FigSize = (Width[0], HeightScale * Height)
        elif Column == 2:
            HeightScale = SubFigSize[0] / SubFigSize[1] * HeightScale * 2
            FigSize = (Width[1], HeightScale * Height)
        else:
            print("Column can be only defined as 1 or 2")
            raise ValueError
        fig, axes = plt.subplots(nrows=SubFigSize[0],
                                 ncols=SubFigSize[1],
                                 layout="tight",
                                 figsize=FigSize,
                                 sharex=sharex,
                                 sharey=sharey
                                 )

        tight = {"pad": 0.1, "w_pad": 0.6, "h_pad": 0.4, "rect": Border}
        fig.set_tight_layout(tight)
        return fig, axes

    @staticmethod
    def set_fashion(fashion: str = "IEEE"):
        colors = colorsets["Modern Scientific"]
        plt.rcParams['axes.prop_cycle'] = plt.cycler('color', colors)
        if fashion == "IEEE":
            FigFon._set_fashion_IEEE()
            pass
        elif fashion == "GB":
            FigFon._set_fashion_GB()
            plt.rcParams["font.serif"] = ["Times New Roman", "SimSun"]
            plt.rcParams['font.family'] = ' Times New Roman, SimSun'
        else:
            print("fashion type input error, which can only selected as IEEE or GB")
            raise TypeError

    @staticmethod
    def set_shared_legend(handles,
                          labels,
                          Loc: Literal["upper  center", "lower center"] = "lower center",
                          Cols=None):
        FigSize = plt.gcf().get_size_inches()
        StdLegendWidth = 3.5 / 4
        RowVolumn = int(np.round(FigSize[0] / StdLegendWidth)) if Cols is None else Cols
        Rows = np.ceil(labels.__len__() / RowVolumn)

        StdLegendHeight = 0.15  # inch
        NewFigHeight = StdLegendHeight * Rows + FigSize[1]
        BorderRatio = StdLegendHeight * Rows / NewFigHeight

        Border = [0, 0, 1, 1]
        if Loc == "upper center":
            Border[3] -= BorderRatio
        elif Loc == "lower center":
            Border[1] += BorderRatio
        tight = {"pad": 0.1, "w_pad": 0.5, "h_pad": 0.5, "rect": Border}
        plt.gcf().set_size_inches((FigSize[0], NewFigHeight))
        plt.gcf().set_tight_layout(tight)
        plt.figlegend(handles, labels,
                      loc="lower center",
                      # loc="lower right",
                      bbox_to_anchor=(0.45, -0.03, 0.1, 0.1),
                      ncol=RowVolumn,
                      frameon=False)

    def get_axes_from_figure(self):
        pass

    def get_axes(self):
        pass

    def update_axes(self):
        pass

    def update_figure(self):
        pass

    def set_color_cycle(self, name):
        plt.rcParams['axes.prop_cycle'] = plt.cycler('color', colorsets[name])
