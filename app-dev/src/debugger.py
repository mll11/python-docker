import debugpy
import multiprocessing


def initialize_debugger():
    if multiprocessing.current_process().pid > 1:
        debugpy.listen(("0.0.0.0", 10001))
        print("VS Code debugger can now be attached", flush=True)
        debugpy.wait_for_client()
        print("VS Code debugger attached", flush=True)
