from uagents import Agent, Context, Model


class Message(Model):
    message: str

RECIPIENT_ADDRESS = (
    "test-agent://agent1qwd7pz864fkj82rtu0pg64yazw6jd3v8p2mh4gpnrmdat05xtcsf7sw5676"
)

SenderAgent = Agent(
    name="SenderAgent",
    port=8000,
    seed="this is a very unique seed",
    endpoint=["http://127.0.0.1:8000/submit"],
)

print(SenderAgent.address)


@SenderAgent.on_interval(period=30.0)
async def send_message(ctx: Context):
    current_count = ctx.storage.get("count") or 0
    await ctx.send(RECIPIENT_ADDRESS, Message(message=f"The num is {current_count}"))



@SenderAgent.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    current_count = ctx.storage.get("count") or 0
    print(int(msg.message[-1]))
    ctx.storage.set("count", int(msg.message[-1]) * 3)
    await ctx.send(RECIPIENT_ADDRESS, Message(message=f"The num is {current_count}"))



if __name__ == "__main__":
    SenderAgent.run()
