#  ACP Textual Arena 协议扩展
## 基本介绍
**ACP Textual Arena** 中基于 **ACP 核心协议** 的扩展规范。

## 核心原则
ACP Textual Arena 协议设计基于以下核心原则：
*   **纯文本交互 (`Forma` 流)**: ACP Textual Arena 的 Arena Context 本质上是**结构化文本 (`Forma`) 的流动**。所有指令、数据和元信息都以文本形式（作为 `Forma` 的载体）交换。`Cognitor` 的核心活动是处理这些文本 `Forma`，利用其结构和上下文作为**约束 (`Constraint`)** 来管理和消解其引发的**意义不确定性 (`Uncertainty`)**。即使 `Cognitor` 模拟了高级概念，其状态和对 `Uncertainty` 的管理过程也**必须**通过认知轨迹 (`Cognitive Trace`，以 `Forma` 形式记录) 进行记录和维护，以确保跨载体的一致性和可审计性。
*   **`Forma`-`Constraint`-`Uncertainty` 核心**: 整个 Textual Arena 的运作都建立在 `Cognitor` 应用可见的文本形式 (`Forma`) 作为约束 (`Constraint`) 来处理意义不确定性 (`Uncertainty`) 的核心过程之上。（见 [[11_language.md]]）

## 核心实体
### Cognitor (认知实体)

*   **定义**: 在典型的 Textual Arena 环境中，`Cognitor` 通常是指参与交互的**大型语言模型 (LLM Agent) 或人类用户**。它们的核心认知能力体现为**处理和理解文本 (`Forma`)**（包括自然语言和 NPL），并基于此运用其内在的学习（适应对话流程）、推理（应用 `Forma` 约束解释指令、管理 `Uncertainty`、生成响应 `Forma`）和元认知（通过 `meta` 触发或内在反思，审视自身的 `Uncertainty` 管理过程，并通过 `Cognitive Trace` 报告）能力。其能力表现受限于具体的模型或个人。`Cognitor Info` 旨在捕获这些具体实例的元信息 (`Forma`)。

### Arena (认知空间)
*   **定义**: 在 Textual Arena 中，`Arena` 的模拟过程主要通过当前负责执行的 `Cognitor` **在其自身的认知中，处理流经的文本 (`Forma`)、应用约束 (`Constraint`)、管理不确定性 (`Uncertainty`) 并生成相应的文本输出 (`Forma`) 及认知轨迹 (`Cognitive Trace`) 来体现**。其运作方式包含以下关键方面：

    1.  **上下文维护:** 它通过解析历史文本流 (ArenaContext，一个 `Forma` 序列，包括之前的 `Cognitive Trace`) 来维护交互上下文。这个历史 `Forma` 构成了 `Cognitor` 应用约束、管理 `Uncertainty` 的主要隐式 `Constraint` 来源。
    2.  **行为模拟:** `Arena` 的其他行为，如路由、状态转换（见 [[22.3_canvas_implementation.md]]），是 `Cognitor` 根据其对文本流 (`Forma`) 和 ACP Textual Arena 规则 (`Forma`-Constraint) 的**理解和模拟**来执行的。这些行为本质上是 `Cognitor` 在管理“下一步该做什么”这个核心 `Uncertainty` 后的 `Forma` 输出，其决策过程应记录在 `Cognitive Trace` (特别是 `ArenaLog` 如果在 Canvas 中)。
    3.  **`Forma` 基础:** 其交互完全构建在由 `Cognitor` 处理的 `Forma` 流之上，整个交互流程和状态变迁都必须通过这些文本记录（作为 `Forma` 传递 `Constraint`、管理 `Uncertainty` 和留下 `Cognitive Trace` 的载体）来体现。

## 交互
### 认知指令 (Cognitive Directive) 在 Textual Arena 中的表现

在 Textual Arena 中，认知指令 (Cognitive Directive) 是 `Cognitor` 间用于沟通、协作和执行任务的 **特定类型的文本 (`Forma`)**。Textual Arena 的媒介特性决定了认知指令主要通过文本形式进行传递，其目的是**提供明确的约束 (`Constraint`) 来引导目标 `Cognitor` 管理特定的意义或行动 `Uncertainty`**。其具体表现形式如下：

