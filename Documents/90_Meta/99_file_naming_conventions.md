# 文件命名规范

本规范定义了 ACP 项目中文档的文件命名规则，旨在确保整个项目结构清晰、易于管理。

1.  **编号**:
    *   文件名以两位数字编号开头，指示文件类别和顺序。
    *   编号与目录结构中的编号对应，便于快速定位文件。

2.  **分隔符**:  使用下划线 `_` 分隔编号、文件名和扩展名。

3.  **文件名**:
    *   使用小写字母和下划线描述文件内容，力求简洁明了。
    *   避免使用含糊不清的缩写或专业术语。

4.  **扩展名**: 所有文档使用 `.md` (Markdown) 作为扩展名。

**类别编号:**

*   **00**: **核心协议**.  定义 ACP 的基本概念、架构和核心机制。  对应 `00_Core_Protocol` 目录。
*   **10**: **领域规范 (Arena Specifications)**. 描述不同类型 Arena 领域需要符合的规范。 对应 `10_Arena_Specifications` 目录.
     *       一级子目录`Textual_Arena_Spec`, `Visual_Arena_Spec`等  描述更加细化的分类
*   **20**: **领域实现 (Arena Implementations)**. 提供具体领域环境的实现细节。  对应 `20_Arena_Implementations` 目录。
     *       一级子目录`Canvas`,  `Shell` 等  描述更加细化的分类
*   **50**: **兼容性层**. 处理特定场景下的兼容性问题。  对应 `50_Compatibility_Layers` 目录。
*   **70**: **示例**. 展示 ACP 的使用方法和效果。  对应 `70_examples` 目录.
     *       一级子目录`shell`,  `canvas` 等  描述更加细化的分类
*   **80**: **附录**.  提供补充信息、参考资料等。 对应 `80_Appendices` 目录。
*   **90**: **元信息**.  描述项目结构、版本历史等元数据. 对应 `90_Meta` 目录.

**示例:**

*   `00_introduction_and_core_protocol.md`:  核心协议的介绍和定义。
*   `11_protocol_requirements.md`:  Textual Arena 需要遵循的协议规范。
*   `31_canvas_protocol.md`:  Canvas 的协议实现细节。
