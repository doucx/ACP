#  ACP Textual Space 协议扩展
## 基本介绍
**ACP Textual Space** 中基于 **ACP 核心协议** 的扩展规范。

## 核心原则
ACP Textual Space 协议设计基于以下核心原则：
*   **纯文本交互 (`Sign` 流)**: ACP Textual Space 本质上是**结构化文本 (`Sign`) 的流动**。所有指令、数据和元信息都以文本形式（作为 `Sign` 的载体）交换。`Cognitor` 的核心活动是处理这些文本 `Sign`，利用其结构和上下文作为**约束 (`Constraint`)** 来管理和消解其引发的**意义不确定性 (`Referent`)**。
* 即使 `Cognitor` 模拟了高级概念，如 NPL 中的类，其状态和对 `Referent` 的管理过程也**必须**通过认知轨迹 (`Cognitive Trace`，以 `Sign` 形式记录) 进行记录和维护，以确保跨 `Cognitor` 的一致性和可审计性。
*   **`Representamen`-`Constraint`-`Referent` 核心**: 整个 Textual Space 的运作都建立在 `Cognitor` 应用可见的文本形式 (`Space.context` `Sign`) 作为约束 (`Constraint`) 来处理意义不确定性 (`Referent`) 的核心过程之上。（见 [[12_language]]）

## 核心实体
### Cognitor (认知实体)

**本质**：参与Textual Space交互的智能实体，包括：
- 大型语言模型（LLM Agent）
- 人类用户

**核心能力**：
1. **文本处理**：理解自然语言和NPL格式的`Sign`
2. **认知功能**：
   - **学习**：适应对话流程
   - **推理**：
     - 应用`Sign`约束解释指令
     - 管理`Referent`
     - 生成响应`Sign`
   - **元认知**：
     - 监控自身的`Referent`管理过程
     - 通过`Cognitive Trace`报告认知活动

**限制**：具体能力取决于模型版本或个人水平  
**元信息**：通过`Cognitor Info`描述其初始特征（`Sign`形式）

### Space (认知交互空间)

**运作原理**：当前活跃的`Cognitor`通过以下流程驱动交互：
1. **输入处理**：解析输入的文本流（`Sign`序列）
2. **认知活动**：
   - 应用约束条件（`Constraint`）
   - 管理不确定性（`Referent`）
3. **输出生成**：
   - 产生新文本（`Sign`）
   - 记录认知轨迹（`Cognitive Trace`）

**核心特征**：

1. **上下文维护机制**
   - 通过历史文本流（含先前`Cognitive Trace`）构建上下文
   - 这些历史`Sign`构成主要隐式约束来源

2. **行为模拟规则**
   - 路由和状态转换基于对文本流和ACP规则的理解
   - 本质是解决"下一步行动"的不确定性
   - 决策过程必须记录在`Cognitive Trace`中

3. **文本基础性**
   - 所有交互都通过`Sign`实现：
     - 传递约束条件
     - 管理不确定性
     - 记录认知轨迹

4. **操作控制协议**
   - **单线程控制**：同一时间仅允许一个`Cognitor`（操作者）修改Space
   - **显式声明**：必须通过明确指令获取/释放控制权
   - **修改规则**：
     - 禁止修改已有内容
     - 允许追加新认知轨迹来修正记录

5. **观察与响应机制**
   - **实时监控**：所有`Cognitor`可观察Space状态
   - **竞争响应**：当Space释放时：
     - 多个`Cognitor`可同时创建响应
     - 需要响应拼接机制
     - 每个`Cognitor`需维护独立序列号（`seq`）
   - **控制声明**：通过`CT.SPACE`标记获取操作权

## 交互
### 认知指令 (Cognitive Directive) 在 Textual Space 中的表现

在 Textual Space 中，认知指令 (Cognitive Directive) 是 `Cognitor` 间用于沟通、协作和执行任务的 **特定类型的文本 (`Sign`)**。Textual Space 的媒介特性决定了认知指令主要通过文本形式进行传递，其目的是**提供明确的约束 (`Constraint`) 来引导目标 `Cognitor` 管理特定的意义或行动 `Referent`**。其具体表现形式如下：

#### 自然语言 (Natural Language)

*   **定义**: 使用自然语言（如中文、英文等 `Sign`）表达的指令、问题或请求。这类 `Sign` 通常约束性较弱，需要 `Cognitor` 依赖更多上下文 (`Sign`-Constraint) 和推理能力来管理其 `Referent`。
*   **触发**: 可由 `Cognitor` 自行发起，或由其他 `Cognitor` 通过特定交互模式（如 `chat` 关键字，一个提供上下文 `Constraint` 的 `Sign`）触发。
*   **解析**: `Cognitor` 应根据 ACP 协议 (`Sign`-Constraint) 和其自身的**核心语言理解能力**（应用 `Sign` 约束管理 `Referent` 的能力）对自然语言指令 (`Sign`) 进行理解和解析，并将理解过程记录在 `Cognitive Trace` 中，然后执行相应的操作。
*   **示例**:
	*   `"请总结一下这篇文章的主要内容。"` (这段 `Sign` 提供了总结任务的 `Constraint`，指向关于“文章主要内容是什么”的 `Referent`)
	*   `"chat 你认为接下来应该怎么做？"` (这段 `Sign` + `chat` 关键字提供了请求建议的 `Constraint`，指向关于“后续行动方案”的 `Referent`)
	*   `${User}，请帮我执行这段 Python 命令，我没有可以直接操作的 Python 解释器。` (混合 `Sign`，包含委托执行的 `Constraint`)

