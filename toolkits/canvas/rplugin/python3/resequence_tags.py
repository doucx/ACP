# encoding: utf-8
import pynvim
import re

@pynvim.plugin
class TagResequencer:
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command('ResequenceTags', nargs='0', sync=True)
    def resequence_tags_command(self, *args, **kwargs):
        """
        自动为当前缓冲区中的 ct 和 Node 标签按 origin 和标签类型递增 seq 属性。
        如果 seq 属性不存在，则添加。
        针对不同的 origin 和标签类型组合，使用独立的序列。
        """
        self.resequence_tags() # 调用核心处理方法

    def resequence_tags(self):
            """
            核心逻辑：遍历缓冲区行，查找并修改标签的 seq 属性。
            """
            nvim = self.nvim
            buffer = nvim.current.buffer
            lines = buffer[:] # 获取所有行
            modified_lines = [] # 存储修改后的行
            # 存储每个 (origin, tag_type) 组合的下一个 seq 值
            # Key: (origin, tag_type) 元组, Value: int (下一个序列号，从 0 开始)
            seq_counters = {}

            # 正则表达式匹配 ct 或 Node 标签的起始部分 (不变)
            tag_pattern = re.compile(r'<(ct|Node)(\s*[^>]*?)(\/?>)')
            # 正则表达式匹配 origin 属性及其值 (不变)
            origin_pattern = re.compile(r'origin="([^"]*)"')
            # 正则表达式匹配已存在的 seq 属性及其值 (不变)
            seq_pattern = re.compile(r'seq="[^"]*"')

            # >>> 修改点：新增：正则表达式匹配行首的空白字符（缩进）
            indent_pattern = re.compile(r'^(\s*)')
            # <<< 修改点结束

            # nvim.out_write("开始重新编号 seq 属性...\n") # 打印开始信息

            for i, line in enumerate(lines):
                # >>> 修改点：捕获当前行的缩进
                indent_match = indent_pattern.match(line)
                # group(1) 包含捕获到的缩进字符串，如果行不以空白开头则为空字符串
                leading_indent = indent_match.group(1) if indent_match else ""
                # <<< 修改点结束

                modified_line = line # 默认情况下行内容不变
                match = tag_pattern.search(line) # 在当前行查找匹配

                if match:
                    tag_name = match.group(1) # 'ct' 或 'Node'
                    attributes_part = match.group(2) # 例如 ' origin="User" type="THINK"'
                    closing_part = match.group(3) # '>' 或 '/>'

                    origin_match = origin_pattern.search(attributes_part) # 在属性部分查找 origin

                    # 只处理有 origin 属性的标签
                    if origin_match:
                        origin = origin_match.group(1) # origin 的值，例如 'User'
                        key = (origin, tag_name) # 用于计数器的唯一键

                        # 获取或初始化计数器 (不变)
                        if key not in seq_counters:
                            seq_counters[key] = 0
                        current_seq = seq_counters[key]
                        new_seq_attr_str = f'seq="{current_seq}"'
                        seq_counters[key] += 1

                        # 检查 seq 属性是否已存在并更新属性部分 (不变)
                        seq_match = seq_pattern.search(attributes_part)
                        updated_attributes_part = attributes_part

                        if seq_match:
                            updated_attributes_part = seq_pattern.sub(new_seq_attr_str, attributes_part, count=1)
                        else:
                            if attributes_part.strip():
                                updated_attributes_part = attributes_part + ' ' + new_seq_attr_str
                            else:
                                updated_attributes_part = ' ' + new_seq_attr_str

                        # >>> 修改点：重构整行：在前面加上捕获到的缩进
                        # 将之前捕获到的 leading_indent 拼接到新行的最前面
                        modified_line = f'{leading_indent}<{tag_name}{updated_attributes_part}{closing_part}'
                        # <<< 修改点结束

                modified_lines.append(modified_line) # 将处理后的行添加到列表中

            # 用修改后的内容替换缓冲区的所有行 (不变)
            buffer[:] = modified_lines

            # nvim.out_write("Seq 属性已重新编号完成。\n") # 打印完成信息
