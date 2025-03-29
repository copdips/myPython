# https://docs.python.org/3/library/contextvars.html#contextvars.Context.run
import contextvars

var = contextvars.ContextVar("var")
var.set("spam")
print(var.get())  # 'spam'

ctx = contextvars.copy_context()
id


def main():
    id
    # 'var' was set to 'spam' before
    # calling 'copy_context()' and 'ctx.run(main)', so:
    print(var.get())  # 'spam'
    print(ctx[var])  # 'spam'

    var.set("ham")

    # Now, after setting 'var' to 'ham':
    print(var.get())  # 'ham'
    print(ctx[var])  # 'ham'
    id
    return "return from main"


""""
# ! The key point is that when you call ctx.run(main), any modifications to context
variables are isolated to that specific execution context.
When you access the variable through the context object using ctx[var],
you see the modified value 'ham'.
Any changes that the 'main' function makes to 'var'
will be contained in 'ctx'."

# ! Explicit Context Switching: Using ctx.run() creates a new isolated environment
# ! Inheritance: New contexts inherit values from their parent context
# ! Local Mutations: Changes are contained within the current context

# ! Implicit Context Switching occurs automatically in asynchronous programming environments like asyncio. The system manages context switching for you:

```python title="example for implicit context switching inside an async function"
async def task():
    # Context variables are automatically preserved when you await
    var.set("value")
    await asyncio.sleep(1)  # Context switch happens here implicitly
    # When execution returns, the context is automatically restored
    print(var.get())  # Still "value"
```

run(callable, *args, **kwargs)
Enters the Context, executes callable(*args, **kwargs), then exits the Context.
Returns callable's return value, or propagates an exception if one occurred.
"""
ret = ctx.run(main)
print(f"ret: {ret}")  # ret: return from main

# The 'main()' function was run in the 'ctx' context,
# so changes to 'var' are contained in it:
print(ctx[var])  # 'ham'

# ! However, in the global execution context (outside of ctx.run(main)),
# the original value 'spam' is preserved. This is why var.get() returns 'spam'
# at the end - you're accessing the variable from the global context,
# not from inside the ctx context where it was modified.
print(var.get())  # 'spam'
