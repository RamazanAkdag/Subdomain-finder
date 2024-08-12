# Subdomain Enumeration Tool

This project is a multithreaded Python application designed for efficient subdomain enumeration. By leveraging threading, it optimizes the process of discovering valid subdomains for a given domain, handling up to 10 concurrent threads simultaneously.

## Features

- **Multithreaded Execution**: Utilizes threading to concurrently check subdomains, significantly speeding up the enumeration process.
- **Customizable Subdomain List**: Reads subdomain prefixes from an external file, allowing you to easily customize the list of subdomains to check.
- **Thread Pool Management**: Efficiently manages up to 10 threads at a time, balancing speed and system resource usage.
- **Error Handling**: Gracefully handles DNS errors, ensuring that the process continues even when certain subdomains are unreachable.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/subdomain-enumeration-tool.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd subdomain-enumeration-tool
    ```

3. **Install the required dependencies:**

    This project relies on Python's standard library, so no additional dependencies are required.

## Usage

1. **Prepare your subdomain list:**

    Create a text file named `sdomains.txt` in the project directory. Each line should contain a subdomain prefix you want to check (e.g., `www`, `mail`, `api`).

2. **Run the script:**

    Execute the main script to start the subdomain enumeration:

    ```bash
    python3 subdomain_enumeration.py
    ```

3. **Enter the target domain:**

    When prompted, enter the domain you wish to enumerate subdomains for (e.g., `example.com`).

4. **View the results:**

    The script will output the valid subdomains it finds, along with their corresponding IP addresses.

## Example

```bash
$ python3 subdomain_enumeration.py
Enter the domain name (e.g., example.com): example.com
Subdomain found: www.example.com -> IP: 93.184.216.34
Subdomain not found: mail.example.com
...
Valid subdomains:
['www.example.com', 'api.example.com']
Count: 2
