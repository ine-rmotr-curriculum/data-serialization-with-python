# 01 Why Regular Expressions?

In this exercise you will need to define several regular expressions that match substrings in a text.  Provided for your practice is a `show()` utility function that will display matches by surrounding them with guillemets.  We want to set the various pattern variables such that the following will be output.  Note that there will be many patterns that match the correct substrings, finding any such pattern is acceptable.


```python
>>> show(pat1) 
```
```
«Humpty» «Dumpty» sat on a wall,
«Humpty» «Dumpty» had a great fall.
All the king's horses and all the king's men
Couldn't put «Humpty» together again.
```

```python
>>> show(pat2)
```
```
Humpty Dumpty sat on «a wall»,
Humpty Dumpty had «a great» fall.
All the king's horses «and all» the king's men
Couldn't put Humpty together again.
```

```python
>>> show(pat3)
```
```
Humpty Dumpty «sat» on «a» «wall»,
Humpty Dumpty «had» «a» «great» «fall».
All the king's horses «and» «all» the king's men
Couldn't put Humpty together «again».
```

```python
>>> show(pat4)
```
```
«Humpty Dumpty» sat on a wall,
«Humpty Dumpty» had a great fall.
All the king's horses and all the king's men
Couldn't «put Humpty» together again.
```

## Setup


```python
import re

rhyme = '''Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall.
All the king's horses and all the king's men
Couldn't put Humpty together again.'''

def show(pat, s=rhyme):
    print(re.sub(pat, r'«\g<0>»', s, flags=re.M))
    
pat1 = r"NOMATCH"
pat2 = r"NOMATCH"
pat3 = r"NOMATCH"
pat4 = r"NOMATCH"
```

## Solution


```python
pat1 = r'.umpty'
pat2 = r'\ba\w* \w+'
pat3 = r'\b\w*a\w*'
pat4 = r'\b.u.{8,15}?\b'
```

## Tests Cases


```python
def test_umpty():
    s = '''«Humpty» «Dumpty» sat on a wall,
«Humpty» «Dumpty» had a great fall.
All the king's horses and all the king's men
Couldn't put «Humpty» together again.'''
    assert s == re.sub(pat1, r'«\g<0>»', rhyme, flags=re.M)
    
test_umpty()
```


```python
def test_a_word_next():
    s = '''Humpty Dumpty sat on «a wall»,
Humpty Dumpty had «a great» fall.
All the king's horses «and all» the king's men
Couldn't put Humpty together again.'''
    assert s == re.sub(pat2, r'«\g<0>»', rhyme, flags=re.M)    

test_a_word_next()
```


```python
def test_a_words():
    s = '''Humpty Dumpty «sat» on «a» «wall»,
Humpty Dumpty «had» «a» «great» «fall».
All the king's horses «and» «all» the king's men
Couldn't put Humpty together «again».'''
    assert s == re.sub(pat3, r'«\g<0>»', rhyme, flags=re.M)    

test_a_words()    
```


```python
def test_about_humpty():
    s = '''«Humpty Dumpty» sat on a wall,
«Humpty Dumpty» had a great fall.
All the king's horses and all the king's men
Couldn't «put Humpty» together again.'''
    assert s == re.sub(pat4, r'«\g<0>»', rhyme, flags=re.M)    

test_about_humpty()        
```

# 02 Groups, Classes, and Alternation

In this exercise you will need to define several regular expressions that match substrings in a text. Provided for your practice is a show() utility function that will display matches by surrounding them with guillemets. This exercise is very similar to the previous one, and even uses the same sample text.  However, to create the patterns for this exercise, you will need to use extra regular expression features introduced in this lesson.

Note that you should try to come up with relatively compact patterns, which is possible for all of these exercises.  Now that you understand alternation, a trivial "cheat" is to match any of an enumeration of literal matching strings.  Your goal is to express the pattern more generally.

```python
>>> show(pat1)
```
```
Humpty Dumpty sat on «a wall»,
Humpty Dumpty had a great fall.
All «the king»'s horses and all «the king»'s men
Couldn't put Humpty together again.
```

```python
>>> show(pat2)
```
```
Humpty Dumpty sat on «a wall,»
Humpty Dumpty «had a great »fall.
All the king's horses «and all »the king's men
Couldn't put Humpty together again.
```

