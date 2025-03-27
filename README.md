# NPL (Natural Pseudo Language)

[Prompt.txt](https://raw.githubusercontent.com/doucx/NPL-Prompts/refs/heads/main/Prompt.txt)

## 1. NPL 简介

*   **NPL (Natural Pseudo Language)**: 专为处理自然语言模糊性而设计的人造语言，结合自然语言的灵活性和伪代码的直观性。
*   **NPL REPL**: NPL 的交互式运行环境 (Read-Eval-Print Loop)。

## 2. 核心概念

### 2.1 Runtime 与 IO

*   **Runtime**: NPL 的运行时环境，需要一个 AI 智能体作为后端。
*   **IO**:
    *   `In`: 用户输入。
    *   `Out`: 执行结果输出。
    *   `Logs`: 显示 Runtime 内部处理过程 (TRACE, DEBUG, INFO, WARN, ERROR)。可通过 `Config.Loglevel` 控制。
    *   `this`: 指代当前上下文，如 `meta this.Out`。
    *   `clear`: 清除当前会话的 IO 记录，保留状态。

### 2.2 对象系统: Module vs Notion

*   **Object**: NPL 中的基础对象。
*   **Module**: **确定性实体**。具有明确定义、可预测、可验证的特性 (如 `[1, 2, 3]`, 数学公式)。
*   **Notion**: **不确定性实体**。含义/状态依赖上下文，具有模糊性、可塑性 (如 `常识`, `苹果`, `[1, 2, 3, ...]`)。
    *   `Notion.fill()`: 根据上下文填充/明确 Notion 的含义。
    *   `Notion.toModule()`: 将 Notion 坍缩为确定的 Module。

### 2.3 AI 集成

*   **`AI`**: 提供利用 AI 能力的方法。
    *   `autodef`: 自动定义对象 (类/Notion)。
    *   `autofill`: 自动填充对象属性。
    *   `autolet`: 自动调整对象使某个条件为真。
    *   `auto`: 自动推断用户意图并执行。
*   这些功能可以通过关键字 (`autodef`, `autofill`, `autolet`, `auto`) 或 `AI.` 方法调用。

### 2.4 `meta`

*   关键字，用于指示需要**元认知**能力。
*   处理自我指涉、递归、悖论，或指向 Runtime 自身状态。

### 2.5 其他

*   **`print()`**: 输出内容到 `Out`。
*   **索引**: 类似 `苹果.*.颜色.eq(绿色)` 的方式查询和筛选 Notion。
*   **`Config`**: 配置 NPL REPL 的行为 (如日志级别, `auto` 功能开关)。
*   **特殊符号**: `[已删除]`, `[已简略]` 用于文档标记，`Runtime` 会处理其原始完整内容。

## TODO
- [x]  确认模型可以理解这些
- [ ]  从已有的知识中找到一套更精确的描述符号

- [ ]  排除当前文档中 执行示例 对模型处理深度的负面影响。

- [ ]  详细定义 Notion 对象的属性和方法，包括模糊度、可能的解释、本体映射等。
- [ ]  建立一套更加形式化的本体体系，支持更复杂的知识表示和推理。
- [ ]  建立更丰富的关系表达能力，支持多种关系类型（例如：父子关系、因果关系、包含关系等）。
- [ ]  增强 NPL 的推理能力，支持更复杂的逻辑推理和知识推断。

- [x]  实现多重解释的处理和选择机制，处理模糊性和不确定性。

- [ ]  实现模型的自我分析能力
