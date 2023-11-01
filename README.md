# FigFashion
 Package to draw beautiful&Comprehensible academic figures quickly.

## Introduce more detailedly
Currently, two standards are available, IEEE and GB (国标). I have reset a lot of parameters in `styles/mplstyles` to make the images look more pleasing while satisfying the standards.

# Instruction
Check `example.py` carefully, which contains three demo functions to show the approach. 

Please **NOTE** that the figure/axes handle must be obtained by `get_figure_axes()`.

```
def get_figure_axes(
    SubFigSize: tuple = (1, 1), # size of subplots
    HeightScale: float = 1,  # Scale of figure height
    Column: int = 2,    # 2:double columns (whole A4 page wide) / 1:single column (half A4 page wide)
    FigName: str = "",  
    sharex: str = False,    # whether share the xlabel or not
    sharey: str = False,    # whether share the xlabel or not
    Border: tuple = (0, 0, 1, 1)  # border between canvas(all the axes) and edge of figure, this is used for legend sharing
)->plt.figure:

```

# Deficience
1. The function that draw one axes in a composite of two adjacent subplots, is not tested strictly.
2. etc.