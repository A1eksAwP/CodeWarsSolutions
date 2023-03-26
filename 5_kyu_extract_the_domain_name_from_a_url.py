# https://www.codewars.com/kata/514a024011ea4fb54200004b/

import re


def domain_name(url):
    """
    Write a function that when given a URL as a string,
    parses out just the domain name and returns it as a string. For example:
    * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
    * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
    * url = "https://www.cnet.com"                -> domain name = cnet"
    :param url:
    :return:
    """
    return re.findall(r'(^http.*://www\.?|^http.*://?|^www\.?|^w*?)([^\.]+)', url)[0][1]


print(domain_name('http://www.google-tone.com'))
print(domain_name('http://google.co.jp'))
print(domain_name('www.xakep.ru'))
print(domain_name('https://youtube.com'))
print(domain_name('icann.org'))
