# GitHub User Activity CLI

## Overview

**GitHub User Activity CLI** is a command-line tool that fetches and displays the activity of a specified GitHub user using the GitHub API. Built with Python and relying only on the standard library.

## Features

- **Fetch GitHub Activity:** Retrieve recent events from a GitHub user’s profile.
- **User-Friendly Output:** Summarizes events like pushes, issues, pull requests, and stars.
- **Graceful Error Handling:** Notifies you if a username is invalid or if the API request fails.
- **No External Dependencies:** Uses only Python’s built-in libraries.

## Requirements

- Python 3.x

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   
2. **Navigate to the Project Directory:**

   ```bash
   cd github-user-activity-cli
   
## Usage

Run the CLI tool from command prompt:
   ```bash
   py main.py
```
Then write username:
   ```bash
   github-activity-cli <username>
```
## Project Structure
   ```bash
   github-user-activity-cli/
├── .gitignore
├── main.py # Main script for fetching and displaying GitHub activity
└── README.md # Project documentation
```