# jabi-lol

Inspired by Facebook's [bunnylol](https://github.com/ccheever/bunny1) search engine and using the new
[jack_bunny](https://github.com/jackyang127/jack_bunny) that is a modernized version of the prior. I have tweaked jack's version to
my needs and my possible commands. Also I split the requirements in [basic_requirements](./basic_requirements.txt) and
[requirements](./requirements.txt) being the first for development purposes and the later for production.

### Commands
I have some commands and plan to add more, but right now the possible most important now is this command:

* `help` returns a list of usable commands

### How to write your own commands
You can tweak your command inside the [comamnds.py](./commands.py) file, for example if you want to add the `i` command that works
for going to instagram when given no arguments and takes you to a user when giving arguments, you will need to add this to the
`Commands` class

```python
def i(arg=None):
  """'i [insert query]' searches for users or takes you to the home page"""
  if arg:
    return 'https://instagram.com/{0}'.format(arg)
  else:
    return 'https://instagram.com'
```

### How to host your own server
Jack (the user which version I am basing mine) has a better [explanation](https://github.com/jackyang127/jack_bunny)
for this so go check it out if you have any doubt about it.
