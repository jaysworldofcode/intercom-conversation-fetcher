# Intercom Conversation Automated
The goal for this project is to fetch all your conversation from intercom and output to JSON format.

## Installation
Download and Install python
	For Windows: https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe
	For MacOS: https://www.python.org/ftp/python/3.11.5/python-3.11.5-macos11.pkg <br>

1. Clone the repo
   ```sh
   git clone <repository-url>
   ```
3. Install pip packages
   ```sh
   pip install -r requirements.txt
   ```
4. Open .env file and update the required variables

## Usage

```bash
python main.py {url} {recursion_depth_limit}

ex: python main.py https://news.ycombinator.com/ 2
```