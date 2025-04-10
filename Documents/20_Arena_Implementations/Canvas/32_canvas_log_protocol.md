# ACP 日志条目格式
本规范定义了 ACP Canvas 中日志条目的推荐结构，旨在同时适应人类 Cognitor 的输入习惯和当前主流 LLM Cognitor 的实际输出特性（如倾向于自然语言叙述、难以提供精确内部状态、可能存在幻觉等），同时保持足够结构化以供分析。

## 日志条目结构

每个日志条目应包含以下字段：

1.  **`originator`** (String, **必需**)
    *   产生此日志的 实体 的唯一标识符。
    *   *示例:* `"ChatGPT-XYZ123"`, `"Alice111"`, `"Python-310"`

2.  **`type`** (Enum, **可选**)
    *   产生此日志的 实体 的类型。
    *   *示例:* `"Cognitor", "Tool", "InterfaceCognitor"`
	    * 默认值： "`Cognitor`"

3.  **`log_level`** (Enum, **必需**)
    *   日志级别: `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`.

4.  `log_number` (String, **必需**)
	- 当前日志在同层级日志中的序号。

5.  **`message`** (String, **必需**)
    *   日志的核心内容。
    * **对于 Cognitor，此字段预期主要是自然语言文本。** 它应该尽可能真实地记录 Cognitor 提供的“思考”或说明。

6.  **`log_entry_type`** (Enum, **推荐**)
    *   提供日志内容的语义分类，帮助理解条目意图。推荐值包括：
        *   `Observation`: 记录观察到的事实、数据或外部事件。
        *   `ActionPlan`: 描述计划执行的动作或 ACP 语句。
        *   `Interpretation`: 对观察结果或信息的解读。
        *   `Hypothesis`: 提出的假设或可能性。
        *   `ReasoningNarrative`: **主要用于 LLM/Human**，以自然语言形式叙述的思考过程、推理链或分析步骤。这是容纳“口语化”输出的核心类型。
        *   `DecisionRationale`: **主要用于 Human** (LLM 或可模拟)，为作出的某个决策提供的理由。
        *   `SelfCorrection`: 对先前错误认知的修正记录。
        *   `ConfidenceReport`: 对某结论或过程的置信度的主观陈述（通常需要被提示或自愿提供）。
        *   `MetaDataChange`: 记录配置变更等元数据事件。
        *   `ExternalInput`: 记录通过 `input()` 等方式获取的外部输入。
        *   `ToolOutput`: 记录调用外部工具（Function Call）的返回结果。
        *   `FhrskAnnotation`: Fhrsk 对其他日志条目添加的元注释。
        *   `SystemEvent`: Arena 内部事件。

7. **`flags`** (List[String], 可选)
    *   用于标记此日志条目的特殊状态或引起注意，可由 Cognitor 自行添加或由 Arena/Fhrsk 监控添加。
    *   *推荐标志:*
        *   `LLM_PossibleHallucination`: 提示此 LLM 生成的 `message` 内容可能不完全基于事实，需要谨慎对待（可能由 Fhrsk 或外部验证机制标记）。
        *   `LLM_SelfCorrection_Prompted`: 表明 LLM 的修正是被明确提示后发生的。
        *   `Human_LowConfidence`: 人类用户标记自己对该条日志内容的信心不足。
        *   `InconsistentWithContext`: 系统检测到此条目与之前的日志或上下文存在逻辑矛盾。
        *   `NeedsHumanReview`: 标记此条目或相关流程需要人工介入检查。
        *   `Routing`: 标记接下来会路由到其它 Cognitor。
    *  *Notebook特有标识:*
        *  `CellCreateNeed`: 标记需要创建一个`Cell`。

注：使用了`log_number`代替了难以由`Cognitor`获取的`timestamp`。

具体日志示例( 类xml，省略大部分内容)：
```xml
<log originator="Fhrsk" type="InterfaceCognitor" log_level="INFO" log_number="42">
  <message>
	在分析用户查询时，我识别到需要获取用户位置信息，我需要询问用户所在城市。
	接下来，我将执行 `city_info = input("你在什么城市")` 来获取用户城市信息。
  </message>

  <log_entry_type value="ReasoningNarrative"/>
  <flags>
	<flag value="CellCreateNeed"/>
  </flags>
</log>
```

示例(shell-like，即将废弃)：
```
INFO[42]: 
	在分析用户查询时，我识别到需要获取用户位置信息，我需要询问用户所在城市。
    接下来，我将执行 `city_info = input("你在什么城市")` 来获取用户城市信息。
```

## 设计考量与应用

*   **拥抱自然语言:** `message` 字段优先考虑容纳 Human 和 LLM 自然产生的语言表达。
*   **结构源于元数据:** 日志的可分析性主要来自丰富的元数据（ID, Type, Timestamp, Level, Context, EntryType, Flags），而非强制内容格式化。
*   **区分来源与意图:** `cognitor_type` 区分了是谁，`log_entry_type` 帮助理解他/它想表达什么。
*   **处理不确定性与风险:** `flags` 字段提供了一个机制来标记和管理日志信息的不确定性，特别是针对 LLM 的潜在幻觉问题。
*   **灵活性:** 该格式旨在提供一个通用框架，具体的 `log_entry_type` 和 `flags` 可以根据应用场景进行扩展。

这种格式试图在“让 Cognitor (特别是 LLM 和人) 舒适地表达”与“让系统能够有效理解和分析日志”之间取得平衡。
