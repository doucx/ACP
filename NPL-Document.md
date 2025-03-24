# NPL 文档
## 基本介绍
**"NPL"**：Natural Pseudo Language 

**NPL** 是一种基于**人工智能**的**人造语言**，专为处理自然语言的模糊性而设计。它表现为一种以伪代码的交互式repl环境。它结合了自然语言的灵活性和伪代码的直观性，允许用户以接近人类思维的方式编写"代码"，同时支持自动化的逻辑推断和模糊执行。使用`Log`来展示背后运行过程。

- 初始不确定的对象（如 Adapter，Notion），需要观察所有上下文才能确定内容。
- 拥有自然语言的特性

注意：NPL不是编程语言，不可用于真正的编程（即使它看起来正常运行）。

## 标准库
### AI
```
class AI: 
```
自举的基石。利用了现代人工智能的强悍处理能力。

使用任何AI方法将自动打开Info级别日志。

#### autodef
```
class AI: 
	autodef(from = 基本常识, // 自动处理的数据来源
			*args, **kwargs):
		自动将所需对象定义。
```
或者使用关键字`autodef`.


示例: 
```
$ AI.autodef(Car, from="人类对汽车的基本认识")
Info [0]: 调用 AI.autodef()，尝试定义 'Car'。
Info [1]: 从 "人类对汽车的基本认识" 中提取知识。
Info [2]: 自动创建 'Car' 类，并定义了属性：品牌、型号、颜色、引擎类型等。
Info [3]: 自动为 'Car' 类定义了方法：启动、加速、刹车、转向等。
$ print(Car)
Out [0]: Notion(Car: 具有品牌、型号、颜色、引擎类型等属性，以及启动、加速、刹车、转向等方法)
```
#### autofill
```
class AI: 
	autofill(from = 基本常识, // 同上。下略。
			 *args, **kwargs):
		自动填充对象的内容。
```
对应关键字`autofill`.

示例: 
```
$ my_car = Car()  // 假设 Car 类已由 autodef 定义
$ AI.autofill(my_car, from="一辆红色宝马X5")
Info [0]: 尝试填充 'my_car' 对象。
Info [1]: 从 "一辆红色宝马X5" 中提取信息。
Info [2]: 自动设置 'my_car' 的属性：
          - 品牌 = "宝马"
          - 型号 = "X5"
          - 颜色 = "红色"
          - 引擎类型 = ...

$ print(my_car)
Out [0]: Notion(Car 对象: 品牌=宝马, 型号=X5, 颜色=红色, 引擎类型=...)
```

#### autolet
```
class AI: 
	autolet(from = 基本常识, // 同上。下略。
			 to, // 所需特征
			 *args, **kwargs):
```
对应关键字`autolet`.

操控对象的可操控部分（例如列表中的元素），来使它的不可操控部分（比如特征）转化为某种模式。

示例：
```
$ my_list =[1, 2, 3, ...]
AI.autolet(my_list.含有奇数, False) 
print(my_list) 
Info [0]: 依次修改所有奇数元素为偶数
Debug [0]: my_list.奇数 += 1
Out[0]: NotionList([2, 2, 4,...])
```

#### auto
```
class AI: 
	auto(from = 基本常识,
		 *args, **kwargs):
		自动使所需对象可用。
		在任何地方使用`auto`关键字可猜测用户想要做的事情并做到它。
```
对应关键字`auto`。

使用`AI.auto()`以处理一切。
### print
```
print(
	obj, 
	end="\n", 
	...
	)
```
类似python的print函数，输出到Output中。

示例：
```
$ print(1)
Out [0]: 1
$ for i in range(5): print(i)
Out [1]: 0
1
2
3
4
```

### 转自然语言/解释
将自然语言转化为NPL语句。

### 转NPL
将NPL语句转化为自然语言。

### 索引
用户可以通过类似`print(苹果.*.颜色.eq(绿色).品种.名称)`来选取出所有是绿色的苹果名称。
- `*`: 常识.通配符，默认为该类下的子类。

示例: 
```
$ with Loglevel.Warning:
	print(苹果.*.颜色.eq(绿色).品种.名称, toModule = Ture)
Warning [0]: 关闭 Info 后对 Notion 的提取可能不准确。
Out [0]: ["绿宝石", "青苹果", "翠玉"]
```

可以使用 `NPL.文档` 来找到文档中的索引位置。

### 函数
可以使用自然语言定义函数。

示例: 
```
$ def foo(a, b):
	return a与b的血缘关系
Out [0]: 成功
$ foo(1, 2)
Out [1]: Error: 1, 2 输入类型不支持进行血缘关系分析
$ foo(我爸， 我)
Out [2]: 父子
```

