"""
Write a function that when given a URL as a string, parses out 
just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""


def domain_name(url):
    name = url[7:] if 'http://' in url else url[8:] if 'https://' in url else url
    name = (name.lstrip('www.') if 'www.' in name else name).split('.')
    return name[0]
    

domain_name("http://github.com/carbonfive/raygun")
domain_name("http://www.zombie-bites.com" )
domain_name("https://www.cnet.com")
domain_name("http://google.com")
domain_name("http://google.co.jp")
domain_name("https://123.net")
domain_name("https://hyphen-site.org")
domain_name("http://codewars.com")
domain_name("www.xakep.ru")
domain_name("https://youtube.com")
domain_name("http://www.codewars.com/kata/")
domain_name("icann.org")

