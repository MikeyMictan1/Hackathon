from uagents import Agent, Context

# Create an agent named Alice
crystal = Agent(name="crystal", seed="CRYSTAL HAS NO NEW PHRASES")


# Define a periodic task for Alice
@crystal.on_interval(period=2.0)
async def say_hello(ctx: Context):
    ctx.logger.info(f'hello, my name is {crystal.name}')


# Run the agent
if __name__ == "__main__":
    crystal.run()
