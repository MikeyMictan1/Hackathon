from uagents import Agent, Context, Model


# NOTE: Run ReceiverAgent.py before running SenderAgent.py


class Message(Model):
    message: str


ReceiverAgent = Agent(
    name="ReceiverAgent",
    port=8001,
    seed="also a very secret seed",
    endpoint=["http://127.0.0.1:8001/submit"],
)

print(ReceiverAgent.address)


@ReceiverAgent.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    current_count = ctx.storage.get("count") or 0
    ctx.storage.set("count", int(msg.message[-1]) * 2)

    # send the response
    await ctx.send(sender, Message(message=f"The next num is {current_count}"))


if __name__ == "__main__":
    ReceiverAgent.run()
