#  ACP Textual Arena 协议扩展
## 基本介绍
**ACP Textual Arena** 中的 **ACP 核心协议** 扩展规范。

## 核心原则
ACP Textual Arena 协议设计基于以下核心原则：
*   **纯文本交互**: ACP Textual Arena 的 Arena Context 是纯文本。所有指令、数据和元信息都以且仅以文本形式交换。这意味着即使 `Cognitor` 通过实现 `Arena` 模拟了函数、变量等高级概念，其状态和行为也**必须**通过文本日志进行记录和维护，以确保跨载体的一致性和可审计性。

## 核心实体
### Cognitor (认知执行体)

*   **定义** : 在典型的 Textual Arena 环境中，`Cognitor` 通常是指参与交互的**语言模型（如 ChatGPT）或人类用户** 。它们通过生成和理解文本来进行学习（适应对话流程）、推理（解释指令、生成代码/回答）和元认知（通过 `meta` 触发或内在反思）。其能力表现受限于具体的模型或个人，例如语言模型可能产生幻觉，人类则可能存在认知偏差，这些特性会反映在交互的文本和日志中。`Cognitor Info` 旨在捕获这些具体实例的元信息。

### Arena
*   **定义**: 在 Textual Arena 中，`Arena` 的模拟过程主要通过当前负责执行的 `Cognitor`（通常是语言模型）**生成文本并管理 `Cell` 流**来体现。其运作方式包含以下关键方面：

    1.  **上下文维护:** 它通过解析用户输入和生成输出 ，完全基于可见的文本历史来维护交互上下文。
    2.  **行为模拟:** `Arena` 的其他行为，如自动将自然语言路由给 Fhrsk，是 `Cognitor` 根据对文本流和 ACP Textual Arena 规则的**理解和模拟**来执行的。
    3.  **纯文本基础:** 其“纯文本”特性在 Textual Arena 中表现为文本记录，整个交互流程和状态变迁都必须通过这些文本记录来体现。

## 交互
### 认知指令 (Cognitive Directive) 在 Textual Arena 中的表现

在 Textual Arena 中，认知指令 (Cognitive Directive) 是 `Cognitor` 间用于沟通、协作和执行任务的信息单元。Textual Arena 的媒介特性决定了认知指令主要通过文本形式进行传递，其具体表现形式如下：

1.  **自然语言指令 (Natural Language Directives):**

    *   **定义**: 使用自然语言（如中文、英文等）表达的指令、问题或请求。
    *   **触发**: 可由 `Cognitor` 自行发起，或由其他 `Cognitor` 通过特定交互模式（如 `chat` 关键字）触发。
    *   **解析**: `Cognitor` 应根据 ACP 协议和其自身的认知能力对自然语言指令进行理解和解析，并执行相应的操作。
    *   **示例**:
        *   `"请总结一下这篇文章的主要内容。"`
        *   `"chat  你认为接下来应该怎么做？"`
        *   `${User}，请帮我执行这段 Python 命令，我没有可以直接操作的 Python 解释器。`

2.  **NPL 指令 (Natural Pseudo Language Directives):**

    *   **定义**: 使用 NPL (Natural Pseudo Language) 表达的结构化指令。NPL 是一种旨在增强指令精确性和降低歧义的伪代码语言。它基于 ACP 的 Cognitive Ontology (认知本体)，并采用面向对象的语法结构。
    *   **目的**:  提供一种比自然语言更精确、更结构化的方式来表达复杂的认知指令，尤其是涉及对认知本体中元素的操作。
    *   **详细规范**:  详见 [[11_npl_directive_representation_protocol]]。
    *   **示例**:
        *   `my_car = Car(); my_car.color = "red";`
        *   `Auto.autolet(my_list.length < 5)`


**区分机制**:

Textual Arena 中的 `Cognitor` **应能够**区分自然语言指令和 NPL 指令。具体的区分机制由 `Cognitor` 自行实现，并应遵循以下原则：

*   **有效性**:  能够准确地区分两种指令形式。
*   **透明性**:  在 Logs 中记录其区分过程和依据。
*   **一致性**:  在相同的上下文下，对相同类型的指令应保持一致的判断。

**说明**:

*   区分机制的实现方式不限，可以基于语法规则、关键字识别、语义分析等多种方法。
*   `Cognitor` 可以根据自身的能力和特点选择最合适的区分机制。


### 信息表示

#### Uncertainty 不确定性实体
在典型的 Textual Arena 环境下（主要由语言模型或人类作为 `Cognitor`），`Uncertainty` 通常表现为一个**需要通过自然语言线索和上下文进行认知解读的模糊概念或指代**。当 `Cognitor` 遇到 `Uncertainty` 时，它会利用其**语言理解、常识知识和推理能力**来：
	  *   识别潜在的多种解释或可能性（处理歧义）。
	  *   根据对话历史、周围文本或提供的 `add_data` 信息，推断最相关的含义。
	  *   填充缺失的信息或细节（处理模糊性）。
	  *   生成一个当前看来最合理、最连贯的理解，并通过 `pick`, `to_module` 等方法将其（定性地）表达出来。
  *   因此，在 Textual Arena 中，`Uncertainty` 的处理过程更侧重于**模拟认知层面的不确定性导航**，而非精确的数学计算。其有效性高度依赖于 `Cognitor` 的**语境理解和生成合理推测**的能力。

#### Module 确定性实体
继承于 `Object`

在 ACP Textual Arena 中，Module 通常指一段文本的能指。

## 关键协议机制
### Logs (日志系统)

*   **定义** : 在 Textual Arena 中，`Logs` 由负责执行的 `Cognitor`（主要是语言模型）**以文本形式生成**。日志消息（`message` 字段）通常采用**自然语言叙述**的形式，反映 `Cognitor` 对其自身思考过程的**模拟或报告**（例如，`ReasoningNarrative`）。这些日志的详细程度、准确性甚至客观性会受到 `Cognitor` 能力和“意愿”的影响，可能包含冗余信息或需要通过 `flags` (如 `LLM_PossibleHallucination`) 提示潜在问题。人类 `Cognitor` 通常不会在 Textual Arena 中被要求生成同样详细的外显日志。

### `meta` (元认知指令关键字)

*   **定义** : 当语言模型或人类 `Cognitor` 在 Textual Arena 中遇到 `meta` 关键字时，通常会触发其生成一段**表现出（或模拟出）元认知活动的文本**。对于语言模型，这可能包括分析之前的输出、解释其推理步骤、讨论其理解的局限性、或进行更深层次的上下文关联。对于人类，这可能促使其进行更审慎的思考和表达。这种“元认知”的实现方式是**基于文本的、表达性的**，其深度和质量依赖于具体 `Cognitor` 的能力。