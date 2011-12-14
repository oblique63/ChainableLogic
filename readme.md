Chainable Logic
==========

I once came across some code that looked like this:

```python
 if thing and other_thing and this_thing.is_true and \
 another_thing.isnt_true and some_other_crap:
     # do some nonsense
     ...
```

and I thought, "Gee, that looks awfully... redundant...?" (even though
it technically wasn't). So I decided to rip off some lisp, and came up with this:

```python
 if AND(thing, other_thing, this_thing.is_true, another_thing.isnt_true, some_other_crap).true:
     # yay, slightly less awkward!
     ...
```

Which I then expanded to:

```python
 if AND(a, b).OR(x, y).true:
     # chaining!
     ...
     
 # which translates to
 if (a and b) or (x or y).true:
     ...
     
 # but can also be written as
 if OR(AND(a, b), x, y).true:
     # nesting!
     ...
```

and once I got bored, I added on:

```python
 if NAND(a, b, c, d).true:
     ...
     
 # which translates to
 if not (a and b and c and d):
     ...
 
 # and also
 if NOR(w, x, y, z).true:
     ...
 
 # is the same as
 if not (w or x or y or z):
     ...
```

which are a bit trickier to keep track of once you start chaining.


### Is that it?
Yeah, pretty much...

### Would there actually be any point in using this?
Probably not.

### Then why did you write it?
So that I could ask myself stupid questions in third-person.

### Ok, sold! How do I use it?

```python
from operations import *
```

then just go by the examples above.
 
 
 Licensing
---------
This code is released under the [Mozilla Public License](http://www.mozilla.org/MPL/MPL-1.1.html).
Copyright &copy; 2011, Enrique Gavidia