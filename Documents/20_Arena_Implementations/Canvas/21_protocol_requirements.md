#  ACP Canvas 协议扩展
## 基本介绍
**ACP Canvas** 中的 **ACP Textual Aren** 扩展规范。

## 核心原则
ACP Canvas 协议设计基于以下核心原则：
*   **类XML格式**:  Arena Context 是 类似XML格式的文本。所有指令、数据和元信息都以XML格式交换。由于Canvas是基于Cognitor运行的，因此Canvas中的XML格式相比于一般的XML格式更加松。

## 核心实体
### Arena
*   **定义**: 在 Canvas 的 Arena 中，`Arena` 的模拟过程主要通过当前负责执行的 `Cognitor`（通常是语言模型）**生成文本并管理 `Cell` 流**来体现。其运作方式包含以下关键方面：

    1.  **上下文维护:** 它通过解析用户输入 (`EXEC`, `INPUT` Cell) 和生成输出 (`OUTPUT` Cell，包含 `stdout`, `Logs`, `value` 等)，完全基于可见的文本历史（`Cell` 序列）来维护交互上下文。
    2.  **基于规则的 `Cell` 创建 (状态机行为):** `Arena` (通过 `Cognitor` 的模拟) **主动监听并响应**特定事件或 `Cell` 状态，以按规则自动创建新的 `Cell`，驱动交互流程。这种“状态转换”机制主要包括：
        *   **`EXEC` -> `OUTPUT`:** 在处理完一个 `type="EXEC"` 的 `Cell` 后，自动创建一个对应的 `type="OUTPUT"` 的 `Cell` 来展示执行结果和日志。
        *   **`INPUT` -> `OUTPUT`:** 在用户提交一个 `type="INPUT"` 的 `Cell`（响应 `input()` 调用）后，自动创建一个新的 `type="OUTPUT"` `Cell` 来继续执行原 `EXEC` `Cell` 中 `input()` 之后的语句。
        *   **`input()` 调用 -> 等待 `INPUT`:** 当在 `EXEC` `Cell` 中遇到 `input()` 调用时，`Arena` 会暂停当前 `OUTPUT` `Cell` 的生成，并将其标记为等待状态（例如，设置 `<value type="INPUT_HINT">` 和 `<flags><flag value="WAIT"/></flags>`)，**监听**用户创建并提交相应的 `type="INPUT"` `Cell`。
        *   **`Flag` 驱动创建:** 明确的 `Cell` 标记（如 `<flags><flag value="ThenCreateCell"/></flags>`）可以指示 `Arena` 在处理完当前 `Cell` 后需要立即创建并处理一个（通常由 Fhrsk 或系统预定义的）新 `Cell`，而不只是等待用户输入。
    3.  **行为模拟:** `Arena` 的其他行为，如自动将自然语言路由给 Fhrsk，也是 `Cognitor` 根据对文本流和 ACP Textual Arena 规则的**理解和模拟**来执行的。
    4.  **纯文本基础:** 其“纯文本”特性在 Textual Arena 中表现为结构化（如 XML 风格）的文本记录，整个交互流程和状态变迁都必须通过这些文本记录来体现。

## 关键协议机制
### Logs (日志系统)
*   **定义** : 在 Canvas 中，`Logs` 嵌入到 `<log>` 节点中。