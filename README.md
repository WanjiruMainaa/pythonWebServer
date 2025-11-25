# Python Web Server Project

A collaborative web server implementation in Python 3, demonstrating fundamental web server concepts including request handling, file serving, directory listing, and CGI script execution.

##Team Members

- **Project Lead:** [Wanjiru] - CGI Implementation & Documentation
- **Member 1 (Issa):** Display Request Values Feature
- **Member 2 (Bill):** Core Request Handling & Error Management
- **Member 3 (David):** Directory Handling (Index & Listing)
- **Member 4 (Phillip):** Static file serving and error handling


## Project Overview

This project implements a simple HTTP web server from scratch using Python's `http.server` module. The server demonstrates progressive feature development based on the article "Hello, Web" and showcases collaborative software development practices using Git and GitHub.

##Features

### 1. Basic Request Handling
- Responds to HTTP GET requests
- Returns proper HTTP status codes (200, 404)
- Handles errors gracefully

### 2. Request Information Display
- Shows detailed information about incoming requests
- Displays: date/time, client IP, port, HTTP command, and requested path
- Formatted in an HTML table

### 3. Static File Serving
- Serves HTML files from disk
- Serves text files and other content
- Proper MIME type handling

### 4. Directory Handling
- **With index.html:** Automatically serves index.html when accessing a directory
- **Without index.html:** Generates and displays directory listing
- Filters out hidden files (starting with '.')

### 5. CGI Script Execution
- Executes Python scripts (`.py` files) dynamically
- Captures script output and sends to client
- Includes timeout protection (5 seconds)
- Error handling for script failures

### 6.Error Handling
- Custom error pages with helpful messages
- Proper HTTP 404 status codes for missing resources
- Exception handling throughout

##Getting Started

### Prerequisites
- Python 3.x installed on your system
- Basic understanding of command line
- Web browser

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR-USERNAME/python-web-server-project.git
cd python-web-server-project
```

2. **No additional dependencies needed!** (Uses Python standard library only)

### Running the Server
```bash
# Start the server
python3 server.py

# You should see:
# server running on http://localhost:8080/
# press Ctrl-C to stop it
```

The server will start on **port 8080**. Open your browser and visit:
- http://localhost:8080/

To stop the server, press `Ctrl+C` in the terminal.

##Testing the Server

### Test 1: Basic File Serving
```bash
# Create a test HTML file
echo "<h1>Test Page</h1><p>This is a test.</p>" > test.html

# Run server and visit:
# http://localhost:8080/test.html
```

### Test 2: Request Information Display
```bash
# Visit the root path:
# http://localhost:8080/

# You'll see a table with request details
```

### Test 3: Directory with Index
```bash
# Create directory with index.html
mkdir my_folder
echo "<h1>Folder Index</h1>" > my_folder/index.html

# Visit: http://localhost:8080/my_folder/
# Should show the index.html content
```

### Test 4: Directory Listing
```bash
# Create directory without index.html
mkdir files
echo "File 1" > files/file1.txt
echo "File 2" > files/file2.txt

# Visit: http://localhost:8080/files/
# Should show a list of files
```

### Test 5: CGI Script
```bash
# Create a CGI script
cat > time_display.py << 'EOF'
from datetime import datetime
print('<html><body>')
print('<h1>Current Time</h1>')
print('<p>{}</p>'.format(datetime.now()))
print('</body></html>')
EOF

# Visit: http://localhost:8080/time_display.py
# Should execute and show current time
```

### Test 6: 404 Error
```bash
# Visit a non-existent file:
# http://localhost:8080/does-not-exist.html

# Should show error page with 404 status
# (Check browser DevTools(right click and press inspect) → Network tab to verify status code)
```

##Architecture

### Case-Based Handler Pattern

The server uses a **case-based architecture** for handling different types of requests:
```python
Cases = [
    case_display_values(),          # Shows request info
    case_root_path(),               # Handles root path
    case_no_file(),                 # File doesn't exist
    case_cgi_file(),                # Python scripts
    case_existing_file(),           # Regular files
    case_directory_index_file(),    # Directory with index.html
    case_directory_no_index_file(), # Directory listing
    case_always_fail()              # Fallback
]
```

Each case handler has two methods:
- **`test(handler)`** - Checks if this handler can process the request
- **`act(handler)`** - Processes the request

The server loops through handlers in order until one matches.


##Resources

This project is based on the article "Hello, Web" which covers:
- HTTP request/response cycle
- Python's `BaseHTTPRequestHandler`
- File I/O operations
- Process execution with `subprocess`
- Error handling patterns
- Code organization and refactoring

### Making Changes

1. **Create a feature branch:**
```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes** and test them

3. **Commit your changes:**
```bash
git add .
git commit -m "Description of changes"
```

4. **Push to GitHub:**
```bash
git push origin feature/your-feature-name
```
5. **Create a Pull Request** on GitHub
6. **Request review** from project lead
7. **After approval**, merge into main branch

# Try a different port by editing server.py:
serverAddress = ('', 3030)  # Use port 3030 instead
```

# For CGI scripts, they don't need execute permission
# (The server runs them with python)
```

### CGI scripts not working
- Make sure the script ends with `.py`
- Check for syntax errors: `python your-script.py`
- Look at server console output for error messages
- Make sure script prints HTML (starts with `print('<html>...')`)

### Files not found (404 errors)
- Check file path is correct (case-sensitive!)
- Make sure file is in the same directory as server.py or subdirectory
- Use relative paths from server.py location

##Learning Objectives Achieveds
- Understanding HTTP protocol basics
- File I/O operations in Python
- Process management with subprocess
- Object-oriented design patterns
- Error handling and exception management
- Git/GitHub collaboration workflow
- Code review and pull request process
- Documentation and README writing




