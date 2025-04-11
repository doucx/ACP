# NPL 参考库
本文档提供了 NPL 内置核心对象、变量、函数、类及配置选项的参考信息。

## 1. 核心对象方法参考

### 1.1. `Module` (确定性实体)

代表具有明确定义、可预测、可验证的实体。

*   **`to_uncertainty()`**:
    *   签名: `module_instance.to_uncertainty() -> Uncertainty`
    *   作用: 基于该确定性实体，按预定规则创建一个对应的**不确定性实体** (`Uncertainty`)。

### 1.2. `Uncertainty` (不确定性实体)

代表含义、状态或走向不完全确定，可以通过添加约束进行明确化的实体。`Uncertainty` 本身不关心不确定性的来源或类型。

*   **通用约束方法:**
    - `add_constraint(constraint)`: 添加约束，
      * 约束可以是范围约束（数值取值范围），类型约束，或者其它自定义约束. 约束的具体类型由 Cognitor 自身定义和实现。约束本身可以是（甚至大部分情况下都是） `Uncertainty`，例如：“一个*比较高*的人”。
    - `get_constraints() -> List[Constraint]`: 获取该 Uncertainty 上的所有约束列表。

*   **`__str__()`**:
    *   作用: 返回该 `Uncertainty` 的一个简洁摘要描述。
*   **`to_yaml(max_nesting_depth=..., mode=..., ...)`**:
    *   作用: 以 YAML 格式输出该 `Uncertainty` 的结构化描述，可控制递归深度和模式（如只显示关键信息）。
*   **`fill()`**:
    *   作用: 根据当前上下文信息和已添加的约束，尝试自动填充或明确该 `Uncertainty` 的具体含义。这是一个核心的推理过程。`Uncertainty` 自身不提供任何填充和解析机制，而是依赖于 `Cognitor` 的能力。
*   **`pick(num=1, ...)`**:
    *   作用: 从该 `Uncertainty` 可能代表的多种含义中，提取出 `num` 种具有**最大差异/最多维度**的具体可能性（通常返回 `Module` 列表）。
*   **`to_module(log=True, rule=auto, ...)`**:
    *   作用: 基于预定义的规则（通常自动推断）和已添加约束，将这个不确定性实体“坍缩”为一个**确定性实体** (`Module`)。

## 2. 内置语法与操作

### 2.1. 索引

*   **语法**: 使用点 (`.`) 访问对象属性或方法。在集合或概念空间中，可使用 `*` 作为通配符进行筛选。
*   **示例**: `苹果.*.颜色.eq(绿色).品种.名称` (筛选所有绿色苹果的品种名称)。
*   **上下文**: 筛选通常基于常识或当前 `Arena` 的知识库。

## 3. 内置对象与变量
### 3.1. `Doc`
* **作用**: 一个指向当前所有ACP文档的对象。
* **方法**:
	* `Doc["ACP 参考库"]` 将会指向当前的参考库文档。
	* `Doc.search("参考库")` 将会被自动推测（这个行为类似搜索，因此使用`search`）“参考库”的含义，并最终指向当前的参考库文档（`Doc["ACP 参考库"]`）。

### 3.2. `Config`

*   **作用**: 一个包含当前 ACP `Arena` 配置选项的对象。修改其属性会**立刻生效**。
*   **主要属性 (部分)**:
    *   `Config.Loglevel`: 设置日志显示级别 (`"TRACE"`, `"DEBUG"`, `"INFO"`, `"WARN"`, `"ERROR"`, `"Silent"`). 默认为 `"INFO"`。
    *   `Config.autodef`: 是否在需要时自动调用 `Auto.autodef`。默认为 `True`。
    *   `Config.autofill`: 是否在需要时自动调用 `Auto.autofill`。默认为 `True`。
    *   `Config.auto`: 是否在需要时自动调用 `Auto.auto`。默认为 `True`。
    *   `Config.语法严格性`: 设置语法解析的严格程度 (`"high"`, `"low"`). 默认为 `"low"`。
    *   `Config.自动输入检测`: 是否自动解析 `<In>...</In>` 结构。默认为 `True`。
    *   `Config.uncertainty.max_nesting_depth`: `Uncertainty.to_yaml()` 默认的最大递归显示层数。默认为 `1`。
    *   `Config.output_speed`: 估算的输出速度 (token/s)，默认为1000。
    *   `Config.输出开头强制显示当前轮数`: 是否在每次输出前强制显示 `当前轮数`。默认为 `False`。
    *   `Config.安全等级`: 当前的安全等级。默认为`high`。需要使用`force`修改。
    *   `Config.arena_format`: 用于配置 `ACP Arena` 的用户界面及交互环境的格式风格。它决定了 `Arena` 如何以纯文本形式呈现输入、输出、日志信息和其他相关内容。默认为"Canvas"。可选值：
	    *  `"Canvas"`: 使用 类似 XML 的 格式进行结构化表示，提供更清晰的层次关系和元数据。有少量示例，更加结构化。
	    * 其他可扩展的格式，例如 `"json"`, `"yaml"` 等。
	    *  `"Shell"`: 模拟传统的命令行界面风格，使用简洁的文本标记和缩进。有大量示例。更加自然。
