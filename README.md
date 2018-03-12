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
$ passphrasegen.py --help
Usage: passphrasegen.py [options]

Options:
  -h, --help            show this help message and exit
  -d PATH, --dict=PATH, --dictionary=PATH
                        The default dictionary to use (default:
                        /usr/share/dict/words)
  -c COUNT, --count=COUNT
                        The number of passwords to output (default: 1)
  -n LENGTH             The number of words to output (default: 4)
  --min=MIN, --min-len=MIN, --min-length=MIN
                        The minimum length of word to consider (default: 4)
  --max=MAX, --max-len=MAX, --max-length=MAX
                        The maximum length of word to consider (default: 6)
  --include-upper       Include words containing upper chars
  --include-numeric     Include words containing numeric chars
  --include-punct       Include words containing punct chars
  -v, --verbose         Report additional statistics
```

It assumes the dictionary is located at `/usr/share/dict/words` which it is on most Linux/BSD/Mac boxes.
However, you can use the `--dict` option to specify an alternate dictionary if you want (or need to on a Windows box)

Throwing this out there in case other folks need a fast way to generate such passwords.
