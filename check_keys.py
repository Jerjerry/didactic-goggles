#!/usr/bin/env python3
"""
OpenAI API Key Checker
A tool to validate multiple OpenAI API keys in parallel and identify their status.
"""

from openai import OpenAI
from concurrent.futures import ThreadPoolExecutor
import time
import sys
import os

def check_api_key(api_key):
    """
    Check if an API key is valid by making a minimal API request.
    
    Args:
        api_key (str): The OpenAI API key to check
        
    Returns:
        tuple: (api_key, is_valid, status_message)
    """
    try:
        client = OpenAI(api_key=api_key.strip())
        # Make a minimal request to check the key
        response = client.models.list()
        return api_key, True, "Valid"
    except Exception as e:
        error_msg = str(e).lower()
        if "invalid api key" in error_msg:
            return api_key, False, "Invalid key"
        elif "exceeded your current quota" in error_msg:
            return api_key, False, "No credits"
        elif "rate limit" in error_msg:
            return api_key, False, "Rate limited"
        else:
            return api_key, False, f"Error: {str(e)}"

def mask_key(key):
    """
    Mask an API key for secure display.
    
    Args:
        key (str): The API key to mask
        
    Returns:
        str: Masked version of the key showing only first 8 and last 4 characters
    """
    return f"{key[:8]}...{key[-4:]}"

def main():
    """Main function to run the API key checker."""
    print("\nOpenAI API Key Checker")
    print("=" * 50)
    print("\nPaste your API keys (one per line)")
    print("Press Enter twice when done (i.e., leave a blank line)")
    print("-" * 50)
    
    # Collect API keys
    api_keys = []
    try:
        while True:
            line = input().strip()
            if not line:  # Empty line
                break
            if line.startswith('sk-'):  # Basic validation
                api_keys.append(line)
            else:
                print(f"Skipping invalid key format: {mask_key(line) if len(line) > 12 else line}")
    except (EOFError, KeyboardInterrupt):
        print("\nInput terminated.")
        sys.exit(1)

    if not api_keys:
        print("\nNo valid API keys provided!")
        return

    print(f"\nChecking {len(api_keys)} API keys...")
    print("-" * 50)

    # Check keys in parallel
    valid_keys = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(check_api_key, api_keys)
        
        for api_key, is_valid, status in results:
            masked_key = mask_key(api_key)
            if is_valid:
                print(f"[VALID] {masked_key}: {status}")
                valid_keys.append(api_key)
            else:
                print(f"[FAIL] {masked_key}: {status}")

    print("-" * 50)
    print(f"\nFound {len(valid_keys)} valid API keys.")
    
    if valid_keys:
        print("\nValid API keys:")
        for key in valid_keys:
            print(key)

        # Save valid keys to file
        output_file = "valid_api_keys.txt"
        try:
            with open(output_file, "w") as f:
                for key in valid_keys:
                    f.write(f"{key}\n")
            print(f"\nValid keys have been saved to '{output_file}'")
        except Exception as e:
            print(f"\nError saving to file: {str(e)}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        sys.exit(1)
