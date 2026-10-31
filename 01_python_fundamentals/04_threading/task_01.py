import threading
import os

current = threading.current_thread()
print("=== PROCESS INFO ===\n", "Process PID: ", os.getpid())
print("=== THREAD INFO ===")
print("Thread name: ", current.name)
print("Thread's ident: ", current.ident)
print("Thread's native_id: ", current.native_id)
print("Is Main Thread: ", current is threading.main_thread())
print("Is Daemon: ", current.daemon)
print("Is Alive: ", current.is_alive())
print("===")
print("=== ACTIVE THREAD ===")
print("Active threads:", threading.active_count())
print("Thread: ", current.name)