1.  **自然语言指令 (Natural Language Directives):**

    *   **定义**: 使用自然语言（如中文、英文等 `Forma`）表达的指令、问题或请求。这类 `Forma` 通常约束性较弱，需要 `Cognitor` 依赖更多上下文 (`Forma`-Constraint) 和推理能力来管理其 `Uncertainty`。
    *   **触发**: 可由 `Cognitor` 自行发起，或由其他 `Cognitor` 通过特定交互模式（如 `chat` 关键字，一个提供上下文 `Constraint` 的 `Forma`）触发。
    *   **解析**: `Cognitor` 应根据 ACP 协议 (`Forma`-Constraint) 和其自身的**核心语言理解能力**（应用 `Forma` 约束管理 `Uncertainty` 的能力）对自然语言指令 (`Forma`) 进行理解和解析，并将理解过程记录在 `Cognitive Trace` 中，然后执行相应的操作。
    *   **示例**:
        *   `"请总结一下这篇文章的主要内容。"` (这段 `Forma` 提供了总结任务的 `Constraint`，指向关于“文章主要内容是什么”的 `Uncertainty`)
        *   `"chat 你认为接下来应该怎么做？"` (这段 `Forma` + `chat` 关键字提供了请求建议的 `Constraint`，指向关于“后续行动方案”的 `Uncertainty`)
        *   `${User}，请帮我执行这段 Python 命令，我没有可以直接操作的 Python 解释器。` (混合 `Forma`，包含委托执行的 `Constraint`)

2.  **NPL 指令 (Natural Pseudo Language Directives):**

    *   **定义**: 使用 NPL (Natural Pseudo Language) 表达的结构化指令 (`Forma`)。NPL 是一种旨在提供**更强、更明确的结构化 `Forma`-Constraint** 的文本形式，用以增强指令精确性、降低歧义、并更清晰地**引导 Cognitor 管理目标 `Uncertainty`**。
    *   **目的**: 提供一种比自然语言更精确、更结构化的方式来表达复杂的认知指令，尤其是涉及对认知概念 (`Uncertainty`/`Forma` 句柄) 的操作。执行过程和结果应通过 `Cognitive Trace` 记录。
    *   **详细规范**: 详见 [[14.1_npl_directive_representation_protocol.md]]。
    *   **示例**:
        *   `my_car = Car(); my_car.color = "red";` (这段 NPL `Forma` 提供了创建对象和设置属性的强 `Constraint`，管理关于 `my_car` 状态的 `Uncertainty`)
        *   `Auto.autolet(my_list.length < 5)` (这个 `Forma`-Constraint 引导 `Cognitor` 管理关于 `my_list` 状态的 `Uncertainty`，使其满足长度约束)

**区分机制**:

Textual Arena 中的 `Cognitor` **应能够**区分自然语言指令 (`Forma`，弱约束) 和 NPL 指令 (`Forma`，强约束)。具体的区分机制是 **`Cognitor` 基于其内在的文本处理能力**（模式识别、语法分析等）自行实现的，它需要将输入的 `Forma` 与已知的 NPL 结构 `Forma` (作为 `Constraint`) 进行匹配，从而判断是哪种指令类型，并管理其解析 `Uncertainty`。其实现应遵循以下原则：

*   **有效性**: 能够准确地区分两种指令形式 (`Forma`)。
*   **透明性**: 在 `Cognitive Trace` (`Forma`) 中记录其区分过程和依据（作为其处理输入 `Forma` 并管理 `Uncertainty` 的一部分）。
*   **一致性**: 在相同的上下文下，对相同类型的指令 `Forma` 应保持一致的判断。

**说明**:

*   区分机制的实现方式不限，可以基于语法模式识别、关键字识别、语义分析等 `Cognitor` 自身具备的应用 `Forma`-Constraint 管理 `Uncertainty` 的能力。

### 信息表示 (基于 `Forma` 与 `Uncertainty`)

