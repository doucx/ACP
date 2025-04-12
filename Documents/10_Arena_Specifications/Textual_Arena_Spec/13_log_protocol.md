# ACP Textual Arena 日志协议 (Log Protocol)

## 1. 核心目的：外化 Cognitor 的 `Language` 处理过程

在 ACP Textual Arena 中，日志 (`Logs`) 的核心目的并非传统意义上的运行时事件记录，而是作为一种**强制性机制**，用于**部分地外化和记录 `Cognitor` 在处理流经 Arena 的 `Language` 时，其内在的认知过程**。

根据 [[11_language]] 的定义，Textual Arena 的交互本质是 `Language` 的流动和 Cognitor 对其的理解与响应。由于 `Cognitor` (特别是 LLM Agent 或 Human) 的核心认知过程是内部的、不透明的，日志系统成为了理解其“思考”轨迹、决策依据、以及对 `Language` 指令如何被解读和执行的关键窗口。

**日志的目标是降低不同 `Cognitor` 对同一段 `ArenaContext` (Language 流) 认知状态的偏差，提升协作的透明度和可审计性。**

## 2. 日志作为 `Language` 的一种特殊形式

- **日志内容:** 日志消息 (`message` 字段) 本身通常也是一段 **`Language`**，最常见的是自然语言叙述 (例如，使用 `log_entry_type="ReasoningNarrative"`)。它反映了 `Cognitor` 对其自身思考过程的**模拟、报告或反思**。
- **生成者:** 日志由当前执行操作或进行思考的 `Cognitor` 负责生成。
- **消费者:** 其他 `Cognitor`（包括未来的自己或其他协作者）通过阅读这些日志（作为 `ArenaContext` 的一部分），来理解之前的 `Language` 是如何被处理的。

## 3. 日志生成机制

- **自动性 vs. 显式性:**
    - **隐式/自动:** 在理想的 NPL 驱动 Arena 中，部分底层执行日志（Trace 级别）可由 NPL 解释器自动生成（但这仍需 Cognitor 模拟解释器行为）。
    - **显式/核心:** 更常见和关键的是 `Cognitor` 通过 NPL 内置的 `Log` 对象（如 `Log.info(...)`, `Log.debug(...)`）**主动、显式地生成**描述其认知活动的日志。
- **时机:** 日志应在 `Cognitor` 执行关键认知步骤时生成，例如：
    - 解析指令 (`Language`) 时
    - 进行推理或决策时
    - 遇到歧义并进行消解时
    - 模拟执行操作前后
    - 改变内部状态（模拟）时
    - 响应 `meta` 指令进行反思时

## 4. `meta` 与日志：触发元认知记录

`meta` 关键字在日志协议中扮演关键角色。当 `Cognitor` 遇到 `meta Log.info(...)` 或类似指令时，它被明确要求：
1.  **调用其元认知能力**：对自身的 `Language` 处理过程、状态或理解进行反思。
2.  **生成阐述性日志**：将反思的结果以 `Language` (通常是自然语言) 的形式记录在日志中。

这使得日志不仅仅是行为记录，更能包含对行为**背后理由和认知状态**的洞察。

## 5. 日志内容的特点与局限性 (Textual Arena)

*   **自然语言为主:** LLM Agent 和 Human 生成的日志倾向于使用自然语言叙述。
*   **模拟性:** LLM Agent 生成的日志是其对自身认知过程的 *模拟或报告*，而非**真实内在状态**的直接转储。其详细度、准确性、客观性受模型能力和“意愿”影响。
*   **潜在冗余或不足:** 日志可能包含冗余信息，也可能遗漏关键决策点（取决于 `Cognitor` 的实现）。
*   **无强制格式 (内容层面):** 协议不强制规定 `message` 内容的严格格式，重点在于其对其他 `Cognitor` 的可理解性。结构化信息主要依赖元数据字段。

## 6. 日志条目结构 (参考 Canvas 规范)

虽然 Textual Arena 本身是纯文本流，但在概念上，其日志条目应包含与 ACP Canvas 日志条目类似的元数据信息，以方便理解和潜在的结构化处理。一个典型的日志条目（即使在纯文本中表现为一段话）应隐含或可以推断出以下信息（具体格式见 [[22.2_canvas_log_protocol.md]] 的设计理念，Textual Arena 实现时会简化其表示）：

*   `originator`: 产生日志的 Cognitor。
*   `type`: Cognitor 类型。
*   `log_level`: (`TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`) - 指示信息的重要性或性质。
*   `seq`: 顺序标识。
*   `message`: 核心 `Language` 内容。
*   `log_entry_type`: (可选) 内容的语义分类 (如 `ReasoningNarrative`, `ActionPlan`)。
*   `flag`: (可选) 特殊标记。

**在纯文本 Shell 实现中，这些元数据通常会被简化或省略，主要依赖日志级别关键字（如 `INFO:`）和 `message` 内容本身。**

## 7. 总结

Textual Arena 的日志协议是其 `Language`-centric 哲学的核心体现。它要求 `Cognitor` 将其处理 `Language` 的内在认知过程，通过生成作为 `Language` 的日志消息来进行外化，从而在纯文本交互环境中实现过程透明性和认知协作。
