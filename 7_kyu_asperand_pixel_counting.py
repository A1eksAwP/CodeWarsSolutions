# https://www.codewars.com/kata/63d54b5d05992e0046752389/train/python

"""
# Description

You can paint an asperand by pixels in three steps:
1. First you paint the inner square, with a side of ```k```.
2. Then you need to paint one pixel, that's laying diagonally relative to the inner square that you just painted ( _the bottom-right corner of the inner square is touching the top-left corner of the pixel_ ). Let's call it the "bridge".
3. Finally, you will need to paint the outer shape, connected diagonally to the "bridge" ( _see the picture for more information_ ).

Here are some examples of this:

![Examples for 0<k<5](https://justpaste.it/img/78b363ec3c92b9be234603fd8ca0b1e4.png)

Your task is to find the number of pixels that need to be painted, for different `k`:

```javascript
k = 1 => 11
k = 2 => 18
k = 3 => 26
k = 4 => 34

# Limitations are 1 ≤ k ≤ 1e9
```

_The idea for this kata was taken from the Ukrainian Informatics Olympiad 2023._
"""

"""
Для внутренних квадратов будет зависимость: (k - 1) * 4
Для внешних квадратов зависимость: ((3 + k - 1) * 4) - 2
Тогда: ((k - 1) + (3 + k - 1)) * 4 - 2
"""
def my_solution(): 
	...
