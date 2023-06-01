# passphrasegen

On multiple occasions I've had to generate reasonably strong passwords that still needed to be conveyed easily over the phone.  I whipped this up to use [the XKCD algorithm](https://xkcd.com/936/) to generate a bunch of possible passwords so I don't have to hand-crank the code every time.  Example invocations:

```
$ passphrasegen.py # generate one passphrase
pedant tanker bails creaky

$ passphrasegen.py -c 4 # generate 4 passphrases
coupes sticks boll fewer
foul skips phased grader
mottle mask dipper idols
horsed cadets digit ruse

$ passphrasegen.py --min=6 --max=8 # words must be 6 <= len(word) <= 8
clearing mushier rivetted planners

$ passphrasegen.py -n3 --caps # randomly capitalize words
took Shine nine

$ passphrasegen.py -n3 -f # insert random fill-chars
side#mind=real

$ passphrasegen.py -n3 --caps -f
bold%Water3scale

$ passphrasegen.py --help
Usage: pass [options]

Options:
  -h, --help            show this help message and exit
  -d FILE, --dict=FILE, --dictionary=FILE
                        The default dictionary to use (default:
                        /usr/share/dict/words)
  -x FILE, --exclude=FILE
                        A file containing (optionally ROT13'ed) words to
                        exclude such as profanity
  -c COUNT, --count=COUNT
                        The number of passwords to output (default: 1)
  -n LENGTH, --number=LENGTH
                        The number of words to output (default: 6)
  --min=MIN, --min-len=MIN, --min-length=MIN
                        The minimum length of word to consider (default: 4)
  --max=MAX, --max-len=MAX, --max-length=MAX
                        The maximum length of word to consider (default: 6)
  --include-upper       Include words containing upper chars
  --include-numeric     Include words containing numeric chars
  --include-punct       Include words containing punct chars
  --caps                Use random capitalization
  -f, --fill            Use random punct/numbers for fill (rather than spaces)
  --fillchars=FILLCHARS
                        Default fill characters (default:
                        '0123456789,.@#$%*-+=')
  -v, --verbose         Report additional statistics
  -g GUESSES_PER_SECOND, --guesses-per-second=GUESSES_PER_SECOND, --guesses=GUESSES_PER_SECOND, --gps=GUESSES_PER_SECOND
                        Guesses per second (for additional statistics)
```

It assumes the dictionary is located at `/usr/share/dict/words` which it is on most Linux/BSD/Mac boxes.
However, you can use the `--dict` option to specify an alternate dictionary if you want (or need to on a Windows box)

Throwing this out there in case other folks need a fast way to generate such passwords.
