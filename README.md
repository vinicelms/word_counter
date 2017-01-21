# Word Counter

API for the purpose of performing a data scraping on a page and returning a number of times that appears on the page.

The URL and a word are pre-informed through parameters entered in the API URL structure.

## Python version used: `3.6.0`

## Project requirements:
- Flask
- Flask-RESTful
- lxml
- requests
- beautifulsoup4

## How to use (install):
1 - Clone the project:
```sh
git clone https://github.com/vinicelms/word_counter.git
```
2 - Enter the project directory:
```sh
cd word_counter
```
3 - Create your Virtualenv `(optional, but recommended)`:
```sh
python -m venv .venv
```
4 - `(only if step 3 is used)` Activate your Virtualenv (Linux and Windows):
- Linux
```sh
source .venv/bin/activate
```
- Windows
```sh
.venv\Scripts\activate.bat
```
5 - Update Pip:
```sh
python -m pip install --upgrade pip
```
6 - Install the project requirements:
```sh
pip install -r requirements.txt
```

## How to use (API):
- Browser `(any operating system)`
```sh
127.0.0.1:5000/word_counter?url=https://docs.python.org/3/&word=python
```
- Linux (Terminal):
```sh
curl -X GET "127.0.0.1:5000/word_counter?url=https://docs.python.org/3/&word=python"
```
- Windows (Powershell):
```sh
Invoke-RestMethod -Uri "127.0.0.1:5000/word_counter?url=https://docs.python.org/3/&word=python"
```
> Powershell returns objects as PSObject, returning a key value pair with common tool formatting.

```sh
Powershell output formatting:
python
------
  18
```

> For the Powershell output to be formatted in JSON:
```sh
Invoke-RestMethod -Uri "127.0.0.1:5000/word_counter?url=https://docs.python.org/3/&word=python" | ConvertTo-Json
```

## Important:
##### `The values entered can be changed if the page is changed or if you use another URL or word.`

## Error Handling:
- Calling the endpoint without parameters or without URL
```sh
{"error": "URL cannot be blank!"}
```
- Calling the endpoint without the word parameter
```sh
{"error": "Word cannot be blank!"}
```
- Calling the endpoint with some incorrect URL information
```sh
{"error": "URL is not valid!"}
```

## How to run tests (Unit Tests):
```sh
python -m unittest discover tests
```
- Expected return on tests:
```sh
Ran 9 tests in 0.724s
OK
```
> The runtime of the test may vary depending on factors of operating system, hardware features or miscellaneous settings