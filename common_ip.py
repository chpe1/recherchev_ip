"""
IP Address Comparison Script

This script compares IP addresses in multiple CSV and TXT files and identifies common IP addresses across them. It utilizes functions to extract IP addresses from files, including both CSV and TXT formats, and then performs the comparison.

Usage:
    To use this script, provide the paths of one or more CSV or TXT files as command-line arguments. The script will find and display the common IP addresses among the provided files.

Example:
    $ python script.py file1.csv file2.txt

Functions:
    - csv_to_list(file): Extracts IP addresses from a CSV file and returns them as a set.
    - txt_to_list(file): Extracts IP addresses from a text (TXT) file and returns them as a set.
    - load_ip_addresses_from_file(file_path): Loads IP addresses from a CSV or TXT file and returns them as a set.
    - compare_all_files(*file_paths): Compares IP addresses from multiple files and returns common IP addresses as a set.

Tests:
    python -m unittest tests.py

This script uses the argparse module to handle command-line arguments and provides meaningful output to identify common IP addresses.

Author: chpe1
Date: 30/10/2023
"""

import csv
from collections import Counter
import argparse

parser = argparse.ArgumentParser(
    description="Compare IP addresses in multiple CSV and TXT files and find common IP addresses.")
parser.add_argument("files", nargs='+',
                    help="List of CSV or TXT files containing IP addresses")
args = parser.parse_args()


def csv_to_list(file):
    """
    Extracts IP addresses from a CSV file and returns them as a set.

    Parameters:
        file (str): Path to the CSV file containing IP addresses.

    Returns:
        set: A set containing the extracted IP addresses as strings.
    """

    liste_f = set()
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                liste_f.add(row[0])
    return liste_f


def txt_to_list(file):
    """
    Extracts IP addresses from a text (TXT) file and returns them as a set.

    Parameters:
        file (str): Path to the TXT file containing IP addresses.

    Returns:
        set: A set containing the extracted IP addresses as strings.
    """
    liste_f = set()
    with open(file, 'r') as f:
        for row in f:
            if row:
                liste_f.add(row.rstrip('\n'))
    return liste_f


def load_ip_addresses_from_file(file_path):
    """
    Loads IP addresses from a CSV or TXT file and returns them as a set.

    Parameters:
        file_path (str): Path to the CSV or TXT file containing IP addresses.

    Returns:
        set: A set containing the extracted IP addresses as strings.

    Raises:
        ValueError: If the file format is not supported.
    """
    if file_path.endswith('.csv'):
        return csv_to_list(file_path)
    elif file_path.endswith('.txt'):
        return txt_to_list(file_path)
    else:
        raise ValueError("Unsupported file format: " + file_path)


def compare_all_files(*file_paths):
    """
    Compares IP addresses from multiple files and returns common IP addresses as a set.

    Parameters:
        *file_paths (str): Variable number of file paths containing IP addresses.

    Returns:
        set: A set containing the common IP addresses among the input files.
    """
    common_ips = None
    for file_path in file_paths:
        ip_addresses = load_ip_addresses_from_file(file_path)
        if common_ips is None:
            # If common_ips is empty, we put all IPs in it.
            common_ips = ip_addresses
        else:
            # If common_ips is not empty, we rewrite it with common values only.
            common_ips = common_ips.intersection(ip_addresses)
    return common_ips


def compare_common_ips_across_files(*file_paths):
    """
    Compares IP addresses from multiple files and returns IP addresses common to at least two files.

    Parameters:
        *file_paths (str): Variable number of file paths containing IP addresses.

    Returns:
        dict: A dictionary where keys are common IP addresses and values are sets of files where they are present.
    """
    common_ips = {}
    ip_sets = []

    for file_path in file_paths:
        ip_addresses = load_ip_addresses_from_file(file_path)
        ip_sets.append((file_path, ip_addresses))

    for file_1, ips_1 in ip_sets:
        for ip in ips_1:
            # Check if the IP address is common to at least one more file
            for file_2, ips_2 in ip_sets:
                if file_1 != file_2 and ip in ips_2:
                    if ip not in common_ips:
                        common_ips[ip] = {file_1, file_2}
                    else:
                        common_ips[ip].add(file_2)

    return common_ips


if __name__ == "__main__":
    # STEP 1 : compare if ip is in all files
    common_ips = compare_all_files(*args.files)
    if common_ips:
        print("Common IP Addresses in all files:")
        for ip in common_ips:
            print(ip)
    else:
        print("No common IP addresses found in all files")

    # STEP 2 : Compare if ip is in at least 2 files
    common_ips_2 = compare_common_ips_across_files(*args.files)
    if common_ips_2:
        print("IP Addresses common to at least two files:")
        for ip, files in common_ips_2.items():
            print(f"IP: {ip}, Present in Files: {', '.join(files)}")
    else:
        print("No common IP addresses found.")
