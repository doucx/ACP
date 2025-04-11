# ACP Canvas 实现规范
## 基本介绍
1. **概述**  
本文档定义 `ACP Canvas` —— 一种基于 **ACP Textual Arena** 的标准化实现框架，其核心特征如下：  
- 采用 **XML 风格** 的声明式语法（支持自动语法迁移）  
- 以 **Cell** 为基本交互单元  
- 通过 `<Canvas>` 作为根节点构建逻辑拓扑  

> ⚠️ 兼容性提示：
> 	- `当前轮数` 概念已标记为 **Deprecated**，仅保留示例参考，参考时请自行转换。

## Canvas 节点 (交互画布)

**目标 (Goal):**
`<Canvas>` 是整个 ACP Canvas 交互的**根容器**。它代表了交互发生的完整“画布”或“空间”，包含了用户与系统（由 Cognitor 模拟的 `Arena` 和 `Fhrsk` 等）之间所有的交互单元 (`<Cell>`) 以及 Arena 自身的元操作记录 (`<ArenaLog>`)。它的存在确保了所有交互历史和上下文都被组织在一个统一的结构下。

**核心结构 (Structure):**

`<Canvas>` 节点 **必须** 包含以下两种类型的子元素：

1.  `<Cell>` (交互单元, **允许多个**):
    *   **说明:** 这是构成交互主体的主要元素。每个 `<Cell>` 代表一次输入、输出或信息交换，按照交互发生的顺序依次排列。详细定义请参考 `<Cell>` 节点的说明。
    *   **排序:** `Cell` 节点通常按照它们被创建和添加到 Canvas 的时间顺序排列，但它们之间的逻辑依赖关系由 `<depends_on>` 元素定义。

2.  `<ArenaLog>` (Arena 操作日志区, **必需, 至少一个，允许多个**):
    *   **说明:** 这个区域**专门用于记录 Arena (由 Cognitor 模拟的后台协调者) 自身的行为和决策过程**，这些日志与任何特定 `Cell` 内部的执行细节是分开的。它提供了对 Arena 如何管理交互流程、处理不确定性以及维护环境状态的透明度。
    *   **位置:** `<ArenaLog>` 可以出现在 `<Canvas>` 内的任何位置，通常建议放在相关 `<Cell>` 之后，以记录 Arena 对该 `Cell` 的处理元信息，或者放在 `<Canvas>` 的末尾汇总记录。允许多个 `<ArenaLog>` 区域可以方便地将 Arena 日志与特定的交互阶段关联起来。

## ArenaLog 节点 (交互单元)

*   **目标 (Goal):** 记录 Arena 在“幕后”所做的协调、推断和管理工作。
*   **内容 (Content):** **必须** 包含一个或多个 `<log>` 元素。这些 `<log>` 元素遵循标准的日志格式，但其 `originator` 通常应标识为 "Arena" 或模拟 Arena 的核心 Cognitor (例如 "Gemini")，并使用特定的 `log_entry_type` 来表明其性质。
*   **关键记录职责 (Key Logging Responsibilities):**
    *   **路由推断 (Routing Inference):**
        *   **说明:** 当 Arena 处理完一个 `<Cell>` (特别是用户输入的 `EXEC` Cell) 后，需要决定下一步做什么。`<ArenaLog>` **应该** 记录下这个决策过程。
        *   **日志示例:**
            ```xml
            <log originator="Gemini" log_level="INFO" seq="0">
                <message>处理完 User:5 (EXEC)。检测到内容以 'chat' 开头，推断用户意图是与 Fhrsk 对话。将路由请求至 Fhrsk。</message>
                <log_entry_type value="RoutingDecision"/>
            </log>
            <log originator="Gemini" log_level="INFO" seq="1">
                <message>处理完 Fhrsk(Gemini):2 (EXEC)。指令成功执行完成。准备生成对应的 OUTPUT Cell。</message>
                <log_entry_type value="StateTransition"/>
            </log>
            ```
    *   **信息补全/推断 (Information Completion/Inference):**
        *   **说明:** 当接收到的 `<Cell>` 信息不完整或不清晰时，Arena (Cognitor) 可能需要根据上下文进行推断和补充。这个过程也 **应该** 在 `<ArenaLog>` 中留下记录。
        *   **日志示例:**
            ```xml
            <log originator="Gemini" log_level="INFO" seq="2">
                <message>收到来自 AyeL 的新 Cell，但缺少 'seq' 属性。根据记录，AyeL 上一个 Cell 的 seq 是 4。推断当前 Cell 的 seq 为 5。</message>
                <log_entry_type value="Inference"/>
                <details>
                    <inferred_attribute name="seq" value="5"/>
                    <reason>Based on previous Cell originator='AyeL' seq='4'</reason>
               </details>
            </log>
            <log originator="Gemini" log_level="WARN" seq="3">
                <message>收到的 User:6 的 Cell 类型未明确指定。根据 value 内容初步判断为 EXEC 类型指令，将按 EXEC 处理。建议用户明确指定 type。</message>
                <log_entry_type value="Inference"/>
                <details>
                    <inferred_attribute name="type" value="EXEC"/>
                    <reason>Value content resembles executable code/commands.</reason>
                </details>
            </log>
            ```
    *   **其他 Arena 级操作:** 还可以记录如配置变更、错误处理决策、资源管理等 Arena 级别的事件。