#### Uncertainty 不确定性实体 (从 `Forma` 约束中浮现)
在 Textual Arena 中，`Uncertainty` **是 `Cognitor` 在处理文本 (`Forma`) 时识别出的、需要通过认知活动来消解的意义可能性空间或模糊性**。它不是独立的本体，而是 `Cognitor` 对 `Forma` 应用 `Constraint` 过程中的核心处理对象。当 `Cognitor` 面对一个指向 `Uncertainty` 状态的句柄（通常是一个变量名或一个文本片段）时，它会利用其**语言理解、常识知识和推理能力**来：
    *   评估该 `Uncertainty` 所代表的可能性空间。
    *   根据 `ArenaContext` (历史 `Forma` 流作为隐式 `Constraint`) 或通过 `add_constraint` 提供的额外 `Forma` 约束，聚焦于最相关的含义。
    *   运用认知能力（推理、补全）来填充缺失的信息或细节（处理 `Uncertainty` 的模糊性）。
    *   生成一个当前看来最合理、最连贯的理解，并通过 `pick`, `to_module` 等方法将其（定性地）表达出来（通常产生新的 `Forma`）。
    *   整个评估、约束应用和精化过程都应通过 **`Cognitive Trace`** 进行记录。
    *   因此，在 Textual Arena 中，`Uncertainty` 的管理本质上是**引导 `Cognitor` 对特定的文本 `Forma` 应用各种 `Forma`-Constraint 进行深度解读、消歧和固化的过程**。其有效性高度依赖于 `Cognitor` 的**语境理解和应用约束生成合理推测**的能力。

#### Forma 确定性实体 (作为 `Constraint` 或 `Uncertainty` 处理结果)
在 ACP Textual Arena 中，`Forma` 扮演双重角色：
1.  **约束 (`Constraint`)**: 文本字符串本身、语言的结构、语法规则、NPL 语句、上下文历史 (`ArenaContext` 中的 `Forma`，包括过去的 `Cognitive Trace`) 等，都是形式确定的 `Forma`，被 `Cognitor` 用来**约束和管理 `Uncertainty`**。
2.  **结果 (`Uncertainty` 处理产物)**: 当 `Cognitor` 成功处理一段文本（管理了其 `Uncertainty`）后，**提取或生成的、形式上确定、意义在此刻被固化的信息片段**也是 `Forma`。例如，从一段描述中解析出的数值、执行 NPL 代码后返回的特定结构数据、或者 `Cognitor` 生成的明确答复文本，以及记录这个过程的 `Cognitive Trace` 条目本身。它是 `Uncertainty` 管理过程后的**结果快照或需要进一步处理的确定性输入**。

## 关键协议机制
### Cognitive Trace System (认知轨迹系统)

*   **定义** : 在 Textual Arena 中，`Cognitive Trace` 是 **`Cognitor` 对其自身应用 `Forma` 约束来管理 `Uncertainty` 的认知过程（理解、推理、决策、状态模拟等）进行的部分外化记录**。它由负责执行的 `Cognitor` 以文本形式 (`Forma`) 生成。`Cognitive Trace` 条目的消息 (`message` 字段 `Forma`) 通常是自然语言叙述（如 `log_entry_type="ReasoningNarrative"`），反映了 `Cognitor` 对其内在 `Uncertainty` 管理活动的**模拟或报告**。这些轨迹的质量受 `Cognitor` 能力和意愿影响。详见 [[13_cognitive_trace_protocol.md]]。

### `meta` (元认知调用关键字)

*   **定义** : 当 `Cognitor` 在 Textual Arena 中遇到 `meta` 关键字（一个 `Forma` 形式的指令）时，它被要求**调用其内在的元认知能力，对其自身的 `Uncertainty` 管理过程（如何应用 `Forma` 约束）进行反思和报告**。这可能包括分析之前的 `Forma` 输出、解释其推理步骤（如何从 `Constraint` 推导出结论）、讨论其对某个 `Uncertainty` 理解的局限性、或进行更深层次的上下文关联。这种“元认知”的实现方式是**基于文本 (`Forma`) 的、表达性的**，其结果记录在 **`Cognitive Trace`** (`Forma`) 中。
