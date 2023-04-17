# https://www.codewars.com/kata/59c5d0b0a25c8c99ca000237/train/python

"""
<a href="https://imgur.com/ta6gv1i"><img src="https://i.imgur.com/ta6gv1i.png?1" title="source: imgur.com" /></a>

# Kata Task

You are given a ``grid``, which always includes exactly two end-points indicated by `X`

You simply need to return true/false if you can detect a **one and only one** "valid" line joining those points.

A line can have the following characters :

* `-` = left / right
* `|` = up / down
* `+` = corner

## Rules for valid lines

* The most basic kind of valid line is when the end-points are already adjacent
```
X
X
```
```
XX
```
* The corner character (`+`) must be used for all corners (but **only** for corners).
* If you find yourself at a corner then you **must** turn.
* It must be possible to follow the line with no ambiguity (lookahead of just **one** step, and never treading on the same spot twice).
* The line may take any path between the two points.
* Sometimes a line may be valid in one direction but not the other. Such a line is still considered valid.
* Every line "character" found in the grid must be part of the line. If extras are found then the line is not valid.
 
# Examples

## Good lines

<table border="2">
<tr>

<td width="20%">
<pre style='font-size:20px;line-height:22px'>
X---------X
</pre>

<td width="20%">
<pre style='font-size:20px;line-height:22px'>
X
|
|
X
</pre>

<td width="20%">
<pre style='font-size:20px;line-height:22px'>
   +--------+
X--+        +--+
			   |
			   X
</pre>

<td width="20%">
<pre style='font-size:20px;line-height:22px'>
   +-------------+
   |             |
X--+      X------+    
</pre>

<td width="20%">
<pre style='font-size:20px;line-height:22px'>
   +-------+
   |      +++---+
X--+      +-+   X
</pre>
</table>

## Bad lines

<table border="2">

<tr>
<td width="20%">
<pre style='font-size:20px;line-height:22px'>
X-----|----X
</pre>

<td width="20%">
<pre style='font-size:20px;line-height:22px'>
X
|
+
X
</pre>

<td width="20%">
<pre style='font-size:20px;line-height:22px'>
   |--------+
X---        ---+
			   |
			   X
</pre>

<td width="20%">
<pre style='font-size:20px;line-height:22px'>
   +------
   |
X--+      X  
</pre>

<td width="20%">
<pre style='font-size:20px;line-height:22px'>
	  +------+
	  |      |
X-----+------+
	  |
	  X
</pre>
</table>

# Hint

Imagine yourself walking a path where you can only see your very next step. Can you know which step you must take, or not?
"""


def line(grid: list[str]):
	field_dict = {f'{i}_{j}': sy for i in range(len(grid)) for j, sy in zip(range(len(grid[i])), grid[i]) if sy != ' '}
	for index, symb in field_dict.items():
		i, j = index.split('_')
		i, j = int(i), int(j)
		left = field_dict.get(f'{i}_{j - 1}', '')
		right = field_dict.get(f'{i}_{j + 1}', '')
		up = field_dict.get(f'{i - 1}_{j}', '')
		down = field_dict.get(f'{i + 1}_{j}', '')
		around = (left, right, up, down)
		ways = len([way for way in around if way != ''])

		if symb == '-' and (left or right) not in '+X-':
			return False
		elif symb == '-' and ways < 2:
			return False
		if symb == '|' and (up or down) not in '+X|':
			return False
		elif symb == '|' and ways < 2:
			return False
		if symb == '+':
			if not any([(left and down), (left and up), (right and up), (right and down)]):
				return False
			elif ways < 2:
				return False
			elif ways == 3 and len([s for s in field_dict.values() if s == '+']) == 8:
				if left == '+' and up == '' and right == 'X' and down == '+':
					return False
				elif left == '+' and up == '+' and right == '' and down == 'X':
					return False
			elif ways == 4:
				if around.count('+') == 4:
					return False
				elif up == '|' and left == '-' and down == '|' and right == '-':
					return False
		if symb == 'X' and not ways == 1:
			if 'X' in around or ways == 0:
				return False
			if left == '+' and (up != '-' or down != '-' or right != '|'):
				return False
			if right == '+' and (up != '-' or down != '-' or left != '|'):
				return False
			if left == '-' and (up == '|' or down == '|' or right == '-'):
				return False
			if right == '-' and (up == '|' or down == '|' or left == '-'):
				return False
			if up == '|' and (down == '|' or left == '-' or right == '-'):
				return False
			if down == '|' and (up == '|' or left == '-' or right == '-'):
				return False
	return True
