# working with JSON files
import json
from pathlib import Path

# Create an array
movies = [
    {'id': 1, 'title': 'Terminator', 'year': 1989},
    {'id': 2, 'title': 'Kindergarten Cop', 'year': 1992}
]

"""
# Create the json file and write the array as data on it
data = json.dumps(movies)
Path('movies.json').write_text(data)
"""

data = Path('movies.json').read_text()
movies = json.loads(data)
print(movies[1]['year'])
