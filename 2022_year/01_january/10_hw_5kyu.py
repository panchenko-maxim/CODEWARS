"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
For example:
domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""

# списал((
def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]

print(domain_name("http://github.com/carbonfive/raygun"))