# Abstract Cognition Protocol (ACP) - v0.4.0 beta 4

## 1. ACP 是什么？

**ACP (Abstract Cognition Protocol)** 是一种旨在实现**跨载体、跨形态智能体**（如人类、AI Agent 等）之间进行有效**认知协作 (Cognitive Collaboration)** 的抽象协议。

它不关注具体的物理或数字传输细节，而是定义了一套在**认知层面**进行交互的规范。ACP 的核心目标是解决以下问题：

> **“当两个或多个认知实体对同一信息 (`Forma`) 的内在理解 (`Uncertainty`) 可能存在偏差时，如何通过协议设计来确保它们能够收敛到协作所需的语义共识，并使协作过程本身可被理解和信任？”**

通过规范交互流程并强制要求过程透明化，ACP 试图为不同心智之间的深度协作建立桥梁。

## 2. 核心概念

ACP 围绕以下核心概念构建：

*   **Cognitor (认知实体):** 任何具备协议所要求的基础认知能力（感知、行动、理解、推理、元认知）的参与者。可以是人类、AI Agent 或其他智慧形式。ACP 旨在调用和协调这些能力。
*   **Cognitive Arena (认知空间):** 由 `Cognitor` 共同维护的、用于认知协作的抽象环境。它管理着交互上下文 (`ArenaContext`)。
*   **ArenaContext (认知上下文):** `Arena` 中由交互产生的、可访问的 `Forma` 记录流，是所有协作的基础。
*   **Forma (确定性实体):** 具有明确形式、可被直接观察或处理的信息载体（如文本、指令、数据）。构成 `ArenaContext` 的基本单元，也是施加约束的来源。
*   **Uncertainty (不确定性实体):** 标记信息中需要通过认知过程来明确的部分。`Cognitor` 通过施加基于 `Forma` 的**约束 (`Constraint`)** 来管理和消解 `Uncertainty`。
*   **Cognitive Trace (认知轨迹):** 取代原 "Logs"概念。`Cognitor` 内部认知活动（思考、决策、状态变化模拟、元认知反思等）的关键步骤，以结构化 `Forma` 形式记录下来的结果性输出。它是实现过程透明性的核心机制。
*   **`meta` (元认知调用关键字):** 一个标准的 `Forma` 关键字，用于请求 `Cognitor` 调用其内在的元认知能力进行反思，并将结果记录到 `Cognitive Trace` 中。

## 3. 核心原则

ACP 的设计遵循以下原则：

*   **跨载体兼容 (Cross-Carrier Compatibility):** 协议不依赖于 `Cognitor` 的具体实现。
*   **能力导向 (Capability-Oriented):** 协议调用 `Cognitor` 的内在认知能力，而非提供它们。
*   **过程透明性 (Process Transparency):** **强制**通过 `Cognitive Trace` 系统记录关键认知过程，确保可审计性和可理解性。

## 4. 主要优势

采用 ACP 旨在带来以下优势：

*   **结构化协作:** 为不同智能体（人与 AI，AI 与 AI）提供了一个通用的协作框架，超越简单的问答或指令执行。
*   **增强的可审计性与可信度:** 强制性的 `Cognitive Trace` 记录使得协作过程和决策路径可以被追溯和审查，有助于建立信任和理解。
*   **异构智能体互操作性:** 潜在地促进拥有不同能力、知识背景和实现方式的 `Cognitor` 进行更深层次的整合与协作。
*   **明确的语义基础:** 通过 `Forma`/`Uncertainty`/`Constraint` 本体论，为处理模糊性和歧义提供了显式框架。
*   **人类兼容:** 人类可以直接参与，协议原则可映射到良好的团队协作实践中。

## 5. 潜在限制与当前挑战

作为一个探索性的协议框架，ACP 目前也面临一些限制和挑战：

*   **模拟器依赖:** 当前 `Arena` 的逻辑（特别是 `Canvas` 实现中的状态机、路由等）主要依赖于 `Cognitor` (通常是 LLM Agent) 的**模拟和理解**来实现。这可能导致行为的不一致性，且难以保证严格遵守协议规则。
*   **`Cognitive Trace` 的可靠性:** 虽然协议强制要求记录 `Cognitive Trace`，但其内容的**真实性、完整性和无偏性**在很大程度上仍依赖于生成它的 `Cognitor`。特别是对于 LLM Agent，其生成的“思考过程”可能是模拟的或存在幻觉，而非其真实的内部状态反映。
*   **人类认知外化难度:** 要求人类 `Cognitor` 像 AI 一样详尽地记录其内在思考过程是困难且不自然的，需要在协议应用中找到平衡。
*   **复杂性与开销:** 引入 `Cognitive Trace` 等机制增加了交互的复杂度和信息量，可能带来额外的理解和处理开销。
*   **标准化程度:** 协议仍在发展中，一些细节（如 `CognitorInfo` 的标准格式、`Cognitive Trace` 的具体结构建议、跨 `Cognitor` 委托的细节实现）还需要进一步标准化。

## 6. 文档结构概览

本项目文档按以下结构组织：

*   `00_Core_Protocol`: 定义核心概念、原则、假设和机制。
*   `10_Arena_Specifications`: 不同类型 `Arena` (如 `Textual_Arena_Spec`) 的规范。
*   `20_Arena_Implementations`: 具体 `Arena` 实现 (如 `ACP_Tracer`, `Canvas`) 的细节。
*   `30_Components_And_Patterns`: 可复用的组件 (如 `Fhrsk`) 和设计模式。
*   `50_Compatibility_Layers`: 特定环境下的兼容性解决方案。
*   `70_Examples`: 各种场景下的使用示例。(已过时)
*   `80_Appendices`: 附录信息，如 `Cognitor` 类型定义。
*   `90_Meta`: 项目元信息，如命名规范、版本日志。

## 7. 当前状态

*   **版本:** 0.4.0 beta 4
*   **状态:** 活跃开发与迭代中。核心概念已初步稳定，正在探索具体实现和应用模式。欢迎反馈和贡献！

TODO:

- [ ] 完善 NPL
- [ ] 基于 NPL 创建 ACP Tracer
