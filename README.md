# Free Speech Flag Maker

A Python script that turns your given hexedecimal string into a Free Speech Flag.

A free speech flag uses three hex bytes of a given input to represent a color as a hex color (#ffffff).
This will automatically convert your hex bytes string into a flag. The bits that can't be made into a
color will be printed to the console.

## Usage
First, prep your ```input.txt``` by removing the spaces in between your bytes.

For example: <br>
```02 0f ff 1a 0a bc ad 11 ff dd 0a 0a 9e ee ff``` needs to be turned into ```020fff1a0abcad11ffdd0a0a9eeeff```. Use Notepad++ to replace all spaces and line breaks.

Now, install the dependency and run the script.
```
pip install pillow
python3 script.py input.txt output.png
```

Here's our example output:

![alt text](https://github.com/wg481/free-speech-flag-maker/blob/main/example%20output.png "Sample Free Speech Flag.")
