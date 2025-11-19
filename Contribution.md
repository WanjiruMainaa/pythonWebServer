# Contributing to Python Web Server Project

Thank you for contributing to this project! This guide will kick you off in getting started.

## Getting Started

### 1. Reviewing your Issue
- Find your assigned issue
- Ask for clarification if unsure
- Create a new branch from the main branch
- Implement required changes commiting regularly
- Test changes locally to ensure issue is resolved



### 3. Make Your Changes
- Write your code in `server.py`
- Add any test files to `tests/`
- Update documentation if needed


### 5. Commit Your Changes
```bash
# Check what files changed
git status

# Add all changes
git add .

# Commit with a clear message
git commit -m "Add static file serving functionality (closes #3)"
```

##Descriptive commit messages:
-Add request information display feature 
-Implement case-based handler architecture 
-Fix encoding bug in do_GET method

##Unreccommended commit messages:**
-update
-changes
-fixed stuff


### 7. Create a Pull Request
1. Go to the repository on GitHub
2. You'll see a prompt to "Compare & pull request" - click it
3. Fill out the PR template:
   - *Title:* Brief description of changes
   - *Description:* Reference the issue, explain what you did
   - *Testing:* Describe how you tested it
4. Request review from the project lead
5. Wait for feedback

### 8. Address Review Comments
- Read the review carefully
- Make requested changes
- Commit and push again
- The PR will automatically update

### 9. After Approval
- The project lead will merge your PR
- Delete your feature branch (GitHub will prompt you)

## Code Style Guidelines

### Python Style 
- Add blank lines between functions/classes
- Use descriptive variable names

### Documentation
- Add docstrings to all classes and methods
- Comment complex logic
- Update README if you add new features

### Example:
```python
class RequestHandler(BaseHTTPRequestHandler):
    '''Handle HTTP requests for the web server.'''
    
    def do_GET(self):
        '''Handle GET requests from clients.'''
        # Your implementation here
        pass
```

## Testing Checklist

Before creating a PR, make sure:
- Server starts without errors
- Your feature works as expected
- You haven't broken existing functionality
- Code follows style guidelines
- You've added comments where needed
- You've tested edge cases

## Need Help?

- **Questions about your issue?** Comment on the issue on GitHub
- **Technical problems?** Ask in the group chat or tag the project lead
- **Stuck on Git?** Check the [Git commands reference](README.md#git-commands-quick-reference)

## Communication

- Use GitHub issue comments for task-specific discussions
- Tag teammates with their @username when you need their input
- Keep the project lead updated on your progress
- Don't hesitate to reach out when stuck!

---

Happy coding!!