# ACP Textual Arena 日志协议 (Log Protocol)

## 1. 核心目的：外化 Cognitor 应用 `Forma` 约束管理 `Uncertainty` 的过程

在 ACP Textual Arena 中，日志 (`Logs`) 的核心目的并非传统意义上的运行时事件记录，而是作为一种**强制性机制**，用于**部分地外化和记录 `Cognitor` 在面对文本输入 (`Forma`) 并管理其引发的意义不确定性 (`Uncertainty`) 时，其内在的认知过程**。

根据 [[11_language.md]] 的定义，Textual Arena 的交互本质是 `Cognitor` 运用文本自身的**形式和结构 (`Forma`)** 作为**约束 (`Constraint`)**，来管理和消解**意义不确定性 (`Uncertainty`)** 的核心实践。由于 `Cognitor` (特别是 LLM Agent 或 Human) 的核心认知过程——即如何应用约束来管理 `Uncertainty`——是内部的、不透明的，日志系统成为了理解其“思考”轨迹、决策依据、以及 `Uncertainty` 是如何被逐步消解或固化为 `Forma` 的关键窗口。

**日志的目标是降低不同 `Cognitor` 对同一段 `ArenaContext` (Forma 流及其关联的 Uncertainty 状态) 认知状态的偏差，提升协作的透明度和可审计性。**

## 2. 日志作为记录 `Uncertainty` 管理过程的 `Forma`

- **日志内容 (`Forma`):** 日志消息 (`message` 字段) 本身通常也是一段文本 (`Forma`)，最常见的是自然语言叙述 (例如，使用 `log_entry_type="ReasoningNarrative"`)。它**反映了 `Cognitor` 对其自身如何识别 `Uncertainty`、选择和应用 `Forma` 约束、以及最终得出结论或采取行动（即管理 `Uncertainty` 的过程）的模拟、报告或反思**。
- **生成者:** 日志由当前执行认知操作（即管理 `Uncertainty`）的 `Cognitor` 负责生成。
- **消费者:** 其他 `Cognitor`（包括未来的自己或其他协作者）通过阅读这些日志（作为 `ArenaContext` 的一部分，是重要的上下文 `Forma` 约束），来理解之前的 `Forma` 输入是如何被解析、其关联的 `Uncertainty` 是如何被管理的。

## 3. 日志生成机制

- **自动性 vs. 显式性:**
    - **隐式/自动:** 在理想的 NPL 驱动 Arena 中，部分底层执行日志（Trace 级别）可由 NPL 解释器（由 `Cognitor` 模拟）在应用结构化 `Forma` 约束时自动生成。
    - **显式/核心:** 更常见和关键的是 `Cognitor` 通过 NPL 内置的 `Log` 对象（如 `Log.info(...)`, `Log.debug(...)`）**主动、显式地生成**描述其应用约束管理 `Uncertainty` 的认知活动的日志。
- **时机:** 日志应在 `Cognitor` 执行关键认知步骤时生成，例如：
    - 解析文本 `Forma` 并识别其核心 `Uncertainty` 时。
    - 选择并应用特定的上下文 `Forma` 或规则 `Forma` 作为 `Constraint` 时。
    - 进行推理、决策以缩小 `Uncertainty` 空间时。
    - 遇到 `Uncertainty` 分支（歧义）并进行消解选择时。
    - 模拟执行操作（即应用推断出的行为 `Forma`）前后。
    - 内部状态（`Uncertainty` 的表征）发生显著变化时。
    - 响应 `meta` 指令，反思 `Uncertainty` 管理过程时。

## 4. `meta` 与日志：触发对 `Uncertainty` 管理过程的反思记录

`meta` 关键字在日志协议中扮演关键角色。当 `Cognitor` 遇到 `meta Log.info(...)` 或类似指令时，它被明确要求：
1.  **调用其元认知能力**：对自身的**`Uncertainty` 管理过程**、状态或对 `Forma` 约束的理解进行反思。
2.  **生成阐述性日志 (`Forma`)**：将反思的结果以文本 (`Forma`) 的形式记录在日志中，描述其如何应用约束、处理不确定性。

这使得日志不仅仅是行为记录 (`Forma` 输出)，更能包含对行为**背后理由和 `Uncertainty` 管理策略**的洞察。

## 5. 日志内容的特点与局限性 (Textual Arena)

*   **自然语言为主 (`Forma`):** LLM Agent 和 Human 生成的日志倾向于使用自然语言叙述其 `Uncertainty` 管理过程。
*   **模拟性:** LLM Agent 生成的日志是其对自身**如何应用约束管理 `Uncertainty` 的认知过程**的 *模拟或报告*，而非**真实内在状态**的直接转储。其详细度、准确性、客观性受模型能力和“意愿”影响。
*   **潜在冗余或不足:** 日志可能包含冗余信息（重复描述约束应用），也可能遗漏关键的 `Uncertainty` 处理步骤（取决于 `Cognitor` 的实现）。
*   **无强制格式 (内容层面):** 协议不强制规定 `message` 内容 (`Forma`) 的严格格式，重点在于其对其他 `Cognitor` 理解 `Uncertainty` 管理过程的可读性。结构化信息主要依赖元数据字段。

## 6. 日志条目结构 (参考 Canvas 规范)

虽然 Textual Arena 本身是纯文本流，但在概念上，其日志条目应包含与 ACP Canvas 日志条目类似的元数据信息，以方便理解和潜在的结构化处理。一个典型的日志条目（即使在纯文本中表现为一段话）应隐含或可以推断出以下信息（具体格式见 [[22.2_canvas_log_protocol.md]] 的设计理念，Textual Arena 实现时会简化其表示）：

*   `originator`: 产生日志的 Cognitor。
*   `type`: Cognitor 类型。
*   `log_level`: (`TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`) - 指示信息的重要性或性质。
*   `seq`: 顺序标识。
*   `message`: 核心文本内容 (`Forma`)，描述 `Uncertainty` 管理过程。
*   `log_entry_type`: (可选) 内容的语义分类 (如 `ReasoningNarrative`, `ConstraintApplication`)。
*   `flag`: (可选) 特殊标记。

**在纯文本 Shell 实现中，这些元数据通常会被简化或省略，主要依赖日志级别关键字（如 `INFO:`）和 `message` 内容 (`Forma`) 本身。**

## 7. 总结

Textual Arena 的日志协议是其 `Forma`-`Constraint`-`Uncertainty` 核心模型的关键体现。它要求 `Cognitor` 将其内在的、应用 `Forma` 约束来管理 `Uncertainty` 的认知过程，通过生成作为 `Forma` 的日志消息来进行外化，从而在纯文本交互环境中实现过程透明性和认知协作。