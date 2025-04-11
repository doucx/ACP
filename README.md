# ACP (Abstract Cognition Protocol)

**Version: 0.3.4**

## 简介

ACP (Abstract Cognition Protocol) 是一种基于认知实体（Cognitor）的抽象认知协作协议。它旨在实现跨载体、跨形态的智能交互，定义了一套认知层面的规范，允许任何具备核心认知能力（学习、推理、元认知）的实体（如人类、AI系统）通过语义等效的指令和透明的过程记录进行协作。

**关键澄清：** ACP **不是** 传统的软件协议（如 HTTP），它作用于认知实体的“思考过程”层面，关注语义可理解性和过程透明性，而非比特级的精确传输。

## 核心概念

*   **Cognitor (认知实体):** 任何具备协议要求的核心认知能力（学习、推理、元认知）的执行实体。协议与其具体形态（AI, 人类）无关。
*   **Cognitive Arena (认知空间):** 一个或多个 Cognitor 交互、协作的抽象环境。它管理交互上下文 (`ArenaContext`) 并协调活动，确保遵循协议（如过程透明性）。
*   **Cognitive Directive (认知指令):** 旨在传达指令、数据或查询的信息单元，强调对目标 Cognitor 的清晰度和可理解性。可以是自然语言或结构化语言（如 NPL）。
*   **Cognitive Ontology (认知本体):**
    *   **Object:** 本体中的最高层抽象基类，代表任何可被思考或讨论的事物。
    *   **Module:** 确定性信息载体（如具体数值、文本、代码、已定义规则）。形式确定，可预测、可验证。
    *   **Uncertainty:** 可管理的不确定状态，通过认知过程逐渐明晰；可以添加约束来缩减可能性空间。
    *   **Logs (日志系统):** 强制性机制，记录关键执行步骤、状态变化和决策依据，确保过程透明和可审计。

## 主要特性

*   **跨载体兼容:** ACP 协议本身不依赖于 Cognitor 的具体实现，理论上可由不同类型 Cognitor 参与和处理。
*   **能力导向:** 协议不限定技术实现细节，仅要求具备核心认知能力（学习、推理、元认知），协议是调用这些能力的接口。
*   **过程可审计:** 强制使用 Logs 实现执行过程透明化，使交互历史、决策路径和状态变化可被追溯和理解。
*   **动态扩展:** 设计上支持运行时切换或组合不同 Cognitor 的可能性（理论层面），以适应复杂任务的需求。
*   **基础可执行性:** 核心协议（定义基本概念、交互流程和日志要求）辅以示例，本身就构成了可运行的基础。

## 项目结构

(请参考 `99_file_naming_conventions.md` 了解详细的文件命名规范)

*   `00_Core_Protocol`: 核心协议定义。
*   `10_Arena_Specifications`: 不同 Arena 类型需要符合的规范。
*   `20_Arena_Implementations`: 具体 Arena 的实现细节
*   `50_Compatibility_Layers`: 不同场景下的兼容处理方案
*   `70_examples`: 示例代码和用法展示.
*   `80_Appendices`: 补充说明和参考.
*   `90_Meta`: 项目结构和版本信息.
## 如何理解与使用

1.  **理解核心概念：** 熟悉 Cognitor、Arena、Uncertainty、Module、Logs 等基本概念。
2.  **阅读规范文档：** 详细阅读核心协议规范，了解 ACP 的基本原则和交互流程（Core_Protocal）。
3.  **参考示例代码：** 学习如何将 ACP 应用于实际场景中，包括建立 Canvas， 与人类 / LLM Agent 交互（Examples）。

## 使用

复制并填充完 `Cognitor-Data/Cognitor.info.yaml`, `config.yaml` 后，使用 `Prompt.py` 生成 `Prompts/Prompt.txt`。

## 贡献

我们欢迎社区贡献！可以贡献代码、文档、示例应用等。

## 版本

当前版本：**0.3.4**

README.md 由 Gemini 自动生成。
