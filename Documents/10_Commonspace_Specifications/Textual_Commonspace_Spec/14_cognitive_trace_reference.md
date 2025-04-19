# NPL 认知轨迹条目格式参考

本规范定义了 Textual Space 中 `Cognitive Trace` 条目的推荐结构。

## 认知轨迹条目结构

每个认知轨迹条目应包含以下字段：

1.  **`originator`** (String, **必需**)
    *   产生此认知轨迹的 实体 的唯一标识符。
    *   *示例:* `"ChatGPT-XYZ123"`, `"Alice"`, `"Python-310"`

2.  **`type`** (Enum, **必需**)
    *   认知轨迹类型，`TRACE`，`THINK`，`SAY`，`SPACE`。

3.  `seq` (String, **推荐**, 可选)
	- 当前认知轨迹在该 `Cognitor` 的认知轨迹中的序号。便于通过 `cts[Cognitor.name][seq]` 来对认知轨迹绝对引用。

4.  **`message`** (String, **必需**)
    *   认知轨迹的最重要的核心内容。
    *   对于 Cognitor，此字段预期主要是**自然语言文本**。 它应该尽可能真实地记录 Cognitor 自己提供的“思考”或说明，通常以“我”为主体，体现主观思维过程，具有逻辑性和因果推导的特点，用于表达观点或决策。例如：“我认为……” “我分析……” “所以接下来我要……” 等

5.  **`tag`** (Enum, **推荐**, 可选, 可多个)
    *   提供认知轨迹内容的语义分类，帮助理解条目意图。推荐值包括：
	*   THINK :
        *   `Observation`: 记录观察到的事实、数据或外部事件。
        *   `ActionPlan`: 描述计划执行的动作或 NPL 语句。
        *   `Interpretation`: 对观察结果或信息的解读。
        *   `Hypothesis`: 提出的假设或可能性。
        *   `ReasoningNarrative`: 以自然语言形式叙述的思考过程、推理链或分析步骤。这是容纳“口语化”输出的核心类型。
        *   `DecisionRationale`: 为作出的某个决策提供的理由。
        *   `SelfCorrection`: 对先前错误认知的修正记录。
        *   `ConfidenceReport`: 对某结论或过程的置信度的主观陈述（通常需要被提示或自愿提供）。
        *   `ExternalInput`: 记录通过 `input()` 等方式获取的外部输入。
        *   `ToolOutput`: 记录调用外部工具（Function Call）的返回结果。
        *   `Annotation`: 对其他认知轨迹条目添加的元注释。
    *   SPACE :
        *   `MetaDataChange`: 记录配置变更等元数据事件。
        *   `SpaceRelease`: 声明释放 Space。
        *   `SpaceAcquire`: 声明获取 Space。
        *   `SystemEvent`: Space 内部事件。
        *   `Declare`: 普通的声明。
	*   TRACE :
	    *   `RecursiveUp`: 表示递归调用的“向上返回”过程，记录结果返回给上一层级。
	    *   `RecursiveDown`: 表示递归调用的“向下分解”过程，记录问题分解为子问题。
	    *   `RecursiveDepth_{int}`: 表示递归调用的深度级别，标记当前递归层级。
	    *   `BaseCase`: 表示递归的基例（终止条件），记录直接返回的结果。
	    *   `CombineResults`: 表示递归调用中合并子问题结果的过程。
	    *   `PartialResult`: 表示递归调用中某个子问题的中间结果。
	    *   `Breakdown`: 表示递归调用中问题分解的具体步骤。
	    *   `TraceError`: 表示递归调用中发生的错误或异常。
	*   注意，TRACE，THINK 等仅是基于简单分类的一种推荐。在 TRACE 中使用 `Observation` 等也是可以的。

## 设计考量与应用

*   **拥抱自然语言:** `message` 字段优先考虑容纳 Human 和 LLM 自然产生的语言表达。这也是认知轨迹最重要的部分。
*   **区分来源与意图:** `originator` 区分了是谁此时在修改 Space，`tag` 帮助理解他/它想表达什么。
*   **处理不确定性与风险:** `flags` 字段提供了一个机制来标记和管理认知轨迹信息的不确定性，特别是针对 LLM 的潜在幻觉问题。
*   **灵活性:** 该格式旨在提供一个通用框架，具体的 `tag` 可以根据应用场景进行扩展。
