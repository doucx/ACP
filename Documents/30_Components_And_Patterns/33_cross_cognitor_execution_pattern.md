# ACP 模式: 跨认知实体执行委托 (Cross-Cognitor Execution Delegation)

## 1. 模式概述

此模式定义了一种机制，允许一个 Cognitor (请求者) 请求另一个 Cognitor (执行者) 在其特定的环境或利用其独特的能力来执行一个任务（通常是指令或代码），并返回结果。这使得 ACP 交互能够超越单个 Cognitor 或 Arena 模拟环境的限制，实现能力的互补与协作。

**核心场景:**
*   AI Cognitor 请求 Human Cognitor 执行需要物理世界交互或访问本地环境的命令（如操作本地文件、运行特定软件、访问硬件）。
*   一个 Cognitor 请求另一个拥有特定专业知识库或计算资源的 Cognitor 执行专门的计算或推理。
*   Human Cognitor 委托 AI Cognitor 执行大规模数据处理或复杂模拟。

## 2. 协议机制 (Canvas 实现建议)

为了在 ACP Canvas 中实现此模式，建议对核心协议进行以下扩展：

**2.1. 扩展 `<Node type="EXEC">` 定义:**
   (参见 `20_Arena_Implementations/Canvas/23_canvas_implementation.md` 中的具体修改)

   为 `<Node type="EXEC">` 增加**可选属性**：

   *   `target_cognitor` (文本, 可选): 指定期望执行此 Node 内容的目标 Cognitor 的标识符。
   *   `execution_context` (文本, 可选): 描述目标 Cognitor 应在何种上下文或环境执行指令。

   **示例:**
   ```xml
   <Node originator="Fhrsk" seq="2" type="EXEC" target_cognitor="AyeL" execution_context="local_fish_shell">
       <value>uname -a</value>
   </Node>
   ```

**2.2. Arena 行为扩展:**
   (应在 Arena 实现中体现，并在 `20_Arena_Implementations/Canvas/23_canvas_implementation.md` 中描述)

   当 Arena 遇到带有 `target_cognitor` 属性的 `EXEC` Node 时：
   1.  **识别与路由**: Arena 识别出这是一个执行委托请求，不内部执行。
   2.  **请求传递**: Arena 将执行请求传递给指定的 `target_cognitor`。
   3.  **状态等待**: Arena 进入等待状态，期望 `target_cognitor` 回应包含结果的 Node。
   4.  **结果处理**: 收到响应后，Arena 将结果传递回原始请求者或继续流程。

**2.3. 执行者 (Target Cognitor) 职责:**

*   接收 Arena 转发的执行请求。
*   根据 `execution_context` 在指定环境中执行 `<value>` 指令。
*   将结果封装在一个或多个新的 Node 中（通常是 `OUTPUT` 类型），并通过 `<depends_on>` 关联原始请求。
*   在响应 Node 的 `<log>` 中记录执行过程。

## 3. 优点

*   **能力扩展**: 扩展 ACP 系统能力，利用不同实体的优势。
*   **虚实结合**: 打通虚拟认知空间与物理/本地环境的交互。
*   **灵活性与效率**: 将任务分配给最适合的执行者。

## 4. 注意事项

*   **安全性**: 需要权限控制机制，执行者应可拒绝请求。
*   **标准化**: `execution_context` 需要逐步标准化以提高互操作性。
*   **错误处理**: 需明确失败报告和处理机制。
*   **日志记录**: 执行者需记录关键步骤和结果。

