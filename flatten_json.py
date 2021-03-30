import collections
import sys
import json

def flatten(json_obj):
    """
    flatten receives a valid JSON object (that does not contain arrays) as
    inputm and returns the flattened version of the JSON object, where keys
    are the path to each value in the JSON structure, as output.

    :param json_obj: the json object to be flattened
    """
    queue = collections.deque()
    output = {}

    for key, value in json_obj.items():
        queue.append((key, value))

    while len(queue) > 0:
        s, j = queue.popleft()

        if not isinstance(j, dict):
            output[s] = j
        else:
            for key, value in j.items():
                queue.append((s + '.' + key, value))

    return str(output)

# Load json document to object
obj = json.load(sys.stdin)

# Print the flattened JSON object
print(flatten(obj))