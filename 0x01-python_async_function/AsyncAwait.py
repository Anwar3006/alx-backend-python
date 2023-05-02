import asyncio

#structure:
async def name():
    print("This prints first")
    something = "I got this from the name() coroutine"
    return something


async def age():
    yearOfBirth = 1998
    return yearOfBirth

# Await is where you tell your coroutine function execution to 
# suspend and pass control to another coroutine

# when you call a coroutine youll have to use await infront of it

# async def main():
#     variable = await name()
#     print(variable)

# in the above coroutine main calls on name; name will eventually return an object
# have to await that object to finish so we retrieve it; assign to variable and print

# to run the program:
# asyncio.run(main())


# run two coroutines in parallel
# async def main():
#     var1, var2 = await asyncio.gather(
#         name(),
#         age()
#     )
#     print(var1)
#     print(var2)

# asyncio.run(main())

#start coroutine without waiting
# async def main():
#     task = asyncio.create_task(name())
#     # do something here; normal execution
#     print("________/\_______")
#     await task
#     var1 = task.result()
#     print(var1)

# asyncio.run(main())