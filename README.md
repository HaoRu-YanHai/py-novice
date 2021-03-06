# python练习
收集了一些python相关的小练习，适合有一定python基础的，需要练习巩固并训练思维的新手。<br>
如果需要，这有一个编程闯关的网站：
[`Checkio`](https://py.checkio.org/)
## Numpy入门70题
[`练习题答案`](https://numpy.org.cn/article/advanced/numpy_exercises_for_data_analysis.html)<br>
1. 导入numpy作为np，并查看版本
    **问题：将numpy导入为np,并打印版本号**
2. 如何创建一维数组？
    **问题：创建从0到9的一维数字数组**
3. 如何创建一个布尔数组？
    **问题：创建一个numpy数组元素值全为True（真）的数组**
4. 如何从一维数组中提取满足指定条件的元素？
    **问题：从 arr 中提取所有的奇数**
5. 如何用numpy数组中的另一个值替换满足条件的元素项？
    **问题：将arr中的所有奇数替换为-1。**
6. 如何在不影响原始数组的情况下替换满足条件的元素项？
    **问题：将arr中的所有奇数替换为-1，而不改变arr。**
7. 如何改变数组的形状？
    **问题：将一维数组转换为2行的2维数组**
8. 如何垂直叠加两个数组？
    **问题：垂直堆叠数组a和数组b**
9. 如何水平叠加两个数组？
    **问题：将数组a和数组b水平堆叠。**
10. 如何在无硬编码的情况下生成numpy中的自定义序列？
    **问题：创建以下模式而不使用硬编码。只使用numpy函数和下面的输入数组a。**
11. 如何获取两个numpy数组之间的公共项？
    **问题：获取数组a和数组b之间的公共项。**
12. 如何从一个数组中删除存在于另一个数组中的项？
    **问题：从数组a中删除数组b中的所有项。**
13. 如何得到两个数组元素匹配的位置？
    **问题：获取a和b元素匹配的位置。**
14. 如何从numpy数组中提取给定范围内的所有数字？
    **问题：获取5到10之间的所有项目。**
15. 如何创建一个python函数来处理scalars并在numpy数组上工作？
    **问题：转换适用于两个标量的函数maxx，以处理两个数组。**
16. 如何交换二维numpy数组中的两列？
    **问题：在数组arr中交换列1和2。**
17. 如何交换二维numpy数组中的两行？
    **问题：交换数组arr中的第1和第2行：**
18. 如何反转二维数组的行？
    **问题：反转二维数组arr的行。**
19. 如何反转二维数组的列？
    **问题：反转二维数组arr的列。**
20. 如何创建包含5到10之间随机浮动的二维数组？
    **问题：创建一个形状为5x3的二维数组，以包含5到10之间的随机十进制数。**
21. 如何在numpy数组中只打印小数点后三位？
    **问题：只打印或显示numpy数组rand_arr的小数点后3位。**
22. 如何通过e式科学记数法（如1e10）来打印一个numpy数组？
    **问题：通过e式科学记数法来打印rand_arr（如1e10）**
23. 如何限制numpy数组输出中打印的项目数？
    **问题：将numpy数组a中打印的项数限制为最多6个元素。**
24. 如何打印完整的numpy数组而不截断
    **问题：打印完整的numpy数组a而不截断。**
25. 如何导入数字和文本的数据集保持文本在numpy数组中完好无损？
    **问题：导入鸢尾属植物数据集，保持文本不变。**
26. 如何从1维元组数组中提取特定列？
    **问题：从前面问题中导入的一维鸢尾属植物数据集中提取文本列的物种。**
27. 如何将1维元组数组转换为2维numpy数组？
    **问题：通过省略鸢尾属植物数据集种类的文本字段，将一维鸢尾属植物数据集转换为二维数组iris_2d。**
28. 如何计算numpy数组的均值，中位数，标准差？
    **问题：求出鸢尾属植物萼片长度的平均值、中位数和标准差(第1列)**
29. 如何规范化数组，使数组的值正好介于0和1之间？
    **问题：创建一种标准化形式的鸢尾属植物间隔长度，其值正好介于0和1之间，这样最小值为0，最大值为1。**
30. 如何计算Softmax得分？
    **问题：计算sepallength的softmax分数。**
31. 如何找到numpy数组的百分位数？
    **问题：找到鸢尾属植物数据集的第5和第95百分位数**
32. 如何在数组中的随机位置插入值？
    **问题：在iris_2d数据集中的20个随机位置插入np.nan值**
33. 如何在numpy数组中找到缺失值的位置？
    **问题：在iris_2d的sepallength中查找缺失值的数量和位置（第1列）**
34. 如何根据两个或多个条件过滤numpy数组？
    **问题：过滤具有petallength（第3列）&gt; 1.5 和 sepallength（第1列）&lt; 5.0 的iris_2d行**
35. 如何从numpy数组中删除包含缺失值的行？
    **问题：选择没有任何nan值的iris_2d行。**
    ```python
      # Input
      url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
      iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
    ```
36. 如何找到numpy数组的两列之间的相关性？
    **问题：在iris_2d中找出SepalLength（第1列）和PetalLength（第3列）之间的相关性**
    ```
    # Input
      url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
      iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
    ```
37. 如何查找给定数组是否具有任何空值？
    **问题：找出iris_2d是否有任何缺失值。**
    ```python
      # Input
      url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
      iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
    ```
38. 如何在numpy数组中用0替换所有缺失值？
    **问题：在numpy数组中将所有出现的nan替换为0**
    ```python
      # Input
      url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
      iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
      iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
    ```
39. 如何在numpy数组中查找唯一值的计数？
    **问题：找出鸢尾属植物物种中的独特值和独特值的数量**
    ```python
      # Input
      url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
      iris = np.genfromtxt(url, delimiter=',', dtype='object')
      names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
    ```
40. 如何将数字转换为分类（文本）数组？
    **问题：将iris_2d的花瓣长度（第3列）加入以形成文本数组，这样如果花瓣长度为：**
41. 如何从numpy数组的现有列创建新列？
    **问题：在iris_2d中为卷创建一个新列，其中volume是**
42. 如何在numpy中进行概率抽样？
    **问题：随机抽鸢尾属植物的种类，使得刚毛的数量是云芝和维吉尼亚的两倍**
43. 如何在按另一个数组分组时获取数组的第二大值？
    **问题：第二长的物种setosa的价值是多少**
44. 如何按列对2D数组进行排序
    **问题：根据sepallength列对虹膜数据集进行排序。**
45. 如何在numpy数组中找到最常见的值？
    **问题：在鸢尾属植物数据集中找到最常见的花瓣长度值（第3列）。**
46. 如何找到第一次出现的值大于给定值的位置？
    **问题：在虹膜数据集的petalwidth第4列中查找第一次出现的值大于1.0的位置。**
47. 如何将大于给定值的所有值替换为给定的截止值？
    **问题：从数组a中，替换所有大于30到30和小于10到10的值。**
48. 如何从numpy数组中获取最大n值的位置？
    **问题：获取给定数组a中前5个最大值的位置。**
49. 如何计算数组中所有可能值的行数？
    **问题：按行计算唯一值的计数。**
50. 如何将数组转换为平面一维数组？
    **问题：将array_of_arrays转换为扁平线性1d数组。**
51. 如何在numpy中为数组生成单热编码？
    **问题：计算一次性编码(数组中每个唯一值的虚拟二进制变量)**
52. 如何创建按分类变量分组的行号？
    **问题：创建按分类变量分组的行号。使用以下来自鸢尾属植物物种的样本作为输入。**
53. 如何根据给定的分类变量创建组ID？
    **问题：根据给定的分类变量创建组ID。使用以下来自鸢尾属植物物种的样本作为输入。**
54. 如何使用numpy对数组中的项进行排名？
    **问题：为给定的数字数组a创建排名。**
55. 如何使用numpy对多维数组中的项进行排名？
    **问题：创建与给定数字数组a相同形状的排名数组。**
56. 如何在二维numpy数组的每一行中找到最大值？
    **问题：计算给定数组中每行的最大值。**
57. 如何计算二维numpy数组每行的最小值？
    **问题：为给定的二维numpy数组计算每行的最小值。**
58. 如何在numpy数组中找到重复的记录？
    **问题：在给定的numpy数组中找到重复的条目(第二次出现以后)，并将它们标记为True。第一次出现应该是False的。**
59. 如何找出数字的分组均值？
    **问题：在二维数字数组中查找按分类列分组的数值列的平均值**
60. 如何将PIL图像转换为numpy数组？
    **问题：从以下URL导入图像并将其转换为numpy数组。**
61. 如何删除numpy数组中所有缺少的值？
    **问题：从一维numpy数组中删除所有NaN值**
62. 如何计算两个数组之间的欧氏距离？
    **问题：计算两个数组a和数组b之间的欧氏距离。**
63. 如何在一维数组中找到所有的局部极大值(或峰值)？
    **问题：找到一个一维数字数组a中的所有峰值。峰顶是两边被较小数值包围的点。**
64. 如何从二维数组中减去一维数组，其中一维数组的每一项从各自的行中减去？
    **问题：从2d数组a_2d中减去一维数组b_1D，使得b_1D的每一项从a_2d的相应行中减去。**
65. 如何查找数组中项的第n次重复索引？
    **问题：找出x中数字1的第5次重复的索引。**
66. 如何将numpy的datetime 64对象转换为datetime的datetime对象？
    **问题：将numpy的**
67. 如何计算numpy数组的移动平均值？
    **问题：对于给定的一维数组，计算窗口大小为3的移动平均值。**
68. 如何在给定起始点、长度和步骤的情况下创建一个numpy数组序列？
    **问题：创建长度为10的numpy数组，从5开始，在连续的数字之间的步长为3。**
69. 如何填写不规则系列的numpy日期中的缺失日期？
    **问题：给定一系列不连续的日期序列。填写缺失的日期，使其成为连续的日期序列。**
70. 如何从给定的一维数组创建步长？
    **问题：从给定的一维数组arr中，利用步进生成一个二维矩阵，窗口长度为4，步距为2，类似于**
## python练习
* 八皇后问题<br>
在8×8格的国际象棋上摆放8个皇后，使其不能互相攻击，即任意两个皇后都不能处于`同一行`、`同一列`或`同一斜线`上。
问有多少种摆法？
[`我的代码`](https://github.com/HaoRu-YanHai/py-novice/blob/main/eight-queens.py)

* 约瑟夫问题<br>
N个人围成一圈
从第一个开始报数，第M个将被杀掉，接着`下一个`开始报数，第M个将被杀死，直到最后剩下一个，其余人都将被杀掉。
问哪个位置是安全的？
[`我的代码`](https://github.com/HaoRu-YanHai/py-novice/blob/main/Josephus.py)
