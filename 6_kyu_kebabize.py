# https://www.codewars.com/kata/57f8ff867a28db569e000c4a/train/python

"""
Modify the `kebabize` function so that it converts a camel case string into a kebab case.


```
"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"
```

Notes:
  - the returned string should only contain lowercase letters
"""

import re


def re_kebabize(st):
    return re.sub(r'(\d*)([a-z]*)([A-Z])?([a-z]*)', r'\g<2>-\g<3>\g<4>', re.sub(r'\d', '', st)).lower().strip('-')


def re_v2_kebabize(st):
    return re.sub(r'\B([A-Z])', r'-\g<1>', re.sub(r'\d', '', st)).lower()


def join_kebabize(st):
    return ''.join(c if c.islower() else f'-{c}' for c in st if c.isalpha()).lower().strip('-')
