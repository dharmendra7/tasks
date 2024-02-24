# import requests
# from bs4 import BeautifulSoup

# # Symbol parameter
# symbol = "ADS"

# # URL for the company details page
# # url = f"https://www.boerse-frankfurt.de/equity/{symbol}/company-details"
# url = f"https://www.boerse-frankfurt.de/equity/adidas-ag/company-details"

# # Fetch the HTML content of the page
# response = requests.get(url)
# print(response)
# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response.content, "html.parser")

# # Write the HTML content to a text file
# with open("dividend_dates.txt", "w", encoding="utf-8") as file:
#     file.write(str(soup))

# # Find the dividend information section
# dividend_section = soup.find("div", {"class": "Dividend"})
# print(dividend_section)
# # Extract the dividend date information
# dividend_dates = [date.text.strip() for date in dividend_section.find_all("span", {"class": "Date"})]

# # Print the dividend dates
# print(dividend_dates)

import requests
from bs4 import BeautifulSoup

# URL of the webpage containing the dividend dates information
url = "https://www.boerse-frankfurt.de/equity/adidas-ag/company-details"

# Send a GET request to the URL and get the HTML response
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
with open("dividend_dates.txt", "w", encoding="utf-8") as file:
    file.write(str(soup.prettify()))
print(soup.prettify())


# dividend_dates = []
# for item in soup['data']:
#     dividend_dates.append(item['dividendLastPayment'])
# # Find the div element with the class 'divident-dates'
# divident_dates = soup.find("div", class_="divident-dates")
# print(divident_dates)
# # Extract the ul element with the class 'divident-dates-list' from the div element
# divident_dates_list = divident_dates.find("ul", class_="divident-dates-list")

# # Extract the dividend dates information from the ul element
# dividend_dates = [item.text.strip() for item in divident_dates_list.find_all("li")]

# # Print the dividend dates information
# print(dividend_dates)