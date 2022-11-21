# Vertical Slashes

## [This week’s question](https://buttondown.email/cassidoo/archive/normal-is-not-something-to-aspire-to-its-4437/)

Write a function that takes a string of slashes (\ and /) and returns all of those slashes drawn downwards in a line connecting them.

### Example

```bash
$ verticalSlashes('\\\//\/\\')
\
 \
  \
  /
 /
 \
 /
 \
  \
$ verticalSlashes('\\\\')
\
 \
  \
   \
```

## Plus and Minus

Initially, I thought to keep track of how many spaces are being used per line while incrementing for `\` and decrementing for `/`.

### Code 1

```python
def veritcal_slashes(slashes):
    spaces = 0
    for slash in slashes:
        output = " " * spaces + slash
        print(output)
        if slash == '\\':
            spaces = spaces + 1
        if slash == '/':
            spaces = spaces -1
```

### Result 1

This resulted in misaligned slashes

```text
veritcal_slashes('\\\//\/\\')
\
 \
  /
 /
\
 /
\
```

## Memeory

Looking at the failed results, I realised that I only need to change spacing if the slash matches the previous slash. This means I needed the ability to look back at the previous input. I could accomplish this in the same for-each loop by adding another variable to keep track of the last seen symbol, but I thought it would be better to switch to a regular range for loop allowing me to grab both the current and previous slash.

### Code 2

```python
def veritcal_slashes(slashes):
    spaces = 0
    for x in range(len(slashes)):
        if x == 0:
            print(slashes[x])
        else:
            current = slashes[x]
            previous = slashes[x-1]
            spaces = shift(current, previous, spaces)
            output = ' ' * spaces + slashes[x]
            print(output)
def shift(current, previous, spaces):
    if current == previous:
        if current == '\\':
            return spaces + 1
        else:
            return spaces - 1
    else:
        return spaces
```

### Result 2

This gave me the output I was looking for. However, I wasn't quite done just yet.

```text
veritcal_slashes('\\\//\/\\')
\
 \
 /
/
\
/
\
```

## Shift All

Thinking about edge cases, I considered two possiblities.

1. Input was not restricted to slashes
2. There was a substring of concurrent forward slashes pushing the spaces counter to negative

For the premise of the question to work, I decided to accept `|` chars but error out for any other input. This was done with a simple `not in` check using the string `\\|/`.

I considered erroring out if the number of forward slashes forced spaces to negative, but I decided that it could be handled by shifting all of the text to the right to give more room for the forward slashes. In order to support this change, I needed to hold my output in an array instead of printing immediately after processing a line.

This allowed me to check if spaces is negative. If spaces is negative, I could go through my output array and add a space to every line before printing the final answer at the end.

### Code 3

```python
def veritcal_slashes(slashes):
    spaces = 0
    answer = []
    for x in range(len(slashes)):
        if slashes[x] not in '\\|/':
            print("ERROR: Line " + str(x) + " not valid char")
            exit(1)
        if x == 0:
            answer.append(slashes[x])
        else:
            current = slashes[x]
            previous = slashes[x-1]
            spaces = shift(current, previous, spaces)
            if spaces < 0:
                spaces = spaces + 1
                answer = shift_all(answer)
            output = ' ' * spaces + slashes[x]
            answer.append(output)
    print_answer(answer)
def shift(current, previous, spaces):
    if current == '|':
        if previous == '\\':
            return spaces + 1
        else:
            return spaces - 1
    if current == previous:
        if current == '\\':
            return spaces + 1
        else:
            return spaces - 1
    else:
        if previous == '|':
            if current == '\\': 
                return spaces + 1
            else:
                return spaces - 1 
        return spaces
def shift_all(lines):
    newlines = []
    for line in lines:
        newlines.append(' ' + line)
    return newlines
def print_answer(answer):
    for line in answer:
        print(line)
```

### Result 3

```text
vertical_slashes('/|///a|\\\\|\\\\|//|\\')
ERROR: Line 5 not valid char

veritcal_slashes('/|///|\\\\|\\\\|//|\\')
     /
    |
   /
  /
 /
|
 \
  \
   |
    \
     \
      |
     /
    /
   |
    \
```
