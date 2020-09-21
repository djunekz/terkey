import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'

def setup():
    try:
        os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
        pass
    key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(key)
    os.system('termux-reload-settings')


def banner():
    os.system('clear')
    print(a+'Tombol Shortcut buat para newbie'.center(40))
    print(b+'Djunekz'.center(40))
    print("".join([i for i in "\n"*3]))


if __name__=='__main__':
    banner()
    from threading import Thread as td
    t = td(target=setup)
    t.start()
    while t.is_alive():
        for i in "-\|/-\|/":
            print('\rPlease wait '+i+' ',end="",flush=True)
            sleep(0.1)
    banner()
    print(c+'Silahkan lihat-lihat script lainnya '+a+'https://github.com/djunekz'+c+' jika ada yang mau di bicarakan terkait tool ini, bisnis atau sekedar bertanya kabar. \nTerimakasih ^_^')

# ini cuma shortcut buat bantu para newbie
# D J U N E K Z
