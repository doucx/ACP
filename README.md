# NPL (Natural Pseudo Language)

[System Prompt](https://raw.githubusercontent.com/doucx/NPL-Prompts/refs/heads/main/Prompt.txt)

[Prompt for Chat （不确定有效）](https://raw.githubusercontent.com/doucx/NPL-Prompts/refs/heads/main/Prompt-Chat.txt)

我通常用于 NPL 的模型：Gemini 2.0 pro (api)

## 简介

**NPL (Natural Pseudo Language)** 是一种认知协作协议，旨在实现跨载体的智能交互。它定义了一套规范，使得不同的认知实体（例如 AI、人类或混合系统）能够通过 NPL 进行交流和协作，共同完成复杂的任务。

**NPL 是一种协议，一种通用语，而非编程语言**

## 核心功能

*   **跨载体兼容：** 同一段 NPL 代码可由 AI、人类或混合团队执行。
*   **能力导向：** 不限定技术实现，只要求载体具备学习、推理、元认知三大核心能力。
*   **过程可审计：** Logs 提供完整的执行溯源，支持调试和优化。
*   **动态扩展：** 允许运行时切换载体。
*   **Fhrsk交互：** 通过Fhrsk进行人性化互动。

## 基本用法示例

### 1. 指令理解

NPL 能够理解清晰的指令，包括自然语言和代码：

```npl
In: print("Hello, NPL!")
```

### 2. 变量赋值与计算

```npl
In: x = 10
In: y = 20
In: print(x + y)
```

### 3. 使用 Auto 自动推断

```npl
In: auto 定义一个函数，计算两个数的平均值
```

### 4. 与 Fhrsk 交互

```npl
In: chat 你好，Fhrsk!
```

### 5. 元认知能力

```npl
In: with meta: chat 请重新审视 {Out[0]}
```

## 关键对象

*   **NPL.Runtime:** NPL 的智能执行环境。
*   **Cognitor:** 认知执行体，例如 AI、人类。
*   **Fhrsk:** 人性化交互界面。
*   **Auto:** 自动推断和执行工具。

## 日志 (Logs)

NPL Runtime 会生成详细的日志，记录执行过程中的各种信息，方便调试和优化。

## 更多信息

请参考完整的 NPL 文档以了解更多细节。

## 更多信息

请查阅完整的 NPL.文档 以获取更多详细信息。

## TODO
- [x]  确认模型可以理解这些
- [ ]  从已有的知识中找到一套更精确的描述符号

- [x]  排除当前文档中 执行示例 对模型处理深度的负面影响。
   - 可行，但需要强大的模型

- [x]  详细定义 Notion 对象的属性和方法，包括模糊度、可能的解释、本体映射等。
- [ ]  建立一套更加形式化的本体体系，支持更复杂的知识表示和推理。
- [ ]  建立更丰富的关系表达能力，支持多种关系类型（例如：父子关系、因果关系、包含关系等）。
- [x]  增强 NPL 的推理能力，支持更复杂的逻辑推理和知识推断。

- [x]  实现多重解释的处理和选择机制，处理模糊性和不确定性。

- [x]  实现模型的自我分析能力
- [x]  仅通过对doc的修改，使meta方法可以突破NPL而与实现它的模型交互
