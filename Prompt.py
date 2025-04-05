from jinja2 import Environment, FileSystemLoader
import yaml
from pathlib import Path

# 加载配置
with open('config.yaml') as f:
    config = yaml.safe_load(f)

config_snippets = {
    'notebook_agent_name': config['notebook']['agent_name'],
    'notebook_user_name': config['notebook']['user_name'],
}
# 读取所有Markdown片段
prompt_dir = Path('NPL-Documents')
md_snippets = {
    'introduction_and_core_protocol': (prompt_dir / '01_introduction_and_core_protocol.md').read_text(encoding='utf-8'),
    'interactive_environment': (prompt_dir / '02_interactive_environment.md').read_text(encoding='utf-8'),
    'reference_library': (prompt_dir / '03_reference_library.md').read_text(encoding='utf-8'),
    'advanced_concepts': (prompt_dir / '04_advanced_concepts.md').read_text(encoding='utf-8'),
    'log_system': (prompt_dir / '05_log_system.md').read_text(encoding='utf-8'),
    'notebook_example': (prompt_dir / '07_notebook_tiny_example_0.0.x.md').read_text(encoding='utf-8'),
    'appendix_symbols': (prompt_dir / '08_appendix_symbols.md').read_text(encoding='utf-8'),
}

cognitor_dir = Path("Cognitor-Data")
yaml_snippets = {
    'cognitor_info': (cognitor_dir / 'Cognitor.info.yaml').read_text(encoding='utf-8')
}

# 设置Jinja2环境
env = Environment(loader=FileSystemLoader('.'), trim_blocks=True)
template = env.get_template('Prompt-Base.md')

# 合并数据
context = {
    **config_snippets,
    **md_snippets,  # 解包所有Markdown片段
    **yaml_snippets
}

# 渲染结果
output = template.render(context)

# 输出或保存结果
# print(output)
with open('Prompt.txt', 'w', encoding='utf-8') as f:
    f.write(output)
