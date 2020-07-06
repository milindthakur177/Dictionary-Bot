# Cambridge-Dictionary-Bot

# Brief

A bot that uses Cambridge Dictionary to give meaning of a word given as input. The meaning of the word will be web scrapped through this [Website](https://dictionary.cambridge.org/dictionary/english/) and No API is used what so ever.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Libraries.

```bash
pip install bs4
pip install request
```

## Usage

```python
import requests
from bs4 import BeautifulSoup
result= requests.get(user)
soup= BeautifulSoup(result.text,"lxml")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
