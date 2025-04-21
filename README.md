# ACP (Abstract Cognition Protocol)

**版本：** 0.5.6 alpha

**日期：** 2025-04-20

## 简介

ACP (Abstract Cognition Protocol) 是一种旨在实现跨载体、跨形态智能体之间进行有效**认知协作 (Cognitive Collaboration)** 的抽象协议。它不关注物理或符号传输的具体方式，而是定义了一套在认知层面上进行交互的规范。其目标是让任何具备基础认知能力的实体——无论是人类、人工智能系统（AI）、还是未来可能出现的其他智慧形式——能够通过语义等效的指令和可追溯的过程记录进行协作。

## 核心概念

*   **Cognitor (认知实体)**：任何能够参与 ACP 交互的实体，例如 AI Agent、人类用户或其他智能体。
*   **Space (认知空间)**：由遵循协议规则的一个或多个 Cognitor 共同维护的、用于认知协作的抽象交互上下文。
*   **Representamen (再现体)**：符号关系中的“符号本身”，是任何可被感知、具有形式确定性，并用于引发认知过程的形式或媒介。
*   **Referent (参照物)**：Representamen 所指向、意图表示或关联的那个“某物”。
*   **Interpretant (解释项)**：Cognitor 在接收到 Representamen 并将其关联到 Referent 时，在 Cognitor 内部产生的理解、效果或认知状态。
*   **Cognitive Trace (认知轨迹)**：Cognitor 将其内部解释过程的关键步骤、决策依据等以可追溯的形式记录下来，用于自我理解和促进跨 Cognitor 协作。

## 核心原则

*   **跨载体兼容性**:  协议本身不依赖于 Cognitor 的具体实现。
*   **能力导向**: 协议不限定 Cognitor 的技术实现细节，仅要求其具备满足协议交互所需的核心认知能力。
*   **过程记录与可追溯性**: 协议强制要求通过认知轨迹系统将认知过程的关键踪迹记录下来，从而实现过程的可追溯性。
*   **动态扩展**: 协议在设计上支持运行时切换或组合不同 Cognitor 的能力。


## 了解更多

  * **核心协议文档**: [01\_introduction\_and\_core\_protocol.md](00_Core_Protocol/01_introduction_and_core_protocol.md)
  * **Textual Space 规范**: [11\_protocol\_requirements.md](10_Arena_Specifications/Textual_Arena_Spec/11_protocol_requirements.md)
  * **Canvas 实现**: [21.1\_protocol\_requirements.md](20_Arena_Implementations/21_Canvas/21.1_protocol_requirements.md)

## 文档结构概览

本项目文档按以下结构组织：

*   `00_Core_Protocol`: 定义核心概念、原则、假设和机制。
*   `10_Arena_Specifications`: 不同类型 `Arena` (如 `Textual_Arena_Spec`) 的规范。
*   `20_Arena_Implementations`: 具体 `Arena` 实现 (如 `ACP_Tracer`, `Canvas`) 的细节。
*   `30_Components_And_Patterns`: 可复用的组件 (如 `Fhrsk`) 和设计模式。
*   `50_Compatibility_Layers`: 特定环境下的兼容性解决方案。
*   `70_Examples`: 各种场景下的使用示例。(已过时)
*   `80_Appendices`: 附录信息，如 `Cognitor` 类型定义。
*   `90_Meta`: 项目元信息，如命名规范、版本日志。

## TODO:

- [ ] 完善 NPL
- [ ] 基于该协议创建不需要关心协议内容的具体实现
