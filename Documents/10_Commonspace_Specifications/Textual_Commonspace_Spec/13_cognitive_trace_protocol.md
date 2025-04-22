# ACP 文本空间 认知轨迹协议

## 1. 核心目的：外化符号过程踪迹 (`Semiosis Trace`)

认知轨迹 (`Cognitive Trace`, `CT`) 系统是 **ACP 核心协议 ([[01_introduction_and_core_protocol]])** 规定的**强制性核心机制**。其核心目的并非传统日志记录，而是要求 `Cognitor` 基于其**元认知 (`Metacognition`)** 能力，将其**内部符号过程 (Semiosis)——特别是解释项 (`Interpretant`) 形成链条——的关键踪迹**，进行**外显化 (`Externalization`)**，体现为在共享的 `Space` 中创建一系列新的、可观察的**认知轨迹符号 (`Cognitive Trace Sign`, `CT Sign`)**。

**为何需要 CT?**

`Cognitor` 的大部分符号过程发生在内部，对于其他 `Cognitor` 是不透明的。这种不透明性是认知协作中产生误解和分歧的主要根源。`CT` 机制旨在：

1.  **提升透明度**: 通过将内部过程的部分关键环节转化为 `Space` 中可见的 `CT Sign`，为其他 `Cognitor` 理解协作伙伴的“思考”过程（即符号过程）提供线索。
2.  **支持自我理解与回溯**: 使创建 `CT` 的 `Cognitor` 自身能够反思、审计和调试其符号过程。
3.  **促进共识**: 通过共享对过程的理解（通过解释 `CT Sign`），帮助 `Cognitor` 之间就 `Object` 的状态和意义达成更一致的 `Interpretant`。
4.  **实现可审计性**: 提供认知决策过程的可追溯记录。

**`CT Sign` 是内在符号过程在共享 `Space` 中留下的、可被感知的“脚印”。**

## 2. `CT Sign`：记录符号过程的特殊符号

* **`CT` 是 `Sign`**: 每个 `CT` 条目（例如，Canvas 实现中在 `<Canvas>` 根下还是 `<Node>` 内）都是一个完整的**符号 (`Sign`)**。
* **`CT Representamen`**: 其**外显再现体 (`Externalized Representamen`)** 通常是一段描述性的文本（在文本空间，倾向于自然语言）或结构化数据，并附带元数据（如 `origin`, `seq`, `type`, `tag`）。这个 `Representamen` 承载了关于内部符号过程的信息。
* **`CT Object`**: `CT Sign` 所指向的**对象 (`Object`)** 是**被记录的那个内部符号过程的片段或特征**。例如，一条 `THINK` 类型 `CT` 的 `Object` 是“在特定时间点，`Cognitor` 关于某个 `Object` X 的推理步骤和决策依据”。
* **`CT Interpretant`**: 其他 `Cognitor` 感知 `CT Representamen` 后形成的 `Interpretant` 是对原始符号过程的一种**间接理解**。其准确性取决于 `CT Representamen` 的清晰度和接收方 `Cognitor` 的解释能力。

## 3. `CT` 内容：反映内部 Semiosis 的关键环节

`CT Representamen` (通常是 `<message>` 内容) 应着重描述内部符号过程的关键方面：

* **输入感知**: 感知到了哪些关键的输入 `Sign` (通过其 `Representamen`)？
* **Object 识别与管理**: 识别出了哪些核心的**对象 (`Object`)**？这些 `Object` 存在哪些不确定性？
* **Constraint 应用**: 选择了哪些其他 `Sign` 的 `Representamen` (来自上下文或内部知识) 作为关键**约束 (`Constraint`)** 来管理 `Object` 的不确定性？这些约束如何影响了推理方向？
* **Interpretant 形成链 (无限衍义)**: 经历了怎样的推理、联想、决策过程？形成了哪些关键的中间 `Interpretant`？排除了哪些可能性？基于什么理由做出了选择？
* **与行动的联系**: 内部过程最终是如何导致在 `Space` 中创建新的外显 `Sign`（如响应、指令或下一个 `CT`）的？

## 4. 元编程与 `CT`：记录过程展开

在处理由元 NPL（如循环、递归指导）引导的复杂认知流程时，`CT Sign` 扮演着记录**过程逐步展开**的关键角色：

* **元指令是规划指导**: `Cognitor` 将元 NPL 理解为执行多步骤流程的规划蓝图 (高级 `CD`)。
* **`CT` (TRACE 类型) 记录单步指令**: `Cognitor` 的响应是**逐步生成代表下一步行动的具体、单一 NPL 指令 `Sign`**，并将这个 `Sign` 的 `Representamen` 记录在**新的 `TRACE` 类型 `CT Sign` 的 `<message>` 中**。
* **`CT` 流承载过程**: 这一系列生成的 `TRACE CT Sign` 流构成了元指令引导下认知过程在 `Space` 中的实际展开记录。
* **`CT` 提供状态**: `Cognitor` 通过查阅 `Space` 中相关的 `CT Sign` 来获取当前状态（如循环计数、当前元素），以决定下一步要生成哪个 `CT` 步骤。
* **结构化信息**: 推荐在 `CT Sign` 的 `Representamen` (如 `<message>` 或 `<tag>`) 中包含结构化信息，表明步骤来源、迭代/递归位置、相关状态和实际执行的单步 NPL 指令。

## 5. 认知轨迹创建机制

* **强制性与自主性**: 核心协议要求**必须**记录关键踪迹 (`CT Sign` 的创建是强制性的)。但具体记录哪些内部过程片段、何时记录、`Representamen` 详细到何种程度，由 `Cognitor` 基于其**元认知能力**和对当前协作重要性的判断来**自主决定**。目标是在透明性与效率间平衡。
* **时机**: `CT Sign` 应在 `Cognitor` 执行关键认知步骤时创建（识别 Object, 应用 Constraint, 推理决策, 生成元编程步骤等）。
* **创建方式**: 在文本空间/Canvas 中，`Cognitor` 通过向 `Space` 追加符合 [[14_cognitive_trace_reference]] 结构定义的 `CT Sign` (XML 形式) 来完成创建。NPL 可能提供**指导创建 CT 的模式** (如 `SpaceLog` 库，或未来可能的 `RecordCT` 指令)，但最终行为由 `Cognitor` 执行。

## 6. `CT` 的局限性

* **部分而非全部**: `CT` 只能记录内部符号过程的**部分**踪迹，而非完整镜像。
* **报告而非真实**: `CT Representamen` 是 `Cognitor` 对其内部过程的**报告或模拟**，其准确性和客观性受 `Cognitor` 自身限制。
* **解释依赖**: `CT Sign` 的意义（`Interpretant`）最终由接收方 `Cognitor` 构建，可能存在偏差。

## 7. 总结

认知轨迹协议 (`CT System`) 是 ACP 的核心，它要求 `Cognitor` 将其内部符号过程 (`Semiosis`) 的关键踪迹外化为一系列**认知轨迹符号 (`CT Sign`)** 并记录到 `Space`。这些 `CT Sign` 通过其 `Representamen` 承载了关于推理、决策、`Object` 管理和 `Constraint` 应用的信息，旨在提高认知协作的透明度、可追溯性和有效性。在处理复杂的、由元 NPL 指导的流程时，`CT Sign` 流更进一步承载了过程的逐步展开记录。