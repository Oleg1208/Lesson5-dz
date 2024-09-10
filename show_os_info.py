import os
import platform
def show_os_info():
    """Выводит информацию об операционной системе."""
    print(f'Операционная система: {platform.system()}')
    print(f'Версия: {platform.release()}')
    print(f'Архитектура: {platform.architecture()[0]}')