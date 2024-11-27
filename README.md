# OpenAI API Key Checker

A simple yet powerful tool to validate multiple OpenAI API keys in parallel. This tool helps you identify which API keys are valid, expired, or have no remaining credits.

## Features

- ✅ Check multiple API keys simultaneously
- 🔒 Secure key display (only shows first 8 and last 4 characters)
- 🚀 Parallel processing (5 keys at a time)
- ⚡ Fast validation using minimal API calls
- 📝 Saves valid keys to a file
- ❌ Detailed error messages for invalid keys
- 🔍 Basic key format validation

## Requirements

- Python 3.7+
- OpenAI Python package

## Installation

1. Clone this repository or download the files
2. Install the required package:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:
```bash
python check_keys.py
```

2. Paste your API keys, one per line
3. Press Enter twice (leave a blank line) when done
4. The script will check all keys and show their status
5. Valid keys will be saved to `valid_api_keys.txt`

## Output Format

For each key, you'll see one of these statuses:
- `[VALID]` - Key is valid and working
- `[FAIL] Invalid key` - Key format is invalid or key is revoked
- `[FAIL] No credits` - Key has no remaining credits
- `[FAIL] Rate limited` - Too many requests (try again later)

## Security Notes

- API keys are only stored locally in `valid_api_keys.txt`
- Keys are never sent anywhere except to OpenAI's API
- The script masks most of the key characters in the output

## License

MIT License - Feel free to use and modify as needed!
