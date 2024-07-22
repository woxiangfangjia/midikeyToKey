# MIDI to Keyboard Mapper

这个Python脚本可以将MIDI键盘上的C4到C6音符（不包含半音）映射到计算机键盘的字母输入。当按下或松开一个琴键时，计算机会相应地模拟按键输入和释放。

## 依赖

- Python 3.x
- mido
- python-rtmidi
- pynput

## 安装

首先，确保你已经安装了Python 3.x，然后使用`pip`安装必要的库：

```bash
pip install mido python-rtmidi pynput
```

## 使用方法

1. **连接你的MIDI键盘**: 确保你的MIDI键盘已连接到计算机，并且能够被识别。
2. **获取MIDI设备名称**: 使用以下代码获取你的MIDI设备名称：
    ```python
    import mido
    print(mido.get_input_names())
    ```
    这会输出所有可用的MIDI输入设备名称。找到你的MIDI键盘的名称。

3. **修改脚本中的设备名称**: 打开`midi_to_keyboard.py`脚本，将以下行中的`'你的MIDI设备名称'`替换为你的实际设备名称：
    ```python
    midi_input = mido.open_input('你的MIDI设备名称')
    ```

4. **运行脚本**: 在终端中运行该脚本：
    ```bash
    python midi_to_keyboard.py
    ```

5. **开始演奏**: 当你在MIDI键盘上按下或松开C4到C6范围内的琴键时，计算机键盘会相应地模拟字母输入。

## 代码说明

以下是脚本的主要代码：

```python
import mido
from pynput.keyboard import Controller, Key

# 创建一个键盘控制器对象
keyboard = Controller()

# 打开MIDI输入
midi_input = mido.open_input('你的MIDI设备名称')

# 定义MIDI音符到字母的映射（只包括自然音）
note_to_char = {
    60: 'a',  # C4
    62: 'b',  # D4
    64: 'c',  # E4
    65: 'd',  # F4
    67: 'e',  # G4
    69: 'f',  # A4
    71: 'g',  # B4
    72: 'h',  # C5
    74: 'i',  # D5
    76: 'j',  # E5
    77: 'k',  # F5
    79: 'l',  # G5
    81: 'm',  # A5
    83: 'n',  # B5
    84: 'o',  # C6
    86: 'p',  # D6
    88: 'q',  # E6
    89: 'r',  # F6
    91: 's',  # G6
    93: 't',  # A6
    95: 'u',  # B6
    96: 'v',  # C7
}

# 监听MIDI输入，并转换为键盘按键
for msg in midi_input:
    if msg.type == 'note_on' and msg.velocity > 0:
        note = msg.note
        if note in note_to_char:
            char = note_to_char[note]
            keyboard.press(char)
    elif (msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0)):
        note = msg.note
        if note in note_to_char:
            char = note_to_char[note]
            keyboard.release(char)
```
