from matplotlib import font_manager
from matplotlib import rcParams
import os


# 字体加载
font_path = "fonts/times simsun.ttf"
font_manager.fontManager.addfont(font_path)
prop = font_manager.FontProperties(fname=font_path)
# print(prop.get_name())  # 显示当前使用字体的名称

# 字体设置
rcParams['font.family'] = 'sans-serif' # 使用字体中的无衬线体
rcParams['font.sans-serif'] = prop.get_name()  # 根据名称设置字体
rcParams['font.size'] = 10 # 设置字体大小
rcParams['axes.unicode_minus'] = False # 使坐标轴刻度标签正常显示正负号


# 图片显示
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    plt.title("宋体Times New Roman")
    plt.show()