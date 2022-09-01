import sys
import reliance.global_vars

VERSION = '1.0.1'
VERSION_NO = 13

reliance.global_vars.VERSION = VERSION
reliance.global_vars.VERSION_NO = VERSION_NO

if __name__ == "__main__":

    import multiprocessing
    import os
    import reliance.core
    import reliance.interface.commandline

    if sys.platform != "win32":
        import fcntl

    run_gui = reliance.interface.commandline.parse_interface()

    multiprocessing.freeze_support()

    if run_gui:
        if sys.platform == "win32":
            try:
                os.remove(os.path.join('misc', 'temp', 'lock'))
            except PermissionError:
                print('重复调用，不启动')
                sys.exit(1)
            except FileNotFoundError:
                pass

        guard = open(os.path.join('misc', 'temp', 'lock'), 'w')
        if sys.platform != "win32":
            try:
                fcntl.lockf(guard, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except IOError:
                print('重复调用，不启动')
                sys.exit(1)

        print('正在启动程序，请最小化本窗口，操作期间勿直接关闭本窗口，会随主窗口关闭而关闭')
        import reliance.interface.gui
        talk_core = reliance.core.core()
        reliance.interface.gui.tkinter_gui(talk_core)
    else:
        talk_core = reliance.core.core(no_projects=True)
        cmd_ui = reliance.interface.commandline.CmdUI(talk_core)
        cmd_ui.execute_command()