#### NPL (Natural Pseudo Language):

*   **定义**: 使用 NPL (Natural Pseudo Language) 表达的结构化指令 (`Sign`)。NPL 是一种旨在提供**更强、更明确的结构化 `Sign`-Constraint** 的文本形式，用以增强指令精确性、降低歧义、并更清晰地**引导 Cognitor 管理目标 `Referent`**。
*   **目的**: 提供一种比自然语言更精确、更结构化的方式来表达复杂的认知指令，尤其是涉及对认知概念 (`Referent`/`Sign` 句柄) 的操作。执行过程和结果应通过 `Cognitive Trace` 记录。
*   **详细规范**: 详见 [[14.1_directive_representation_protocol]]。
*   **示例**:
	*   `my_car = Car(); my_car.color = 红色;` (这段 NPL `Sign` 提供了创建对象和设置属性的强 `Constraint`，管理关于 `my_car` 状态的 `Referent`，同时展现了其与自然语言“红色”混合使用的能力)
	*   `Auto.autolet(my_list.length < 5)` (这个 `Sign`-Constraint 引导 `Cognitor` 管理关于 `my_list` 状态的 `Referent`，使其满足长度约束)

#### 混合机制

可以将 **自然语言** 和 **NPL** 的语法混合使用，例如：  

- **在自然语言中嵌入 NPL 表达式**：  
  - 使用 `Symbol("文本")` 或 `cts[X]` 等编程风格的引用。
- **在 NPL 中直接使用自然语言**：
  - 隐含有限列表：如 `for 洲 in 七大洲:`，其中 `七大洲` 是人类可理解的固定集合（亚洲、欧洲等）。  
  - 条件判断：如 `如果 x 大于5且小于10`。

这种混合方式既保持代码的可读性，又能利用自然语言的直观性。

`Cognitor` **应能够** 区分自然语言部分 (`Sign`，弱约束) 和 NPL 部分 (`Sign`，强约束)，并通过认知轨迹来减少不确定性，使认知指令达到可以理解与处理的状态。

### 信息表示 (基于 `Sign` 与 `Referent`)

#### Referent 不确定性实体 (从 `Sign` 约束中浮现)

在 Textual Space 中，`Referent` **是 `Cognitor` 在处理文本 (`Sign`) 时识别出的、需要通过认知活动来消解的意义可能性空间或模糊性**。它不是独立的本体，而是 `Cognitor` 对 `Sign` 应用 `Constraint` 过程中的核心处理对象。当 `Cognitor` 面对一个指向 `Referent` 状态的句柄（通常是一个变量名或一个文本片段）时，它会利用其**语言理解、常识知识和推理能力**来：
    *   评估该 `Referent` 所代表的可能性空间。
    *   根据 `Space` (历史 `Sign` 流作为隐式 `Constraint`) 或通过 `add_constraint` 提供的额外 `Sign` 约束，聚焦于最相关的含义。
    *   运用认知能力（推理、补全）来填充缺失的信息或细节（处理 `Referent` 的模糊性）。
    *   创建一个当前看来最合理、最连贯的理解，并通过 `pick`, `to_module` 等方法将其（定性地）表达出来（通常产生新的 `Sign`）。
    *   整个评估、约束应用和精化过程都应通过 **`Cognitive Trace`** 进行记录。
    *   因此，在 Textual Space 中，`Referent` 的管理本质上是**引导 `Cognitor` 对特定的文本 `Sign` 应用各种 `Sign`-Constraint 进行深度解读、消歧和固化的过程**。其有效性高度依赖于 `Cognitor` 的**语境理解和应用约束创建合理推测**的能力。

#### Representamen 确定性实体 (作为 `Constraint` 或 `Referent` 处理结果)
在 ACP Textual Space 中，`Sign` 扮演双重角色：
1.  **约束 (`Constraint`)**: 文本字符串本身、语言的结构、语法规则、NPL 语句、上下文历史 (`Space` 中的 `Sign`，包括过去的 `Cognitive Trace`) 等，都是形式确定的 `Sign`，被 `Cognitor` 用来**约束和管理 `Referent`**。
2.  **结果 (`Referent` 处理产物)**: 当 `Cognitor` 成功处理一段文本（管理了其 `Referent`）后，**提取或创建的、形式上确定、意义在此刻被固化的信息片段**也是 `Sign`。例如，从一段描述中解析出的数值、执行 NPL 代码后返回的特定结构数据、或者 `Cognitor` 创建的明确答复文本，以及记录这个过程的 `Cognitive Trace` 条目本身。它是 `Referent` 管理过程后的**结果快照或需要进一步处理的确定性输入**。

## 关键协议机制

### Cognitive Trace System (认知轨迹系统)

#### 定义

在 Textual Space 中，`Cognitive Trace` 是 **`Cognitor` 对其自身应用 `Sign` 约束来管理 `Referent` 的认知过程（理解、推理、决策、状态模拟等）进行的部分外化记录**。它由 **操作者** 以文本形式 (`Sign`) 写在 `Space` 中。

`Cognitive Trace` 通常是自然语言叙述（如 `tag="ReasoningNarrative"`），反映了 `Cognitor` 对其内在 `Referent` 管理活动的**报告**。

这些轨迹的质量受 `Cognitor` 能力和意愿影响。详见 [[13_cognitive_trace_protocol.md]]。

同时，`Cognitive Trace` 也作为 `Sign` ，以声明的方式成为了对 `操作者行为` 的强约束。