import threading


class AsyncUserInput(threading.Thread):
    """
    ### A class that runs as a separate thread for capturing user input asynchronously.

    #### Usage:
    ```py
        async_input=AsyncInput(input_cbk=callback_function).
        async_input.pause() # (WARNING!: Experimental could cause Problems.) Pauses until resumed.
        async_input.resume() # Resume the input thread.
        async_input.start() # (WARNING!: This is already done automatically).
    ```
    #### Args:
    ```py
        input_cbk: Callback function to be invoked when input is received.
    ```
    """

    def __init__(self, input_callback, input_function=input, name: str='AsyncUserInput-thread'):
        self.input_callback=input_callback
        self.input_function=input_function
        self.paused=False
        self.pause_cond=threading.Condition(threading.Lock())
        super(AsyncUserInput, self).__init__(name=name)
        self.start()

    def run(self):
        while True:
            with self.pause_cond:
                while self.paused:
                    self.pause_cond.wait()
                self.input_callback(self.input_function())

    def pause(self):
        self.paused=True
        self.pause_cond.acquire()

    def resume(self):
        self.paused=False
        self.pause_cond.notify()
        self.pause_cond.release()
