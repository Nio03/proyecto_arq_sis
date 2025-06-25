import asyncio
import json
from datetime import datetime

# Cola global en memoria
_message_queue: asyncio.Queue = asyncio.Queue()


async def send_message(message: dict) -> None:
    """Encola el mensaje y muestra confirmación por pantalla."""
    await _message_queue.put(message)
    print(f"🔄 Encolado (in-memory): {json.dumps(message)}")


async def main() -> None:
    """Produce un evento de ejemplo."""
    sample_event = {
        "event": "case.updated",
        "id": 123,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }
    await send_message(sample_event)

    # (Opcional) consume para demostrar ciclo completo
    queued = await _message_queue.get()
    print(f"✅ Consumido del in-memory queue: {queued}")


if __name__ == "__main__":
    asyncio.run(main())