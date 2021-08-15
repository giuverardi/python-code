# pip install speedtest-cli

import speedtest

test = speedtest.Speedtest()

test.get_servers() # receive list of servers

best = test.get_best_server() #find best server using ping

print(f"Found: {best ['host']} in {best['country']}")

print("Testing download speed...")

download_result = test.download()

print("Testing upload speed...")

upload_result = test.upload()

ping_result = test.results.ping

print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbit/s")

print(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s")

print(f"Ping: {ping_result / 1024:.2f} ms")