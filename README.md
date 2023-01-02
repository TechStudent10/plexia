# Plexia
A toy language made in a couple of hours (with no external dependencies) :D

## Specs
Full specifications are at [**specs.md**](/specs.md)

## Usage
> Note: Plexia doesn't respect BEDMASS (brackets, exponents, division, multiplication, adding, subtracting).

You can create an interactive shell by running:

```bash
$ python shell.py
```

You can run files by running:

```bash
$ python main.py file.plexia
```

---

Calculations:
```
calc 1 + 1 * 2
```

Comments:
```
# This is a comment
```

Creating variables:
```
variable = 10 + 10
```

Outputing something to the standard output:
```
print $variable / 2
```

Strings:

```
print "Hello World!"
string = "Hi Mom!"
print $string
```
