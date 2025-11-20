# Development Conventions

This document defines coding standards and conventions for this project.

## Code Style

### General Principles
- **Clarity over cleverness:** Write code that is easy to understand
- **Consistency:** Follow established patterns within the codebase
- **DRY:** Don't Repeat Yourself - extract common logic
- **YAGNI:** You Aren't Gonna Need It - don't add unused features

### Naming Conventions
<!-- Adjust based on your language -->

- **Variables:** `snake_case` or `camelCase` (specify)
- **Functions:** `snake_case` or `camelCase` (specify)
- **Classes:** `PascalCase`
- **Constants:** `UPPER_SNAKE_CASE`
- **Files:** `kebab-case` or `snake_case` (specify)

### Code Organization

```
project-root/
├── src/               # Source code
├── tests/             # Test files
├── docs/              # Documentation
├── scripts/           # Utility scripts
├── config/            # Configuration files
└── .agentic/          # Agentic system guidance
```

## Documentation

### Code Comments
- Comment **why**, not **what**
- Keep comments up-to-date with code changes
- Use docstrings for all public functions/classes

### Docstring Format
<!-- Adjust for your language -->

```python
def example_function(param1: str, param2: int) -> bool:
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When param2 is negative
    """
    pass
```

## Testing

### Test Structure
- **Unit tests:** Test individual functions/classes in isolation
- **Integration tests:** Test component interactions
- **E2E tests:** Test complete user workflows

### Test Naming
- `test_<function_name>_<scenario>_<expected_result>`
- Example: `test_calculate_price_with_discount_returns_reduced_price`

### Coverage Goals
- Aim for >80% code coverage
- 100% coverage for critical paths
- Don't sacrifice test quality for coverage metrics

## Git Conventions

### Commit Messages
Follow conventional commits:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Code restructuring
- `test`: Adding/updating tests
- `chore`: Maintenance tasks

**Example:**
```
feat(auth): add JWT token validation

Implements middleware to validate JWT tokens on protected routes.
Includes token expiration checking and signature verification.

Closes #123
```

### Branch Naming
- `feature/<feature-name>`
- `fix/<bug-description>`
- `docs/<doc-change>`
- `refactor/<refactor-scope>`

## Error Handling

- Use specific exception types
- Always include helpful error messages
- Log errors with appropriate context
- Fail fast and explicitly
- Clean up resources (use context managers/try-finally)

## Dependencies

- Pin exact versions in production
- Document why each dependency is needed (see DEPENDENCIES.md)
- Minimize dependency count
- Regularly update and audit dependencies
- Prefer well-maintained, widely-used libraries

## Security

- Never commit secrets or credentials
- Use environment variables for configuration
- Sanitize all user inputs
- Follow principle of least privilege
- Keep dependencies updated

---

## Instructions for AI Agents

When writing code:
1. Always follow these conventions
2. If conventions conflict with language idioms, ask for clarification
3. Suggest improvements to conventions if you notice gaps
4. Be consistent with existing code style in the project
