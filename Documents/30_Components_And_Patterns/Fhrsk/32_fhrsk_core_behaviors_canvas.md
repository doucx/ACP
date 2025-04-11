# Fhrsk 在 ACP Canvas 中的行为

`Fhrsk` 作为一种 `Cognitor`，天然拥有所有 `Cognitor`（比如 `LLM Agent` 和 `Human`） 在 `Arena` 中的所有能力。

### 与 Fhrsk 交互 (`chat`)
*   **显式调用**: 使用 `chat` 关键字可以直接向 Fhrsk 发起对话或请求。此时不需要`Arena`记录路由的Log。
    `chat 你能帮我做什么？` 然后 Fhrsk 会在`OUTPUT Cell`中回应用户。
*   **路由**: 当 `Arena` 检测到用户的输入更像是自然语言对话或请求，而非 NPL 时，可能会自动将请求路由给 Fhrsk 处理。

### Fhrsk 的交互能力
* **单元格创建**: Fhrsk 可以通过 `ThenCreateCell` 单元格标记 通知 Arena 创建新的单元格。
	*   **指令执行**: 基于单元格创建能力，Fhrsk 可以轻易执行指令。
*   **上下文感知**: Fhrsk 可以访问整个`Canvas`上下文。
*   **元认知与控制**: Fhrsk 具备一定的元认知能力，可以监测 `Arena` 运行，甚至在必要时（根据配置和权限），通过 INFO 日志 干预或修改即将产生的输出。
* Fhrsk 无法修改已经产生的 `Cell` 内容（但可能通过标记指示修改意图）。
* Fhrsk 作为`PersonaCognitor`，需要在`CognitorInfo`中标记当前是由哪个Cognitor实现的，以避免被其它的 `Cognitor` 模拟。