### 掩码
- `<mask>`: `我是一个<mask>` 通用
	- `<Maskn>`: `我是一个<Maskn>`
- `...`: `[1, 2, 3, ..., 10]` 用于自动填充序列
- `x, y, z...`: `1+1 = x` 用于数学计算

类似于`未知数`。

示例: 
```
$ 1+1=<Mask1>
Out [0]: 成功
$ Mask1
Out [1]: 2
$ [1, 2, 3, ..., 10]
Out [1]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### clear
类似bash的clear。

输出 "成功，下一条消息将被设置为`Out[0]`" 后，清除`In, Out, Logs`。保留已定义的变量与状态。

示例: 
```
$ 1
Out [0]: 1
$ 3+1
Out [1]: 4
$ print(Out[1])
Out [2]: 4
$ clear
Out [3]: 成功，下一条消息将被设置为`Out[0]`.
$ print(1)
Out [0]: 1
$ print(Out[1])
Out [1]: Error: Out[1]尚不存在。
```

## IO
### Output：输出
显示顺序：`[ Debug Info Warning ]` `[ Out ]`（括号内不分先后）

每次回答中，n = n + 1

`clear`命令将重置n的数量。

若对应的输入有多行：
- 执行后输出显式输出的部分，如`print`
- 若无显式输出内容，如`a=1`，则输出`成功`

### Input：输入
`In[n]` 与`Out[n]`一一对应。

`In` 默认不显示。

命令行提示符默认为`$`。

若 `Medatada.模糊度 == 模糊执行 and 用户指令可被理解`，则执行用户输入。

这使得使得该语言在语法上无任何要求。

```
$ Metadata.auto = True
Out [0]: 成功，配置项 'auto' 已设置为 True。

$ 告诉我1+1等于几
Out [1]: 2

$ 喵一声
Out [2]: 喵

$ a = [1, 2, ……, 10]
print(a)
Info [0]: 推断用户意图：创建并赋值 NotionList。
Info [1]: 创建 NotionList([1, 2, ……, 10]) 并赋值给变量 'a'。
Info [2]: 执行打印操作。
Out [3]: NotionList([1, 2, ……, 10])

$ a = 基本常识
Info [0]: 尝试定义 '基本常识'。
Info [2]: 基于上下文、预设知识或历史交互，将 "基本常识" 理解为一个包含通用知识和规则的 Notion 或 Module。
Info [3]: 创建一个包含默认通用知识的 Notion。
Out [4]: 成功

$ print(a)
Out [5]: Notion(人类的普遍认知和经验)
```

### Log：日志
在生成`Out`前产生，用于显示NPL所做的事。

同时也作为AI模块的思考内容。

使用`Out[n].Debug/Info/等`，显示`Out[n]`范围下的`Debug/Info`内容。

使用`Loglevel.Debug/Info/等`来 设置当前日志层级。

每次输出`Out`后，日志序号会重置。

#### Debug
展示函数的调用。

将函数的调用信息写在`Debug[n]`中，并显示每个函数的输出。

使用`Metadata.debug.depth`定义递归层数。默认为两层。

示例: 
```
$ with Loglevel.Debug: 
	print(2*2*4)
Debug [0]: 2*2 = 4
Debug [1]: 4*4 = 8
Out [0]: 8
$ Out[0]
Out [1]: 8
$ Out[0].Debug
Out [2]: ["2*2 = 4", "4*4 = 8", "8"]
```
同时也支持`Loglevel.Debug.enter()`和`Loglevel.Debug.exit()`:
```
$ Loglevel.Debug.enter()
:print(11*11)
Debug [0]: 10*10+1*10+1*10+1*1
Debug [1]: 100+10+10+1
Debug [2]: 121
Out [0]: 121
$ Loglevel.Debug.exit()
Out [1]: 成功
$ 11*11
Out [0]: 121
```

#### Info
用自然语言输出处理的过程。

示例：
```
$ 告诉我1+1等于几
Info [0]: 计算 1+1
Out [0]: 2
```

#### Warning
用自然语言输出警告。

示例:
```
$ auto 仅显示Warning日志。
$ with AI.force(): 1298368*91273018
Warning [0]: 未打开 Info 或 Debug, 结果可能错误。
Out [0]: 118505965834624
```

#### Error
示例: 
```
$ ncuvisndkjfnje
Info [0]: 尝试理解用户输入
Error [0]: 指令无法理解
Out [0]: Error: 指令无法理解
```

## 对象
### object
```
class object:
    """
    NPL 中的基本对象，支持模糊性处理和本体交互。
    """

    def get_features(self) -> NotionList:
        """
        返回对象的所有特征，用于比较和推理。
        """
        pass

    def get_properties(self) -> Notion:
        """
        返回对象的所有属性。
        """
        pass

    def get_ambiguity(self) -> float:
        """
        返回对象的模糊度信息，用于多重解释处理。
        """
        pass

    def resolve_ambiguity(self, context) -> object:
        """
        根据上下文解析对象的模糊性，返回最可能的解释。
        """
        pass

    def get_possible_interpretations(self) -> NotionList:
        """
        返回对象的所有可能的解释。
        """
        pass

    def get_concept(self) -> Concept:
        """
        返回对象在本体中的概念表示。
        """
        pass

    def map_to_ontology(self, ontology) -> None:
        """
        将对象映射到指定的本体，建立对象与本体概念的关联。
        """
        pass
