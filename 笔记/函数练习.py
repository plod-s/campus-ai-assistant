'''
写一个函数 `count_text`：

- 必传参数：`text`（字符串）
- 可选参数：`mode`，默认值为 `"char"`
  - `mode="char"`：返回文本的字符总数（包含空格）
  - `mode="word"`：返回文本的单词数量（按空格分割）
- 调用测试：分别用位置参数、关键字参数调用，测试两种模式

**进阶要求**：如果传入空字符串，直接返回 0，做好边界处理。
'''


def count_text(text, mode="char"):
    if mode == '':
        return 0
    print('text')
    print('mode')

    if mode == 'char':
        return len(text)
    elif mode == 'word':
        return 0


