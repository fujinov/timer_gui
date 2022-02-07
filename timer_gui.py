import pathlib

import PySimpleGUI as sg


sg.theme('DarkBrown1')
path = pathlib.Path('user_set.txt')

def set_time():
    layout = [[sg.Text('タイマーをセットします', size=(None, 2))],
              [sg.Spin([m for m in range(61)], size=2, font=(None, 15)), sg.T('分'),
                sg.Spin([s for s in range(60)], size=2, font=(None, 15)), sg.T('秒')],
              [sg.VPush()],
              [sg.Checkbox('デフォルトとして設定する', key='-DEFAULT-')],
              [sg.OK(), sg.Cancel()]]

    window = sg.Window('セットタイマー', layout, size=(250, 160) ,element_justification='center')

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        user = (0, 0)
    elif event == 'OK':
        user  = (values[0], values[1])
        if values['-DEFAULT-'] == True:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(f'{values[0]} {values[1]}')
    window.close()
    return user

set_time()