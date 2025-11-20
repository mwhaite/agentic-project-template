# Dependencies Documentation

This file tracks all project dependencies and explains why each is needed.

## Core Dependencies
<!-- Production dependencies -->

### [Dependency Name] (v1.2.3)
- **Purpose:** TODO: Why is this needed?
- **Alternatives Considered:** TODO: What else was evaluated?
- **License:** TODO: License type
- **Security Notes:** TODO: Any known vulnerabilities or concerns?
- **Added:** YYYY-MM-DD

## Development Dependencies
<!-- Dependencies needed only for development/testing -->

### [Dev Dependency Name] (v1.2.3)
- **Purpose:** TODO: Why is this needed?
- **Added:** YYYY-MM-DD

## Dependency Management

### Update Policy
- **Patch updates:** Applied automatically
- **Minor updates:** Review and test before applying
- **Major updates:** Requires careful evaluation and migration plan

### Security Scanning
- Run `npm audit` / `pip-audit` / equivalent regularly
- Address high/critical vulnerabilities within 7 days
- Evaluate moderate vulnerabilities case-by-case

### Dependency Health Checks
Before adding a new dependency, verify:
- [ ] Active maintenance (commits within last 6 months)
- [ ] Good documentation
- [ ] Reasonable download/usage statistics
- [ ] Compatible license
- [ ] No known security issues
- [ ] Suitable alternatives evaluated

## Deprecated Dependencies
<!-- Track removed dependencies for historical context -->

### [Old Dependency Name]
- **Removed:** YYYY-MM-DD
- **Reason:** TODO: Why was this removed?
- **Replaced By:** TODO: What replaced it?

---

## Instructions for AI Agents

When adding dependencies:
1. Verify the dependency is actively maintained
2. Check for security vulnerabilities
3. Document the dependency in this file
4. Update the appropriate manifest (package.json, requirements.txt, etc.)
5. Consider if the functionality could be easily implemented instead
