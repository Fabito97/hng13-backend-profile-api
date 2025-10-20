import random
import httpx

fallback_jokes = [
    "Why do Java developers wear glasses? Because they don't C#.",
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "Why do Python devs prefer dark mode? Because light attracts bugs.",
    "Why was the JavaScript developer sad? Because he didn’t know how to 'null' his feelings.",
    "Why did the developer go broke? Because he used up all his cache."
]

async def get_fact():
    fallback_message = f'Sorry, we couldn\'t get facts for you, but here\'s is a joke for you: {random.choice(fallback_jokes)}'
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get('https://catfact.ninja/fact')
            # check if response failed
            if response.status_code != 200:
                print("Failed to fetch fact, using fallback joke.")
                return fallback_message

            fact = response.json().get("fact")  # get fact

            if not fact:  # if fact is None or empty
                print("Fact was empty or None, using fallback joke.")
                return fallback_message

            print("Successfully fetched fact:", fact)
            return fact

    except httpx.HTTPError as e:
        print("Error fetching cat fact:", e)
        print("Falling back to available fact jokes")
        return fallback_message
