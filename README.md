# year-remaining
A python script that generates a progress bar and percentage of time left in the year.

## Using the script

### In a Zapier code action

The primary intent of this script is to be used in a Python code action in Zapier, which is why it has a very specific output variable format. Follow these steps in Zapier:

* Add a Code action to your Zap, and select the "Run Python" option. The script requires no configuration of "Input Data" values.
* Paste the script into the Code field, then test the action.
* Once complete, any action that follows will have access to the progress bar text. 

Customize the accessible values by adding elements to the dictionary contained in the output variable.

### From the command line

Execute the script from the command line to get an output of the progress bar and percentage text.

```
% python3 generate.py
░▓▓▓▓▓▓▓▓▓ 85.4%
```
