# https://aiosfstream.readthedocs.io/en/latest/quickstart.html
# install: pip3 install aiosfstream
# create connected app in Org: Consumer Key, Consumer Secret


import asyncio

from aiosfstream import SalesforceStreamingClient


async def stream_events():
    # connect to Streaming API
    async with SalesforceStreamingClient(
        consumer_key="3MVG9KsVczVNcM8z.zmkR5nEPO18QbQ8KghCWdTsxsCDnh1C5pXrZ8n4i3C8JiR021l.PYKMeqbk44LtYCh3j",
        consumer_secret="25B64D759EB2E4FDB7629D4C8F62CFE74CCC0E21930F706128E03E3D4F81648F",
        username="lsahlmann+universal-networks@salesforce.com",
        password="2Bfw^uhZ5Y*u"
    ) as client:

        # subscribe to topics
        await client.subscribe("/event/Notification__e")
        # await client.subscribe("/topic/two")

        # listen for incoming messages
        async for message in client:
            topic = message["channel"]
            data = message["data"]
            print(f"{topic}: {data}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(stream_events())