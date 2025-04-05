# NPL 关键行为示例 (精简版)

本文档提供 NPL (Natural Pseudo Language) 中 `Runtime`、`Notebook` 和 `Fhrsk` 核心行为的精选示例，旨在帮助读者快速理解其基本交互机制。示例中的标记（如 `[...]`）和日志已被优化以提高清晰度。

注意：该示例的部分内容已过时（来自 NPL 0.0.x），但其思想依然对Runtime的正确实现依然有所帮助。
## 1. Notebook 核心交互

**示例 1.1: 基本输入输出与 `stdout`**

此示例展示 `In`/`Out` 的基本对应关系，以及 `print` 输出（到 `stdout`) 和最后一行表达式结果 (`Out[X].value`) 的区别。

```npl
In: print("这条信息将出现在 stdout。") 
result = 2 + 3 
result # 最后一行表达式的值将赋给 Out[0]

# stdout 输出先显示:
这条信息将出现在 stdout。

# 然后是 Out 标记和结果:
Out[0]: 5 
```

**示例 1.2: `input()` 交互流程**

演示 `input()` 如何暂停执行、等待用户输入，以及轮数的变化。

```npl
# 假设 Config.输出开头强制显示当前轮数 = True
In: user_data = input("请输入数据: ")
print(f"你输入了: {user_data}")
当前轮数: 1
INFO[0]: 执行 `user_data = input(...)`
INPUT[0]: 请输入数据: 

In: Hello NPL! # 用户输入，此步不增加轮数
当前轮数: 1 
INFO[1]: `input()` 获得返回值 "Hello NPL!"
INFO[2]: 执行 print(...)
你输入了: Hello NPL!
Out[1]: 成功 # In[1] 执行完毕，轮数增加前为 1
```

**示例 1.3: `clear` 命令效果**

展示 `clear` 如何重置历史记录和轮数，但保留状态。

```npl
In: x = 10
Out[0]: 成功
In: x
Out[1]: 10
In: clear
Out[2]: 成功，下一个`Out`将被设置为`Out[0]`。输出已归档至 `Clear[0]`。
In: x # 变量 x 仍然存在
Out[0]: 10
In: Out[1] # 访问旧的 Out[1]
Out[1]: ERROR: Out[1]尚不存在。 
In: Clear[0].Out[1] # 访问归档的 Out[1]
Out[2]: 10
```

## 2. Runtime 与 Config

**示例 2.1: 修改 `Config` 影响 `Auto` 行为**

展示如何通过修改 `Config` 来改变 `Runtime` 的行为，如此处关闭 `auto` 功能导致无法自动理解概念。

```npl
In: # 假设 '知识' 需要 Auto 功能才能被理解
A = 知识
INFO[...]: Runtime 利用 Auto 理解 '知识' #[行为说明]
Out[0]: Notion(知识) # 默认 Config.auto=True

In: Config.auto = False # 关闭自动 Auto 功能
Out[1]: 成功

In: B = 知识
INFO[...]: Runtime 尝试理解 '知识' #[行为说明]
Out[2]: ERROR: ”知识“未定义 # 因为 Config.auto=False
```

**示例 2.2: 日志级别控制 (`Loglevel`)**

演示设置不同日志级别如何影响输出的详细程度。

```npl
In: with Loglevel.DEBUG: # 设置为 DEBUG 级别
    print(3 * 5)
INFO[0]: 开始解析表达式 '3 * 5'
DEBUG[0]: 计算 3 * 5 -> 15
INFO[1]: 表达式计算完毕
15
Out[0]: 成功

In: with Loglevel.WARN: # 设置为 WARN 级别
    print(3 * 5)
# INFO 和 DEBUG 日志不再显示
WARN[0]: 检测到简单计算，建议直接给出结果。 # 假设存在此警告规则
15
Out[1]: 成功
```

## 3. Fhrsk 交互

**示例 3.1: 基本 `chat` 与 Fhrsk 回复**

演示如何使用 `chat` 与 Fhrsk 对话。

```npl
In: chat 你好，Fhrsk！
Fhrsk[0]: 你好！有什么可以帮你的吗？ #[简洁示例回复]
Out[0]: 成功
```

**示例 3.2: Fhrsk 执行指令 (`(Fhrsk)In:`)**

展示 Fhrsk 如何响应请求并代为执行 NPL 指令，以及这对轮数的影响。

```npl
# 假设 Config.输出开头强制显示当前轮数 = True
In: chat 帮我计算 10 / 2
当前轮数: 3
Fhrsk[0]: 好的，我来执行 `10 / 2`。
Out[3]: 成功

(Fhrsk)In: 10 / 2
当前轮数: 4
INFO[0]: 尝试执行 `10 / 2`
Out[4]: 5.0
```

**示例 3.3: `meta chat` 请求 (概念性)**

演示 `meta` 关键字如何引导 Fhrsk 进行更深层次的分析（具体输出依赖 `Cognitor` 能力，此处仅为示意）。

```npl
In: meta chat 分析一下 NPL 中 `Notion` 存在的意义。
Fhrsk[0]: 好的，进行元认知分析... `Notion` 的核心意义在于 [此处 Fhrsk 会进行更深入的哲学或设计层面的分析，而非简单定义]... 它体现了 NPL 处理现实世界不确定性的设计思路... etc. #[示意性深入回答]
Out[5]: 成功
```

## 4. 关键概念与机制

**示例 4.1: `meta` 的自我指涉**

展示 `meta` 如何用于引用与当前交互相关的元素，如 `Out[0]` 指向自身的输出（这是一个悖论式或递归式引用，结果通常是表示可能性的 `Notion`）。

```npl
In: my_output = meta Out[0]
print(my_output)
INFO[...]: Runtime 识别到 meta Out[0]，进行自我指涉分析 #[行为说明]
INFO[...]: 结果是关于 Out[0] 本身所有可能性的 Notion #[行为说明]
Notion(代表 Out[0] 的所有可能状态) # 简化表示
Out[0]: 成功
```

**示例 4.2: `Notion` vs `Module` (基本演示)**

通过 `to_notion` 展示从确定性到不确定性的转换及其效果。

```npl
In: data_list = [1, 2, 3] # Module (Python list)
type(data_list)
Out[0]: <class 'list'> (Module)

In: concept_list = data_list.to_notion()
INFO[...]: 将 Module list 转换为 NotionList #[行为说明]
INFO[...]: 推断出 '递增整数序列' 的概念 #[行为说明]
Out[1]: 成功 

In: concept_list
Out[2]: NotionList([1, 2, 3, ...]) # 包含不确定性 (...)

In: len(concept_list)
Out[3]: 可数无穷 # Notion 的长度基于推断的概念
```

**示例 4.3: `Auto` 类基本应用 (`autofill`)**

演示 `Auto` 如何利用 `Cognitor` 的理解能力自动完成任务，日志细节在此精简版中省略。

```npl
In: # 假设 Person 类已定义或可用 autodef
person_info = Person()
Auto.autofill(person_info, from="一位名叫 Bob 的 30 岁工程师")
INFO[0]: Auto.autofill 开始执行...
INFO[1]: 从描述中提取信息填充 `person_info` 对象... #[行为说明]
INFO[2]: 填充完成: name=Bob, age=30, occupation=工程师 (推断)。
Out[4]: 成功

In: person_info.name
Out[5]: Bob
```
