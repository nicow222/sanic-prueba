from aio_pika import connect_robust, Message

async def publish_rabbitmq(queue,body_message):
    # Conectar al servidor RabbitMQ
    connection = await connect_robust(
        "amqp://guest:guest@127.0.0.1/",
    )
    async with connection:
        channel = await connection.channel()

        await channel.default_exchange.publish(
            Message(body=body_message.encode()),
            routing_key=queue,
        )