```python
>>> show(pat3)
```
```
Humpty Dumpty sat on a wall,
Humpty Dumpty had a «gre»at fall.
«All» «the» «king's» «horses» and all «the» «king's» men
«Couldn't» put Humpty «together» again.
```

```python
show(pat4)
```
```
Humpty Dumpty sat« on a »wall,
Humpty Dumpty had« a great »fall.
All« the king»'s horses« and all »«the king»'s men
Couldn't put Humpty together again.
```

## Setup


```python
import re

rhyme = '''Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall.
All the king's horses and all the king's men
Couldn't put Humpty together again.'''

def show(pat, s=rhyme):
    print(re.sub(pat, r'«\g<0>»', s, flags=re.M))
    
pat1 = r"NOMATCH"
pat2 = r"NOMATCH"
pat3 = r"NOMATCH"
pat4 = r"NOMATCH"
```

## Solution


```python
pat1 = r'\b(the|a) [wk]\w+\b'
pat2 = r'(\w*a\w*[ ,]){2,3}'
pat3 = r'[^mpa ,.\n]{3,}'
pat4 = r' ?(on|a|the|and) \w+ ?'
```

## Tests Cases


```python
def test_article_something():
    s = '''Humpty Dumpty sat on «a wall»,
Humpty Dumpty had a great fall.
All «the king»'s horses and all «the king»'s men
Couldn't put Humpty together again.'''
    assert s == re.sub(pat1, r'«\g<0>»', rhyme, flags=re.M)    

test_article_something()
```


```python
def test_a_words_2_3():
    s = '''Humpty Dumpty sat on «a wall,»
Humpty Dumpty «had a great »fall.
All the king's horses «and all »the king's men
Couldn't put Humpty together again.'''
    assert s == re.sub(pat2, r'«\g<0>»', rhyme, flags=re.M)    

test_a_words_2_3()
```


```python
def test_not_some_letters():
    s = '''Humpty Dumpty sat on a wall,
Humpty Dumpty had a «gre»at fall.
«All» «the» «king's» «horses» and all «the» «king's» men
«Couldn't» put Humpty «together» again.'''
    assert s == re.sub(pat3, r'«\g<0>»', rhyme, flags=re.M)    

test_not_some_letters()
```


```python
def test_stop_word_next():
    s = '''Humpty Dumpty sat« on a »wall,
Humpty Dumpty had« a great »fall.
All« the king»'s horses« and all »«the king»'s men
Couldn't put Humpty together again.'''
    assert s == re.sub(pat4, r'«\g<0>»', rhyme, flags=re.M)    

test_stop_word_next()
```

# 03 Lookahead, Lookbehind, and Back References

In this exercise you will need to define several regular expressions that match substrings in a text. Provided for your practice is a show() utility function that will display matches by surrounding them with guillemets. This exercise is very similar to the previous two, but uses a slightly expanded text (with my own doggerel addition). However, to create the patterns for this exercise, you will need to use extra regular expression features introduced in this lesson.

```python
>>> show(pat1)
```
```
Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall,
«Dumpty Humpty» went to the ball,
«Humpty Dumpty» then had a lull.
All the king's horses and all the king's men
All this king's horses and all the king's men
Could not put Humpty together again.
```

```python
>>> show(pat2)
```
```
Humpty «Dumpty» sat on a wall,
Humpty «Dumpty» had a great fall,
Dumpty Humpty «went» to the ball,
Humpty «Dumpty» then had a lull.
All the king's horses and all the king's men
All this king's horses and all the king's men
Could not put Humpty «together» again.
```

```python
>>> show(pat3)
```
```
Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall,
Dumpty Humpty went to the ball,
Humpty Dumpty then had a lull.
All «the king's horses and all the» king's men
All this «king's horses and all the king»'s men
Could not put Humpty together again.
```

```python
>>> show(pat4)
```
```
Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall,
Dumpty Humpty went to the ball,
Humpty Dumpty then had a lull.
«All» «the» king's horses «and» «all» «the» king's «men»
«All» this king's horses «and» «all» «the» king's «men»
Could «not» «put» Humpty together again.
```

## Setup


