# AsyncUserInput

A class that runs as a separate thread for capturing user input asynchronously.

## Usage:
```python
async_input = AsyncUserInput(
    input_callback=callback_function,
    input_function=input,
    name='AsyncUserInput-thread')
async_input.pause()
# (WARNING!: Experimental could cause Problems.) Pauses until resumed.
async_input.resume()
# Resume the input thread.
async_input.start()
# (WARNING!: This is already done automatically).
```

## Arguments:

| Argument              | Description                                                                   | Type                  | Default |
| --------------------- | ----------------------------------------------------------------------------- | --------------------- | ------- |
| **`input_callback`**            | Callback function to be invoked when input is received.                                                  | `function (without `( )`)`                 |         |
| **`input_function`** | The input function to use for capturing user input. | `function (without `( )`)`          |`input`|
| **`name`** |The name of the thread. | `str`|`'AsyncUserInput-thread'` |
## Additional Class Methods:

### `run(self)`

Starts the input capturing loop. Invokes the `input_callback` when input is received.

!!! warning "Done Automatically"

### `pause(self)`

Pauses the input capturing thread.

### `resume(self)`

Resumes the paused input capturing thread.

???+ note "input_callback"
    The class runs as a separate thread and captures user input asynchronously. Make sure to handle the input appropriately in the provided `input_callback` function.

## Example use:
```python
def handle_input(user_input):
    # Handle the received input
    print(f"Received input: {user_input}")

async_input = AsyncUserInput(input_callback=handle_input)
async_input.pause()  # Pauses the input capturing thread
# Perform other tasks...
async_input.resume()  # Resumes the input capturing thread
```