import pyshorteners

# Create a Shortener object
s = pyshorteners.Shortener()

# Long URL to be shortened
long_url = input("Enter the URL: ")
# Shorten the URL
short_url = s.tinyurl.short(long_url)

print("Original URL:", long_url)
print("Shortened URL:", short_url)