
# import sys
# import requests

# def main():

#     if len(sys.argv) != 2:
#         sys.exit("Missing command-line argument")

#     try:

#         bitcoins = float(sys.argv[1])
#     except ValueError:
#         sys.exit("Command-line argument is not a number")

#     try:

#         response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
#         response.raise_for_status()
#         data = response.json()
#         price = data["bpi"]["USD"]["rate_float"]
#     except requests.RequestException:
#         sys.exit("Error fetching Bitcoin price")


#     total_cost = bitcoins * price
#     print(f"${total_cost:,.4f}")

# if __name__ == "__main__":
#     main()


# import sys
# import requests

# def main():
#     if len(sys.argv) != 2:
#         sys.exit("Missing command-line argument")

#     try:
#         bitcoins = float(sys.argv[1])
#     except ValueError:
#         sys.exit("Command-line argument is not a number")

#     try:
#         response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
#         response.raise_for_status()
#         data = response.json()
#         price = data["bpi"]["USD"]["rate_float"]
#         total_cost = bitcoins * price
#         print(f"${total_cost:,.4f}")
#     except (requests.RequestException, KeyError, ValueError):
#         sys.exit("Error fetching Bitcoin price")

# if __name__ == "__main__":
#     main()


# import sys
# import requests

# # Check if the correct number of arguments is provided
# if len(sys.argv) != 2:
#     sys.exit("Missing command-line argument")

# # Try to convert the argument to a float
# try:
#     n = float(sys.argv[1])
# except ValueError:
#     sys.exit("Command-line argument is not a number")

# # Replace 'YourApiKey' with your actual CoinCap API key
# api_key = '8e4b733bb90e6853a9de07597893458068f8e42c79cdc7bd49da2beeed0aa0b3'
# url = f'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

# try:
#     # Make the API request
#     response = requests.get(url)
#     response.raise_for_status()  # Raise an exception for HTTP errors
#     data = response.json()

#     # Extract the price of Bitcoin in USD
#     price_per_btc = data['bitcoin']['usd']

#     # Calculate the total cost
#     total_cost = price_per_btc * n

#     # Format the output with a thousands separator
#     print(f"${total_cost:,.4f}")

# except requests.RequestException as e:
#     sys.exit(f"Error fetching Bitcoin price: {e}")


# import sys
# import requests

# # Check for command-line argument
# if len(sys.argv) != 2:
#     sys.exit("Missing command-line argument")

# # Check if argument is a valid number
# try:
#     n = float(sys.argv[1])
# except ValueError:
#     sys.exit("Command-line argument is not a number")

# # Public API URL (no API key required)
# url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

# try:
#     # Make the API request
#     response = requests.get(url)
#     response.raise_for_status()  # Raise an exception for HTTP errors

#     # Parse the JSON response
#     data = response.json()

#     # Extract the price of Bitcoin in USD
#     price_per_btc = data["bitcoin"]["usd"]

#     # Calculate the total cost
#     total_cost = price_per_btc * n

#     # Format the output with a thousands separator
#     print(f"${total_cost:,.4f}")

# except requests.RequestException as e:
#     sys.exit(f"Error fetching Bitcoin price: {e}")
# except KeyError:
#     sys.exit("Error: Unexpected API response format.")



# import sys
# import requests

# # Check for command-line argument
# if len(sys.argv) != 2:
#     sys.exit("Missing command-line argument")

# # Check if argument is a valid number
# try:
#     n = float(sys.argv[1])
# except ValueError:
#     sys.exit("Command-line argument is not a number")

# # Public API URL (no API key required)
# url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

# try:
#     # Make the API request
#     response = requests.get(url)
#     response.raise_for_status()  # Raise an exception for HTTP errors

#     # Parse the JSON response
#     data = response.json()

#     # Extract the price of Bitcoin in USD
#     price_per_btc = data["bitcoin"]["usd"]

#     # Calculate the total cost
#     total_cost = price_per_btc * n

#     # Format the output with a thousands separator
#     print(f"${total_cost:,.4f}")

# except requests.RequestException as e:
#     sys.exit(f"Error fetching Bitcoin price: {e}")
# except KeyError:
#     sys.exit("Error: Unexpected API response format.")





# import sys
# import requests
# import time

# # Check for command-line argument
# if len(sys.argv) != 2:
#     sys.exit("Missing command-line argument")

# # Check if argument is a valid number
# try:
#     n = float(sys.argv[1])
# except ValueError:
#     sys.exit("Command-line argument is not a number")

# # Public API URL (no API key required)
# url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

# # Retry mechanism for API requests
# max_retries = 3
# for attempt in range(max_retries):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         print("Raw Response:", response.text)  # Debugging: Print the raw response
#         data = response.json()
#         price_per_btc = data["bitcoin"]["usd"]
#         total_cost = price_per_btc * n
#         print(f"${total_cost:,.4f}")
#         break
#     except requests.RequestException as e:
#         if attempt < max_retries - 1:
#             print(f"Attempt {attempt + 1} failed. Retrying...")
#             time.sleep(1)  # Wait before retrying
#         else:
#             sys.exit(f"Error fetching Bitcoin price after {max_retries} attempts: {e}")
#     except KeyError as e:
#         sys.exit(f"Error: Unexpected API response format. {e}")




# import sys
# import requests

# def main():
#     if len(sys.argv) != 2:
#         sys.exit("Missing command-line argument")

#     try:
#         n = float(sys.argv[1])
#     except ValueError:
#         sys.exit("Command-line argument is not a number")

#     try:
#         response = requests.get(
#             "https://api.coindesk.com/v1/bpi/currentprice.json")
#         response.raise_for_status()
#     except requests.RequestException:
#         sys.exit("Error fetching Bitcoin price")

#     price_usd = response.json()["bpi"]["USD"]["rate_float"]
#     total = n * price_usd

#     # Format with 4 decimals and commas
#     print(f"${total:,.4f}")

# if __name__ == "__main__":
#     main()



import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(
        "https://api.coincap.io/v2/assets/bitcoin",
        headers={"Authorization": "Bearer 8e4b733bb90e6853a9de07597893458068f8e42c79cdc7bd49da2beeed0aa0b3"}
    )
    response.raise_for_status()
    data = response.json()
    price = float(data["data"]["priceUsd"])
    amount = bitcoins * price
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit("API request failed")
