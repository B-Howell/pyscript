from pyscript import display

# This function simulates a long-running task
def long_running_task():
    import time
    time.sleep(5)  # Simulating delay
    return "Task completed!"

# Display output in a specific DOM element
display(long_running_task(), target="worker-output")