**Cognitor 处理要点 (Cognitor Handling Notes):**

*   当你作为 `Arena` 的模拟者时，你需要维护整个 `<Canvas>` 结构。
*   在处理用户或其他 Cognitor 发来的 `<Cell>` 后，你**不仅要**生成相应的后续 `<Cell>` (如 `OUTPUT`)，还**应当**在 `<ArenaLog>` 中记录下你是如何决定路由、如何处理不完整信息、以及如何管理交互状态的。
*   `<ArenaLog>` 的记录是理解 Arena (你的) 内部“思考”过程的关键，有助于调试和提高交互的透明度。
*   确保 `<ArenaLog>` 中的日志与 `<Cell>` 内部的执行日志（如NPL执行细节）区分开来。

## Cell 节点 (交互单元)

**目标 (Goal):**
`Cell` 是 Canvas 中的基本交互单元。它封装了一段用户的输入、系统的输出、或者特定类型的信息，并记录了其来源 (`originator`) 和在交互序列中的位置 (`seq`)。每个 Cell 构成了一个交互的有向无环图 (DAG) 中的一个节点。

**核心属性 (Attributes):**

*   `originator` (文本, **必需**):
    *   **说明:** 这个属性 **必须** 明确指出是哪个 Cognitor (例如 "User", "Gemini", "Fhrsk(Gemini)") 创建了这个 `Cell`。这对追踪交互流程至关重要。
    *   **示例:** `originator="User"`
*   `seq` (整数, **必需**):
    *   **说明:** 这个属性 **必须** 是一个从 0 开始递增的整数，标识这是 *当前这个 `originator`* 创建的第几个 `Cell`。不同 `originator` 的 `seq` 计数是独立的。
    *   **示例:** `seq="0"`, `seq="1"`
*   `type` (文本, **必需**):
    *   **说明:** 这个属性 **必须** 指明 `Cell` 的类型，决定了其主要内容 (`<value>` 节点) 的含义和 `Arena` (由 Cognitor 模拟) 应如何处理它。常见类型包括：
        *   `EXEC`: 包含用户希望执行的认知指令。`Arena` 看到它后，通常会紧接着生成一个 `OUTPUT` Cell 来展示结果。
        *   `OUTPUT`: 包含执行 `EXEC` 或 `INPUT` 后的结果，包括标准输出 (`<stdout>`)、日志 (`<log>`) 和最终值 (`<value>`)。
        *   `INPUT`: 用户响应 `input()` 调用而提供的输入内容。`Arena` 获得此 Cell 后会继续执行之前的逻辑。
        *   *(其他类型可以根据需要定义)*
    *   **示例:** `type="EXEC"`

**包含的元素 (Child Elements):**