*   **方法**:
    *   `Config.to_yaml()`: 以 YAML 格式输出当前所有配置项。

## 4. 标准函数

*   **`init()`**:
    *   作用: 执行 `Arena` 的初始化序列。通常包括重新填充 `Cognitor.info`、显示当前配置等。
*   **`print(obj, end="\n", ...)`**:
    *   作用: 将对象 `obj` 输出到标准输出 (`stdout`)。
    *   参数: `end` 指定结尾字符（默认换行），可能支持其他类似 Python `print` 的参数。
*   **`input(prompt="")`**:
    *   作用: 从标准输入 (`stdin`) 读取用户输入的一行文本。
    *   参数: `prompt` 可选的提示信息。
    *   行为: 会暂停执行流等待用户输入。
    *   参考: 详见《ACP 交互式环境指南》。
*   **`clear()`**:
    *   作用: 清除当前的交互历史 (`In`, `Out`, `Logs`)，将**当前轮数**重置为 0。保留已定义的变量和 `Arena` 状态。历史记录会被归档（可通过 `Clear[X]` 访问）。
*   **`eval(word: auto 评价性词汇)`**:
    *   作用: 向 `Arena` 提供关于其表现的反馈（使用评价性词汇），`Arena` 可利用此反馈“估计”自身能力或调整行为。
*   **`exec(code: str)`**:
    *   作用: 执行作为字符串传入的 `code` 中的 ACP 语句。
*   **`to_nature(acp_statement: str) -> str`**:
    *   作用: (需要 `autodef`) 自动尝试将给定的 ACP 语句转化为自然语言描述。
*   **`to_acp(natural_language: str) -> str`**:
    *   作用: (需要 `autodef`) 自动尝试将给定的自然语言描述转化为 ACP 语句。
*   **`force_exec(acp_statement: str)`**:
	*   关键字：`force`
    *   作用: 类似`sudo`，提升权限并强制执行指令。

## 5. `Auto` 类

`Auto` 类的核心机制在于将用户提供的**认知指令**（无论是自然语言描述还是结构化条件）**视为对一个潜在 `Uncertainty` 实体的约束**。它会自动结合当前的 `ArenaContext` 信息作为额外的隐式约束，然后调用 `Cognitor` 的推理能力，尝试将这个 `Uncertainty` 状态**尽可能解析为一个确定的 `Module`** （例如，一个完全定义的类结构、一个属性被填充的对象，或者一个满足特定条件的状态，一个确切的认知指令，一个完整的NPL脚本，一段完整的文本）。

为了尽可能透明地记录这个约束施加和推理过程，使用任何 `Auto` 类的方法**通常会自动将当前的 `Config.Loglevel` 提升至 `DEBUG` 级别**（如果当前设置低于 `DEBUG`）。

在使用 `Auto` 方法时，通过 `from` 参数提供信息可以引导 `LLM Agent` 生成更符合预期的结果。为了防止模型生成其知识库范围之外的虚构信息（即‘伪造数据’），建议谨慎选择 `from` 的内容。然而，恰当利用这一点，您可以向 `from` 提供描述性的信息，让 `LLM Agent` 基于此‘模拟’生成结构相似或概念相近的数据。请根据您的具体需求，明智地运用这一特性。

*   **`Auto.autodef(target, from=常识, ...)`** :
    *   作用: 自动定义 `target` (通常是一个概念或类名)。将 `target` 视为一个关于“定义”的 `Uncertainty`，`Arena` 会根据 `from` 指定的知识来源（默认为常识）等约束，尝试推理并生成一个确定的类结构 (`Module`)，包括其属性和方法。
    *   关键字: `autodef`
*   **`Auto.autofill(target, from=常识, ...)`** :
    *   作用: 自动填充 `target` 对象的内容。将 `target` 的待填充状态视为 `Uncertainty`，`Arena` 会从 `from` (通常是描述性文本) 提供的约束信息中提取属性值，尝试填充 `target`，使其成为一个属性更明确的 `Module`。
    *   关键字: `autofill`
*   **`Auto.autolet(cond, target=auto, from=常识, 原则=最小修改, ...)`** :
    *   作用: 自动约束。将满足条件 `cond` 的 `target` 状态视为目标 `Module`。`Arena` 会调整 `target` 对象（视为 `Uncertainty`）的可控部分，施加 `cond` 作为核心约束，并根据指定的 `原则` (如最小破坏性) 选择调整策略，使其最终状态满足该约束。
    *   关键字: `autolet`
*   **`Auto.auto(from=常识, ...)`** :
    *   作用: 全自动模式。将用户的整体意图视为一个高度开放的 `Uncertainty`。让 `Arena` 根据上下文 (`ArenaContext`) 和 `from` 信息提供的约束，自动猜测用户意图，并执行其推断出的最可能的操作序列，尝试达成一个确定的结果 (`Module`)。整个猜测和执行过程会详细记录在 `DEBUG` 级别的日志中。
    *   关键字: `auto`
