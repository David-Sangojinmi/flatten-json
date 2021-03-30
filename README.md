# Coding Challenge Submission

## Problem Description
Write a program that takes a JSON object as input and outputs a flattened version of the JSON object, with keys as the path to every terminal value in the JSON structure. Output should be valid JSON.

## Solution Description
**Language Chosen**: Python

To use, create a `.json` file which contains the JSON object to be flattened.

Then run the following in the command line.
```
cat <filename> | python flatten_json.py
```
Where `<filename>` is the name of file that contains the JSON object. An example is:
```
cat test.json | flatten_json.py
```
Which can be run by downloading all files in the repo and running command in command line.