```python
import re

rhyme = '''Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall,
Dumpty Humpty went to the ball,
Humpty Dumpty then had a lull.
All the king's horses and all the king's men
All this king's horses and all the king's men
Could not put Humpty together again.'''

def show(pat, s=rhyme):
    print(re.sub(pat, r'«\g<0>»', s, flags=re.M))
    
pat1 = r"NOMATCH"
pat2 = r"NOMATCH"
pat3 = r"NOMATCH"
pat4 = r"NOMATCH"
```

## Solution


```python
pat1 = r'(.umpty ?){2}(?= \w*e\w*)'
pat2 = r'(?<=Humpty )\w+'
pat3 = r"(?P<word>\b\w+\b)([ ']?\w+\b)+ (?P=word)"
pat4 = r'(?!.*ll.$)(\b\w{2,3}\b)'
```

## Tests Cases


```python
def test_umpty_context():
    s = '''Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall,
«Dumpty Humpty» went to the ball,
«Humpty Dumpty» then had a lull.
All the king's horses and all the king's men
All this king's horses and all the king's men
Could not put Humpty together again.'''
    assert s == re.sub(pat1, r'«\g<0>»', rhyme, flags=re.M)    

test_umpty_context()
```


```python
def test_after_humpty():
    s = '''Humpty «Dumpty» sat on a wall,
Humpty «Dumpty» had a great fall,
Dumpty Humpty «went» to the ball,
Humpty «Dumpty» then had a lull.
All the king's horses and all the king's men
All this king's horses and all the king's men
Could not put Humpty «together» again.'''
    assert s == re.sub(pat2, r'«\g<0>»', rhyme, flags=re.M)    

test_after_humpty()
```


```python
def test_words_apart():
    s = '''Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall,
Dumpty Humpty went to the ball,
Humpty Dumpty then had a lull.
All «the king's horses and all the» king's men
All this «king's horses and all the king»'s men
Could not put Humpty together again.'''
    assert s == re.sub(pat3, r'«\g<0>»', rhyme, flags=re.M)
    
test_words_apart()
```


```python
def test_short_word_not_ll_end():
    s = '''Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall,
Dumpty Humpty went to the ball,
Humpty Dumpty then had a lull.
«All» «the» king's horses «and» «all» «the» king's «men»
«All» this king's horses «and» «all» «the» king's «men»
Could «not» «put» Humpty together again.'''
    assert s == re.sub(pat4, r'«\g<0>»', rhyme, flags=re.M)

test_short_word_not_ll_end()
```

# 04 Python Functions

In this exercise we will reverse the focus of the earlier exercises.  You will be provided with the pattern, but you need to identify which function is called to produce a given result.  You will accomplish this by assigning different functions within the `re` module to new names, `fun1`, `fun2`, etc.

For example, here is a possible solution (this course does not discuss the rarely used `fullmatch()` function, you can look up its documentation):

```python
>>> fun99 = re.fullmatch
>>> fun99(r'^.*$', rhyme, re.DOTALL)
<re.Match object; span=(0, 141), match="Humpty Dumpty sat on a wall,\nHumpty Dumpty had a>
```

Here are functions to assign that the expected results:

```python
>>> fun1(r'Humpty', rhyme)
<re.Match object; span=(0, 6), match='Humpty'>
```

```python
>>> fun2(r'Dumpty', rhyme)
<re.Match object; span=(7, 13), match='Dumpty'>
```

```python
>>> list(fun3(r'Humpty', rhyme))
[<re.Match object; span=(0, 6), match='Humpty'>,
 <re.Match object; span=(29, 35), match='Humpty'>,
 <re.Match object; span=(119, 125), match='Humpty'>]
```

```python
>>> list(fun4(r'Humpty', rhyme))
['Humpty', 'Humpty', 'Humpty']
```

```python
>>> list(fun5(r'Humpty', rhyme))
['',
 ' Dumpty sat on a wall,\n',
 " Dumpty had a great fall.\nAll the king's horses and all the king's men\nCouldn't put ",
 ' together again.']
 ```

## Setup


```python
import re

rhyme = '''Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall.
All the king's horses and all the king's men
Couldn't put Humpty together again.'''

def wrong(pat, *args): 
    return pat

fun1 = wrong
fun2 = wrong
fun3 = wrong
fun4 = wrong
fun5 = wrong
```

## Solution


```python
fun1 = re.match
fun2 = re.search
fun3 = re.finditer
fun4 = re.findall
fun5 = re.split
```

