import short_url
url = short_url.encode_url(120)
print (url)
key = short_url.decode_url(url)
print (key)