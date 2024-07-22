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
