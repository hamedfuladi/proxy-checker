# proxy-checker
## what does it DO?
This script is like a detective, it goes through a list of suspects (proxies) and attempts to connect to a website (the crime scene) using each suspect. If it finds the guilty suspect (proxy) that can connect to the website, it will say "I cracked the case!" and the loop will end. But if none of the suspects are guilty, it will say "This case remains unsolved." and the script will end. It's like solving a mystery but for your network connections.


# Description

This script is designed to check a list of proxies stored in a text file named "proxies.txt" against a given URL. The list of proxies must be separated by newline characters. The script will iterate through each proxy in the list, attempting to connect to the given URL using the proxy. If a successful connection is made, the script will print the successful proxy and break the loop. If none of the proxies in the list are able to establish a successful connection, the script will print a failure message.

## Dependencies

The script requires the following python libraries:

- requests
- bs4 (BeautifulSoup)
- pandas

## Usage

1. Make sure the text file containing the list of proxies is in the same directory as the script and is named "proxies.txt"
2. Run the script 
3. The script will prompt you to enter the base URL that you want to test the proxies against. Enter the URL.
4. The script will iterate through each proxy in the "proxies.txt" file, attempting to connect to the given URL using the proxy.
5. If a successful connection is made, the script will print the successful proxy and break the loop. 
6. If none of the proxies in the list are able to establish a successful connection, the script will print a failure message.

## Code Breakdown
- The script imports the libraries requests, bs4 and pandas.
- Prompts the user to enter the base URL that they want to test the proxies against.
- Defines a test_url_with_proxy function which takes in the base URL and a proxy and attempts to connect to the URL using the proxy.
- Opens the "proxies.txt" file in read mode.
- Iterates through each proxy in the "proxies.txt" file, attempting to connect to the given URL using the proxy.
- Prints the successful proxy and breaks the loop if a successful connection is made.
- Prints a failure message if none of the proxies in the list are able to establish a successful connection.
## Use Cases

1. Bypassing geo-restrictions: Some websites are only accessible from certain locations. By using a proxy from the restricted location, users can access the website.

2. Anonymous browsing: Proxies can be used to mask the user's IP address, providing a degree of anonymity while browsing the web.

3. Scraping: Proxies can be used to bypass website blocking mechanisms put in place to prevent scraping.

4. Improving online security: Using a proxy can add an extra layer of security by hiding the user's IP address and encrypting the connection.
