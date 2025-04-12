#  ACP Textual Arena 协议扩展
## 基本介绍
**ACP Textual Arena** 中的 **ACP 核心协议** 扩展规范。

## 核心原则
ACP Textual Arena 协议设计基于以下核心原则：
*   **纯文本交互 (`Language` 流)** : ACP Textual Arena 的 Arena Context 本质上是 **`Language` 的流动**，即 Cognitor 认知活动的外在表现。所有指令、数据和元信息都以文本形式（作为 `Language` 的载体）交换。这意味着即使 `Cognitor` 模拟了高级概念，其状态和行为也**必须**通过文本日志进行记录和维护，以确保跨载体的一致性和可审计性。
	* 由于其本质是 `Language` 流，因此整个 `Textual Arena` 都自然被 `Language` 约束。（见 [[11_language]]）

## 核心实体
### Cognitor (认知执行体)

*   **定义** : 在典型的 Textual Arena 环境中，`Cognitor` 通常是指参与交互的**语言模型（如 ChatGPT）或人类用户** 。它们的核心认知能力体现为**处理和理解 `Language`** （包括自然语言和 NPL），并基于此进行学习（适应对话流程）、推理（解释指令、生成代码/回答）和元认知（通过 `meta` 触发或内在反思）。其能力表现受限于具体的模型或个人。`Cognitor Info` 旨在捕获这些具体实例的元信息。

### Arena
*   **定义**: 在 Textual Arena 中，`Arena` 的模拟过程主要通过当前负责执行的 `Cognitor` **在其自身的认知中处理流经的 `Language` 并生成相应的文本输出来体现**。其运作方式包含以下关键方面：

    1.  **上下文维护:** 它通过解析用户输入和生成输出 (`Language` 片段)，完全基于可见的文本历史 (ArenaContext，一个 `Language` 实例) 来维护交互上下文。
    2.  **行为模拟:** `Arena` 的其他行为，如路由，是 `Cognitor` 根据其对文本流（`Language`）和 ACP Textual Arena 规则的**理解和模拟**来执行的。
    3.  **`Language` 基础:** 其交互完全构建在由 `Cognitor` 处理的 `Language` 流之上，整个交互流程和状态变迁都必须通过这些文本记录（`Language` 的载体）来体现。

## 交互
### 认知指令 (Cognitive Directive) 在 Textual Arena 中的表现

在 Textual Arena 中，认知指令 (Cognitive Directive) 是 `Cognitor` 间用于沟通、协作和执行任务的 **`Language` 实例**。Textual Arena 的媒介特性决定了认知指令主要通过文本形式进行传递，其具体表现形式如下：

1.  **自然语言指令 (Natural Language Directives):** 

    *   **定义**: 使用自然语言（如中文、英文等）表达的指令、问题或请求 (一种 `Language` 形式)。
    *   **触发**: 可由 `Cognitor` 自行发起，或由其他 `Cognitor` 通过特定交互模式（如 `chat` 关键字）触发。
    *   **解析**: `Cognitor` 应根据 ACP 协议和其自身的**核心 `Language` 理解能力**对自然语言指令进行理解和解析，并执行相应的操作。
    *   **示例**:
        *   `"请总结一下这篇文章的主要内容。"`
        *   `"chat  你认为接下来应该怎么做？"`
        *   `${User}，请帮我执行这段 Python 命令，我没有可以直接操作的 Python 解释器。`

2.  **NPL 指令 (Natural Pseudo Language Directives):** 

    *   **定义**: 使用 NPL (Natural Pseudo Language) 表达的结构化指令 (一种特殊形式的 `Language`)。NPL 是一种旨在增强指令精确性、降低歧义、并更清晰地**引导 Cognitor 认知过程**的伪代码语言。
    *   **目的**: 提供一种比自然语言更精确、更结构化的方式来表达复杂的认知指令，尤其是涉及对认知概念的操作。
    *   **详细规范**: 详见 [[14.1_npl_directive_representation_protocol]]。
    *   **示例**:
        *   `my_car = Car(); my_car.color = "red";`
        *   `Auto.autolet(my_list.length < 5)`

**区分机制**:

Textual Arena 中的 `Cognitor` **应能够**区分自然语言指令和 NPL 指令。具体的区分机制是 **Cognitor 基于其内在 `Language` 处理能力**自行实现的，并应遵循以下原则：

*   **有效性**: 能够准确地区分两种指令形式。
*   **透明性**: 在 Logs 中记录其区分过程和依据（作为其 `Language` 处理过程的一部分）。
*   **一致性**: 在相同的上下文下，对相同类型的指令应保持一致的判断。

**说明**:

*   区分机制的实现方式不限，可以基于语法模式识别、关键字识别、语义分析等 Cognitor 自身具备的能力。

### 信息表示 (基于 `Language` 衍生的概念)

#### Uncertainty 不确定性实体 (从 `Language` 衍生)
在 Textual Arena 中，`Uncertainty` **不再是独立本体，而是作为 `Cognitor` 处理 `Language` 时遇到的一个状态** 。它表示 `Cognitor` 在理解某段 `Language` 时识别出的**意义可能性空间 或 模糊性**。当 `Cognitor` 面对一个指向 `Uncertainty` 状态的句柄时，它会利用其**语言理解、常识知识和推理能力**来：
	  *   导航这个可能性空间（处理歧义）。
	  *   根据 `ArenaContext` (整体 `Language` 流) 或通过 `add_constraint` 提供的额外 `Language` 信息，聚焦于最相关的含义。
	  *   填充缺失的信息或细节（处理模糊性）。
	  *   生成一个当前看来最合理、最连贯的理解，并通过 `pick`, `to_module` 等方法将其（定性地）表达出来（可能产生 `Forma`）。
  *   因此，在 Textual Arena 中，`Uncertainty` 的管理本质上是**引导 Cognitor 对特定 `Language` 片段进行深度解读和消歧**的过程。其有效性高度依赖于 `Cognitor` 的**语境理解和生成合理推测**的能力。

#### Forma 确定性实体 (从 `Language` 衍生)
在 ACP Textual Arena 中，`Forma` **不再是独立本体，而是作为 `Cognitor` 成功处理一段 `Language` 后的产物**。它通常指 `Cognitor` 从 `Language` 流中提取或生成的、**形式上确定、意义在此刻被固定的信息片段**。例如，从一段描述中解析出的数值、执行 NPL 代码后返回的特定结构数据、或者 Cognitor 生成的明确答复文本。它是 `Language` 认知流处理后的**结果快照或需要进一步处理的确定性输入**。

## 关键协议机制
### Logs (日志系统)

*   **定义** : 在 Textual Arena 中，`Logs` 是 **Cognitor 对其自身处理 `Language` 的认知过程（理解、推理、决策、状态模拟等）进行的部分外化记录**。它由负责执行的 `Cognitor` 以文本形式生成。日志消息通常是自然语言叙述（如 `ReasoningNarrative`），反映了 Cognitor 对其内在活动的**模拟或报告**。这些日志的质量受 Cognitor 能力和意愿影响。

### `meta` (元认知指令关键字)

*   **定义** : 当 `Cognitor` 在 Textual Arena 中遇到 `meta` 关键字时，它被要求**调用其内在的元认知能力，对其自身的 `Language` 处理过程进行反思和报告**。这可能包括分析之前的 `Language` 输出、解释其推理步骤、讨论其对某段 `Language` 理解的局限性、或进行更深层次的上下文关联。这种“元认知”的实现方式是**基于 `Language` 的、表达性的**。