import asyncio
import time
import uuid

import httpx


async def send_request(client: httpx.AsyncClient, url: str, index: int):
	headers = {
		"X-Request-ID": str(uuid.uuid4()),  # Optional: if your app reads this
	}

	# Simulate the same multipart/form-data as your curl
	form_data = {
		"username": "vnhd1",
		"password": "string",
	}

	try:
		response = await client.post(url, data=form_data, headers=headers)
		print(f"[{index}] Status: {response.status_code}, Response: {response.text}")
	except Exception as e:
		print(f"[{index}] Error: {e}")


async def run_concurrent_requests(
	url: str,
	total_requests: int = 50,
	concurrency: int = 10,
):
	start_time = time.time()

	async with httpx.AsyncClient(timeout=10) as client:
		semaphore = asyncio.Semaphore(concurrency)

		async def limited_request(index: int):
			async with semaphore:
				await send_request(client, url, index)

		tasks = [limited_request(i) for i in range(total_requests)]
		await asyncio.gather(*tasks)

	duration = time.time() - start_time
	print(f"\nSent {total_requests} requests in {duration:.2f} seconds")


# Example usage
if __name__ == "__main__":
	target_url = "http://localhost:8000/auth/token"
	asyncio.run(run_concurrent_requests(target_url, total_requests=2, concurrency=10))
