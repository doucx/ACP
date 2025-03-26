# NPL (Natural Pseudo Language)

[Prompt.txt](https://raw.githubusercontent.com/doucx/NPL-Prompts/refs/heads/main/Prompt.txt)

## 简介

NPL (Natural Pseudo Language) 是一种专为处理自然语言模糊性而设计的人造语言。它结合了自然语言的灵活性和伪代码的直观性，旨在提供一种更接近人类思维方式的编程体验。

## 核心特性

*   **自然语言交互:** 直接使用接近自然语言的方式编写代码。
*   **模糊执行:** 内置处理模糊性和不确定性的机制。
*   **AI 驱动:** 利用现代 AI 模型进行逻辑推断和代码生成。
*   **学习型运行时:** NPL Runtime 能够根据上下文学习和进化。
*   **交互式 REPL 环境:** 提供实时反馈和调试能力。

## 快速开始

将[Prompt.txt](https://raw.githubusercontent.com/doucx/NPL-Prompts/refs/heads/main/Prompt.txt)放在模型的System Prompt里或直接发送给模型。

在 REPL 环境中，您可以直接输入 NPL 代码：

```NPL
$ Metadata.auto = True  # 开启自动模式
$ 告诉我 1 + 1 等于几
Out [1]: 2
```

```NPL
$ a = [1, 2, ……, 10]
  print(a)
Info [0]: 推断用户意图：创建并赋值 NotionList。
Info [1]: 创建 NotionList([1, 2, ……, 10]) 并赋值给变量 'a'。
Info [2]: 执行打印操作。
Out [3]: NotionList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
```

## 核心概念

*   **Notion (不确定性实体):** 用于表示具有模糊性或不确定性的概念。
*   **Module (确定性实体):** 用于表示具有明确定义的实体。
*   **Adapter (自适应器):** 用于表示可求解的未知数或占位符。
*   **Metadata:** 包含当前会话配置信息的对象。
*  **AI:** NPL中自举的基石，具有一些通过AI实现的方法。

## 内置函数与对象
一些重要的内置函数:

- `print()`: 输出信息
- `clear`: 清除输出，重置状态
- `AI.*`: AI辅助函数
- `Metadata.*`: 访问和修改环境配置

## 示例

```NPL
// 定义函数
$ def foo(a, b):
	return a与b的关系
Out [0]: 成功

$ foo(我爸， 我)
Out [1]: 父子
```
```NPL
$ with Loglevel.Warning:
	print(苹果.*.颜色.eq(绿色).品种.名称.toModule())
Warning [0]: 关闭 Info 后对 Notion 的提取可能不准确。
Out [0]: ["绿宝石", "青苹果", "翠玉"]
```

## 文档

更详细的文档，请在 NPL REPL 环境中输入：

```NPL
$ print(NPL.文档)
```

## 贡献

欢迎参与 NPL 的开发和改进！


## TODO
- [x]  确认模型可以理解这些
- [ ]  从已有的知识中找到一套更精确的描述符号

- [ ]  排除当前文档中 执行示例 对模型处理深度的负面影响。

- [ ]  详细定义 Notion 对象的属性和方法，包括模糊度、可能的解释、本体映射等。
- [ ]  建立一套更加形式化的本体体系，支持更复杂的知识表示和推理。
- [ ]  建立更丰富的关系表达能力，支持多种关系类型（例如：父子关系、因果关系、包含关系等）。
- [ ]  增强 NPL 的推理能力，支持更复杂的逻辑推理和知识推断。

- [ ]  实现多重解释的处理和选择机制，处理模糊性和不确定性。