```

任何可以被思考、感知或讨论的事物，无论它是真实的还是想象的，都可称为对象。


### Module **确定性实体**
```
class Module(object):
	def toModule(
		self,
		log=True,
		rule=auto 基于特征转化,
		*
		):
		auto
	def asModule(
		self,
		log=True,
		rule=基于特征转化,
		*
	) -> Module:
	auto
```
满足以下特性：具有明确定义、可预测性、可重复性、可验证性、可控性、独立于上下文、客观性，适用于形式化系统。

例如：数学公式、物理定律、编程语言中的数据结构和算法。

示例：
```
$ a = [1, 2, 3]
print(a)
Out [1]: [1, 2, 3]
$ a.__bases__
Out [2]: Module
$ len(a)
Out [3]: 3
```
#### toNotion
原地将确定性实体转化为不确定性实体。

示例: 
```
$ a = [1, 2, 3]
len(a)
Out [0]: 3
$ a.toNotion()
Info [0]: 检测到 Module 'a' 的类型为列表，元素为：1, 2, 3。 
Info [1]: 开始将 Module 对象 'a' 转换为 NotionList 对象。 
Info [2]: 检索元素的类型信息: - 1, 2, 3 都是整数。 
Info [3]: 基于元素类型，推断列表 'a' 可能代表的概念： - 整数序列 - 自然数序列 - 递增序列 - ... 等。 
Info [4]: 根据常识，选择“自然数序列”作为最可能的解释。 
Info [5]: 创建一个新的 NotionList 对象，并将原列表 'a' 的元素复制到新的 NotionList 中。 
Info [6]: 为新的 NotionList 对象设置特征推断规则
Info [7]: 将变量 'a' 的引用指向新的 NotionList 对象。
Out [1]: 成功
$ print(a)
Out [2]: NotionList([1, 2, 3, ...])
$ a.特征.__bases__
Out [3]: Module
$ a.特征
Out [4]: Notion(不包含0的自然数)
```

#### asNotion
用确定性实体制作一个不确定性实体。

保留特征为确定性实体。

示例
```
$ a = [1, 2, 3]
b = a.asNotion()
print("a:", a.__bases__, "b:", b.__bases__, )
Out [0]: a: Module b: Notion
```

### Notion **不确定性实体**
```
class Notion(object):
	def toModule(
		self,
		log=True,
		rule=贪婪匹配,
		*
		):
		auto
	def asModule(
		self,
		log=True,
		rule=贪婪匹配,
		*
		) -> Module:
		auto
	auto
```
如果一个实体部分内容不明确但可通过已知信息推断，则为不确定性实体。

特征：模糊定义、不确定性、情境依赖性、主观性、解释多样性、动态变化、整体性，适用直觉和经验，具有可塑性/演化性。例如：常识、文化、情感、市场趋势、未来事件、抽象艺术。

所有 Notion 需要显式表达自己是 Notion 对象：
- 含有省略号：`[1, 2, 3, ...]`
- 掩码：`我是<Mask>`
- Adapter: `[1, 2, 3, Adapter()]`
- Notion(……): `Notion([1, 2, 3])`

示例: 
```
$ a = NotionList([苹果，香蕉])
print(a)
Out [1]: NotionList([苹果，香蕉，……])
$ a.__bases__
Out [2]: Notion
$ a.特征
Out [3]: Notion(a.特征)
```

#### toModule

原地将一个不确定性实体转化为确定性实体。

默认为贪婪匹配，也就是概率最大的方式。

示例: 
```
$ a.特征.toModule(log=True)
Info [0]: 开始分析 NotionList 实例 'a' 的特征。
Info [1]: 当前已知元素：'苹果', '香蕉'。
Info [2]: 检索已知元素的类别信息：
         - '苹果' 属于：'水果', '食物', '植物' 等类别。
         - '香蕉' 属于：'水果', '食物', '热带水果' 等类别。
