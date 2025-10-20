import random
import asyncio
import httpx

fallback_jokes = [
    "Why do Java developers wear glasses? Because they don't C#.",
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "Why do Python devs prefer dark mode? Because light attracts bugs.",
    "Why was the JavaScript developer sad? Because he didn’t know how to 'null' his feelings.",
    "Why did the developer go broke? Because he used up all his cache."
]

async def get_fact(max_retries: int = 3, backoff_base: float = 0.5):
    fallback_message = f"Sorry, we couldn't get facts for you, but here's a joke for you: {random.choice(fallback_jokes)}"

    for attempt in range(1, max_retries + 1):
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get("https://catfact.ninja/fact")

                if response.status_code != 200:
                    print(f"[Attempt {attempt}] Failed with status {response.status_code}")
                    raise httpx.HTTPStatusError("Non-200 response", request=response.request, response=response)

                fact = response.json().get("fact")
                if not fact:
                    print(f"[Attempt {attempt}] Empty fact received")
                    raise ValueError("Empty fact")

                print(f"[Attempt {attempt}] Successfully fetched fact: {fact}")
                return fact

        except (httpx.HTTPError, ValueError) as e:
            print(f"[Attempt {attempt}] Error: {e}")
            if attempt < max_retries:
                sleep_time = backoff_base * (2 ** (attempt - 1))
                print(f"Retrying in {sleep_time:.1f}s...")
                await asyncio.sleep(sleep_time)
            else:
                print("Max retries reached. Falling back to joke.")
                return fallback_message