## Tests Cases


```python
def test_distinct():
    assert len({fun1, fun2, fun3, fun4, fun5}) == 5, \
            "You have not defined distinct functions"
    
test_distinct()
```


```python
def test_1():
    assert fun1(r'Humpty', rhyme).span() == (0, 6)
    
test_1()
```


```python
def test_2():
    assert fun2(r'Dumpty', rhyme).span() == (7, 13)

test_2()
```


```python
def test_3():
    from collections.abc import Iterator
    assert isinstance(fun3(r'Humpty', rhyme), Iterator)
    
test_3()
```


```python
def test_4():
    assert len(fun4(r'Humpty', rhyme)) == 3
    
test_4()
```


```python
def test_5():
    assert len(fun5(r'Humpty', rhyme)) == 4
    
test_5()
```

# 05 Flags and Performance

In this exercise you will have two tasks.  For the first task, you will show your understanding of `re` flags to change the behavior of some searches.  In the second task, you will reformulate regular expression patterns so they do not take unreasonably long.

There is some value of `flags` which you may set to get the following behavior:

```python
>>> re.findall(r'(\w\w+) o, \1', fela_song, flags=flags)
['Zombie', 'zombie']
```

To assist with the second task, we provide a context manager `timeout` that will let you try searches without them running indefinitely.  The difference between a normal and a pathological case might be milliseconds versus years.

```python
>>> with timeout:
...    sleep(6)
[...]
TimeoutError: Timeout (5 seconds)
```

In the variable `pat1` and `pat2` are equivalent patterns, merely verbose mode or not.  Your answer in `pat` may use either style.  The pattern tries to match a sequence of 8 words, each of which may *either* have 4 letters *or* contain a 3-vowel cluster.  Many words, of course, fulfill neither of those criteria, but some fulfill both.

You need to revise the pattern so that it matches in a reasonable time—less than 10 seconds—for either success or failure cases.

## Setup


```python
import re
from time import sleep
from src.timeout import timeout

fela_song = '''
Zombie o, zombie (zombie o, zombie)
Βρυκόλακας o, βρυκόλακας (βρυκόλακας o, βρυκόλακας)
ზომბი o, ზომბი (ზომბი o, ზომბი)
'''
flags = re.MULTILINE

success = ('lieu aeon raia eoan agave kuia euoi kaie naoi eaux viae '
           'fetid zoeal ciao luau aias huia idyls quai eaus jiao the '
           'moai meou goads paua mooi handy beau moue toea roue ') * 50_000

failure = ('eoan agave kuia lieu aeon raman euoi kaie naoi eaux vie '
           'fetid zoeal ciao idyls quai eaus luau aias huia jiao the '
           'moai meou goads paua mooi handy bean moue toea roue ') * 50_000

pat1 = r'((\b\w{4}\b ??)+|(\b\w*[aeiou]{3}\w*\b ??)+){8}'

pat2 = r'''(                   # Want 8 words in row with either...
  (\b\w{4}\b[ ]??)+            # Four letter word
  |                            # Or...
  (\b\w*[aeiou]{3}\w*\b[ ]??)+ # Has 3-vowel cluster
  ){8}                         # 8 words
'''

pat = re.compile(pat2, re.VERBOSE)
pat = re.compile(pat1)

```

## Solution


```python
flags = re.ASCII | re.IGNORECASE

# Eliminate one-or-more quantifier within each alternative
# Eliminate word boundary checks implied by trailing space
# Space after word common to both alternatives
pat_faster = r'''(   # Want 8 words in row with either...
  (\w{4})            # Four letter word
  |                  # Or...
  (\w*[aeiou]{3}\w*) # Has 3-vowel cluster
  [ ]?){8}           # 8 words
'''

pat = re.compile(pat_faster, re.VERBOSE)
```

## Tests Cases


```python
def test_fela():
    match = re.findall(r'(\w\w+) o, \1', fela_song, flags=flags)
    assert match == ['Zombie', 'zombie'], "Got %s" % match
    
test_fela()
```


```python
def test_success():
    match = re.search(pat, success)
    assert match.span() == (145, 184)
    
test_success()
```


```python
def test_fast_failure():
    with timeout:
        match = re.search(pat, failure)
    assert match is None
    
test_fast_failure()
```


```python

```