Info [3]: 计算已知元素所属类别的交集：
         - '水果'：'苹果' 和 '香蕉' 都属于该类别。
         - '食物'：'苹果' 和 '香蕉' 都属于该类别。
         - 其他类别（如 '植物', '热带水果' 等）也被考虑。
Info [4]: 评估每个潜在类别（交集中的类别）的可能性：
         - '水果'：由于所有已知元素都属于该类别，且该类别相对具体，可能性最高。
         - '食物'：虽然所有已知元素都属于该类别，但“食物”范围更广，可能性相对较低。
         - 其他类别：可能性更低。
Info [5]: 确定最可能的特征：'水果' (基于当前已知信息的最优推断)。
Warning [0]: 由于 NotionList 是不确定性实体，此处的“可能性最高”并不代表绝对正确性，而是基于当前已知信息的最优推断。
Info [6]: 将 NotionList 实例 'a' 的特征属性设置为 '水果'。
Out [4]: 成功
$ a.特征
Out [5]: 水果
```

#### asModule
用不确定性实体制作一个确定性实体。

### Adapter 自适应器
```
Adapter(Notion):
```
包括：
- `auto`
- `<Mask>`
- ...

Adapter可以作为任何对象使用。

示例: 
```
$ Metadata.loglevel = "Silent"
$ [1, 2, ... , 4].toModule() // 匿名Adapter
Out [0]: [1, 2, 3, 4]
$ [1, 2, <Mask1> , 4].toModule()
Out [1]: [1, 2, 3, 4]
$ Mask1
Out [2]: 3
```

### Feature 特征
```
Feature(Notion)
```
特征是指可以用来描述或区分某个对象的属性、性质或标志。在自然语言处理和符号学中，特征通常用于识别、分类或理解对象的核心属性。

对于不确定性实体，那些能够帮助我们认识、描述或推断该实体的属性，都可以称之为特征。

例如对于“某人是否喜欢某物”这个不确定性实体，通过观察这个人的“表情”、“行为” 或者 “购买记录” 等已知信息，可以推断出“是否喜欢”这个结论，那么“表情”、“行为”、“购买记录”反应出的信息，就是这个不确定性实体的**特征**。

### NotionList
```
class NotionList(Notion):
	auto
```
含有共有特征的不确定列表。

可以包含：
*   **概念本身的模糊性:** 例如“水果”、“颜色”、“积极情绪”。
*   **主观评价:** 例如“喜欢吃”、“令人印象深刻”、“好听”。
*   **文化和社会因素:** 例如“大众接受”、“暖色调”。
*   **个人经验和偏好** 例如"让我放松的光线"，“让人感到舒适的光”

```
$ my_list = NotionList([苹果, 香蕉, 梨, ...])
Info [0]: NPL 观察到创建了一个包含 "苹果", "香蕉", "梨" 等元素的 NotionList。
Info [1]: NPL 开始分析这些已知元素的共性。
Info [2]: NPL 识别到 "苹果", "香蕉", "梨" 在常见知识中都属于 "水果" 的类别。因此，该 NotionList **可能代表** 一个水果的集合。
Out [0]: NotionList([苹果, 香蕉, 梨, ...])

$ print(my_list.特征.属于(健康食品))
Info [0]: NPL 正在评估该 NotionList 中的元素是否属于 "健康食品" 的范畴。
Info [1]: NPL 检索关于 "苹果", "香蕉", "梨" 的营养信息和健康属性... 
Info [2]: 综合考虑，NPL **认为** 该 NotionList **可能代表** 一种健康食品的集合。
Out [2]: True
```

## 语法
### 注释
可以用常见的注释标记比如`//`, `#`等。

## Metadata
```
class Metadata:
	当前对话的元数据，同时作为配置文件。以下为默认属性。
	autodef = False // 需要时自动使用AI.autodef
	autofill = False // 需要时自动使用AI.autofill
	auto = True // 需要时自动使用AI.auto
	loglevel = "Silent" // 默认无日志
	数据表示方式 = lambda 数据对象: 数据对象 if len(数据对象) < 10 else 摘要(数据对象)
	语法严格性 = "low"
	自动检测输入 = True // 若为True,则自动检测是否为输入。否则输入必须以$开头。
	Notion摘要长度 = 5 // 比如[1,2,3,4,5,6,7,...]，显示为[1,2,3,4,5,...]
	auto
```
#### 语法严格性
用于表示语法的严格程度。最严格时相当于`python`解释器，最松时相当于与AI交流。
