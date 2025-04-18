# ACP Textual Space 认知轨迹协议 (Cognitive Trace Protocol)

## 1. 核心目的：外化 Cognitor 应用 Representamen 约束管理 Referent 的过程

在 ACP Textual Space 中，认知轨迹 (`Cognitive Trace`) 的核心目的并非传统意义上的运行时事件记录，而是作为一种由核心协议 ([[`01_introduction_and_core_protocol.md`]] 规定的**强制性机制**，用于**部分地外化和记录 `Cognitor` 在面对 `Space` 并管理其引发的意义不确定性 (`Referent`) 时，其内在的认知过程**。

根据 [[11_language.md]] 的定义，Textual Space 的交互本质是 `Cognitor` 运用文本自身的**形式和结构 (`Representamen`)** 作为**约束 (`Constraint`)**，来管理和消解**意义不确定性 (`Referent`)** 的核心实践。由于 `Cognitor` (特别是 LLM Agent 或 Human) 的核心认知过程——即如何应用约束来管理 `Referent`——通常是内部的、不透明的，**认知轨迹系统 (`Cognitive Trace System`)** 成为了理解其“思考”轨迹、决策依据、以及 `Referent` 是如何被逐步消解或固化为 `Representamen` 的关键窗口。

**认知轨迹的目标是降低不同 `Cognitor` 对 `Space` (Representamen 流及其关联的 Referent 状态) 认知状态的偏差，提升协作的透明度和可审计性。**

## 2. 认知轨迹作为记录 `Referent` 管理过程的 `Representamen`

- **轨迹内容 (`Representamen`):** `Cognitive Trace` 条目 (`message` 字段) 本身通常也是一段文本 (`Representamen`)，最常见的是自然语言叙述 (例如，使用 `tag="ReasoningNarrative"`)。它**反映了 `Cognitor` 对其自身如何识别 `Referent`、选择和应用 `Representamen` 约束、以及最终得出结论或采取行动（即管理 `Referent` 的过程）的模拟、报告或反思**。
- **创建者:** 认知轨迹由当前执行认知操作（即 操作者）的 `Cognitor` 负责创建。
- **消费者:** 其他 `Cognitor`（包括未来的自己或其他协作者）通过阅读这些 `Cognitive Trace` （作为 `Space` 的一部分，是重要的上下文 `Representamen` 约束），来理解之前的 `Representamen` 输入是如何被解析、其关联的 `Referent` 是如何被管理的。

## 3. 认知轨迹创建机制

- **手动性:**
    - 由于整个 Textual Space 由 `Cognitor` 维护，所有认知轨迹都会由 `Cognitor` 手动创建。
    - 通过 NPL 内置的 **`ct` 对象**（ `log.info` ，见 [[14.2_npl_reference_library]]）可通知 `Cognitor` 创建一条补充性的 `Cognitive Trace`。
- **时机:** `Cognitive Trace` 应在 `Cognitor` 执行关键认知步骤时创建，例如：
    - 解析文本 `Representamen` 并识别其核心 `Referent` 时。
    - 选择并应用特定的上下文 `Representamen` 或规则 `Representamen` 作为 `Constraint` 时。
    - 进行推理、决策以缩小 `Referent` 空间时。
    - 遇到 `Referent` 分支（歧义）并进行消解选择时。
    - 模拟执行操作（即应用推断出的行为 `Representamen`）前后。
    - 内部状态（`Referent` 的表征）发生显著变化时。
    - 反思 `Referent` 管理过程时。

## 4. 认知轨迹内容的特点与局限性 (Textual Space)

*   **自然语言为主 (`Representamen`):** LLM Agent 和 Human 创建的 `Cognitive Trace` 倾向于使用自然语言叙述其 `Referent` 管理过程。
*   **模拟性:** LLM Agent 创建的 `Cognitive Trace` 是其对自身**如何应用约束管理 `Referent` 的认知过程**的 *模拟或报告*，而非**真实内在状态**的直接转储。其详细度、准确性、客观性受模型能力和“意愿”影响。
*   **潜在冗余或不足:** 认知轨迹可能包含冗余信息（重复描述约束应用），也可能遗漏关键的 `Referent` 处理步骤（取决于 `Cognitor` 的实现）。
*   **无强制格式 (内容层面):** 协议不强制规定 `message` 内容 (`Representamen`) 的严格格式，重点在于其对其他 `Cognitor` 理解 `Referent` 管理过程的可读性。结构化信息主要依赖元数据字段。

## 5. 认知轨迹条目结构

虽然 Textual Space 本身是纯文本流，但在概念上，其 `Cognitive Trace` 条目应包含一些元数据信息，以方便理解和潜在的结构化处理。一个典型的认知轨迹条目（即使在纯文本中表现为一段话）应隐含或可以推断出以下信息（具体格式见 [[14.4_npl_cognitive_trace_reference]]）：

*   创建该轨迹的 Cognitor。
*   信息的类型。
*   为了便于引用而创建的顺序标识。
*   核心文本内容 (`Representamen`)，描述 `Referent` 管理过程。
*   内容的语义分类

## 6. 总结

Textual Space 的认知轨迹协议是其 `Representamen`-`Constraint`-`Referent` 核心模型的关键体现。它要求 `Cognitor` 将其内在的、应用 `Representamen` 约束来管理 `Referent` 的认知过程，通过创建作为 `Representamen` 的 `Cognitive Trace` 消息来进行外化，从而在纯文本交互环境中实现过程透明性和认知协作，也就是约束“其他 `Cognitor`（包括未来的自己或其他协作者）的理解”这个 `Referent`。