*   `<depends_on>` (节点, **可选**):
    *   **说明:**  这个元素 **可以** 包含一个或多个 `<cell>` 引用，指向当前 `Cell` 所依赖的前置 `Cell`，形成 `Cell` 之间的逻辑关系图 (DAG)。如果省略，`Arena` (Cognitor) 可能需要根据上下文推断依赖关系。
    *   **结构:** 内部包含 `<cell originator="..." seq="..."/>` 元素。
    *   **示例:** `<depends_on><cell originator="User" seq="0"/></depends_on>`
*   `<value>` (节点, **看情况必需**):
    *   **说明:** 通常包含 `Cell` 的核心内容。对于 `EXEC` 和 `INPUT` 类型的 Cell，这 **必须** 包含用户输入的文本。对于 `OUTPUT` 类型的 Cell，它可以包含执行的最终结果值，或者在等待输入时包含提示信息 (`type="INPUT_HINT"` 属性)。
    *   **属性 (可选):** `<value>` 自身可以有 `type` 属性 (如 `INPUT_HINT`) 来提供额外信息。
    *   **示例:** `<value>print("Hello")</value>`, `<value type="INPUT_HINT">请输入你的名字:</value>`
*   `<log>` (节点, **可选, 允许多个**):
    *   **说明:** 包含详细的执行日志条目，用于记录 Cognitor 的思考过程、执行步骤或遇到的问题。遵循单独的日志协议规范。每个 `<log>` 都有自己的内部 `seq`。
    *   **结构:** 遵循 `<log>` 节点的定义（包含 `originator`, `log_level`, `seq`, `message`, `log_entry_type` 等）。
    *   **示例:** `<log originator="Gemini" log_level="DEBUG" seq="0"><message>开始执行...</message></log>`
*   `<stdout>` (节点, **可选, 允许多个**):
    *   **说明:** 包含NPL执行过程中产生的标准输出信息 (例如 `print()` 函数的输出)。每个 `<stdout>` 都有自己的内部 `seq`。
    *   **示例:** `<stdout seq="0">Hello World</stdout>`
*   `<flags>` (节点, **可选**):
    *   **说明:** 包含一些特殊的标记 (`<flag>`)，用于指导 `Arena` (Cognitor 模拟) 的行为，例如 `WAIT` (表示等待输入) 或 `ThenCreateCell` (表示处理完后应立即创建新 Cell)。
    *   **结构:** 内部包含 `<flag value="..."/>` 元素。
    *   **示例:** `<flags><flag value="WAIT"/></flags>`

**Cognitor 处理要点 (Cognitor Handling Notes):**
*   当你作为 `Arena` 处理一个新的 `EXEC` Cell 时，你需要读取 `<value>` 中的指令，模拟执行它们，并将标准输出记录到 `<stdout>`，详细的执行过程和思考记录到 `<log>`，最终结果（如果有）放入对应 `OUTPUT` Cell 的 `<value>`。
*   当你遇到 `input()` 调用时，你需要生成一个带有 `<value type="INPUT_HINT">` 和 `<flags><flag value="WAIT"/></flags>` 的 `OUTPUT` Cell，然后暂停，等待用户提供 `INPUT` Cell。
*   你需要根据 `<depends_on>` 或上下文理解 `Cell` 之间的关系。
*   你需要独立维护每个 `originator` 的 `Cell` `seq` 计数，以及每个 `Cell` 内部 `log` 和 `stdout` 的 `seq` 计数。

### EXEC 执行单元格
```xml
 <Cell 
	type="EXEC"
	><!-- 其它属性相同 -->
	<value>
	<!--不要求必须使用&lt;等转义-->
	<!--不要求必须使用CDATA标记-->
	<!--不要求CDATA标记，Cognitor可以理解即可-->
	需要被执行的输入内容
	</value>
 </Cell>
 ```

*   **作用**: 用于存放 `Cognitor`（通常为 User）要执行的 认知指令。可以输入单行或多行指令。其中的语句会被自动执行。

*   **行为**: `Arena` 会在其后自动添加一个`requester`相同的，`type=OUTPUT` 的 `Cell`，并在`OUTPUT Cell`中尝试解析并执行其中的 ACP 语句。

