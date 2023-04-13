from aio_pika import connect_robust, Message
import os

rabbitmq_host = os.environ.get('RABBITMQ_HOST', '127.0.0.1')
async def publish_rabbitmq(queue,body_message):
    # Conectar al servidor RabbitMQ
    connection = await connect_robust(
        f"amqp://guest:guest@{rabbitmq_host}/",
    )
    async with connection:
        channel = await connection.channel()

        await channel.default_exchange.publish(
            Message(body=body_message.encode()),
            routing_key=queue,
        )