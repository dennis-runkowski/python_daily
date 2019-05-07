"""
This script is used to extract emails from text data.

Example:
    text = "Please send a note to dennis@gmail.com"

    email_extractor(text) --> ["dennis@gmail.com"]
"""
import re
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging


def email_extractor(text):
    """
    Extract emails from text
    Args:
        text (str): Text data

    Returns:
        list of emails, returns empty list if none are found
    """
    if not isinstance(text, str):
        log.WARNING("Method will not extract emails from a non str!")
        return []

    emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)

    return emails

if __name__ == "__main__":
    text = input("Enter text: ")
    emails = email_extractor(text)
    log.info(emails)