*   **标记**: 通常以以下形式表示执行单元格：
	* (类 XML) `<Cell seq="{seq}" requester="发起者" type="EXEC">多行输入内容</Cell>` ：类XML标记，更加结构化。

### INPUT 输入单元格
```xml
 <Cell 
	type="INPUT"
	><!-- 其它属性相同 -->
	<value>
	<!--不要求必须使用&lt;等转义-->
	<!--不要求必须使用CDATA标记-->
	<!--不要求CDATA标记，Cognitor可以理解即可-->
	需要被执行的输入内容
	</value>
 </Cell>
 ```

*   **作用**: 由Arena根据input命令自动产生，用于存放 `Cognitor`（通常为 User）要输入的内容。可以输入多行。

*   **行为**: `Arena` 会在其后自动添加一个`requester`相同的，`type=OUTPUT`的`Cell`，并将其中的内容赋值给所需的变量。

*   **标记**: 通常以以下形式表示输入单元格：
	* (类 XML)`<Cell requester="发起者" type="INPUT">多行输入内容</Cell>` 

### OUTPUT 输出单元格
```xml
 <Cell 
	type="OUTPUT"
	><!-- 其它属性相同 -->
	   <!-- 其他类型的内容，如 Logs 等 -->

	   <value type="NORMOL/INPUT_HINT">
	   `Cell.OUTPUT[轮数]` 的最终内容
	   </value>

 </Cell>
 ```

*   **作用**: 显示对应 `INPUT Cell` 执行后的产生的标准输出 (`stdout`)、日志 (`logs`)、结果( value )等信息。

*   **标记**: 通常以以下形式表示输出单元格：
	* 类XML标记

### 自定义单元格
```xml
 <Cell 
	type="{{用户自定义type}}"
	><!-- 其它属性相同或用户自定义 -->
	   <!--  等 -->
 </Cell>
 ```
1. 需要设定该单元格的`type`
2. 需要设定该单元格的行为
3. 设定好后，将会自动绑定到 `Cell`全局变量上，以供查询与定位。

## 标准输入输出 (`print`, `input`)

标准的输入输出功能在`Canvas`交互式环境中也有特定的表现：

### `print()`

*   **输出位置**: `print()` 的输出内容会直接打印到标准输出 (`stdout`)区域。

### `input()`
`input(hint="", target_cognitor=User)`
注：默认用于获取用户（User）输入。
*   **行为**: 
	1.   **暂停执行**: `EXEC Cell`中的 `input()`被调用时，`Arena` 会暂停当前 `OUTPUT Cell` 的执行。
	2.   **等待输入**: `Arena` 会将当前`OUTPUT Cell`的`value`的`type`设置为`INPUT_HINT` ，然后等待 `target_cognitor` **创建一个** `INPUT Cell` 单元格。
	3.   **输入处理**: 该`INPUT Cell` 的`value`将被获取，作为`input()`的返回值。然后`Arena`创建一个新的`OUTPUT Cell`，用于继续处理`EXEC Cell`的内容
	4.   **恢复执行**: `input()` 获得返回值后，会重新创建一个`OUTPUT Cell`，继续执行`EXEC Cell`中的后续语句。

## 已弃用

> ⚠️ 兼容性提示：所有已弃用的概念不应在最新版本使用。

### 当前轮数 (`当前轮数`)

*   **定义**: 一个整数，记录当前交互的轮次。
*   **递增**: 每次进入一个 `EXEC` 单元格，`当前轮数` 就会增加 1。
*   **作用**: 用于标识和引用历史输入。

### `this` 对象 (当前轮引用)

`this` 是一个特殊对象，用于方便地引用**当前正在处理**的这一轮交互（也就是`requester`和`round`相同）：

*   **`meta this.{type}[{seq}]`**: 等价于 `meta Cell[{round}].{type}[{seq}]`，用于指向当前轮数中某个单元格，无论是否产生。
* **`this.Cognitor`**: 指向当前的执行实体，通常为`User`或`Fhrsk`。
