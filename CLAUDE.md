# CLAUDE.md - AI Assistant Guide for DevProgram

**Last Updated**: 2025-11-17
**Repository Status**: New/Minimal - Initial Development Phase

## Table of Contents

1. [Repository Overview](#repository-overview)
2. [Current Project State](#current-project-state)
3. [Development Guidelines](#development-guidelines)
4. [Git Workflow](#git-workflow)
5. [Code Conventions](#code-conventions)
6. [Testing Strategy](#testing-strategy)
7. [Documentation Standards](#documentation-standards)
8. [Common Tasks](#common-tasks)
9. [Important Reminders](#important-reminders)

---

## Repository Overview

**Repository**: DevProgram
**Purpose**: [To be determined - currently in initial setup phase]
**Primary Language**: [Not yet determined]
**Status**: Brand new repository with minimal initial structure

### Current Structure

```
DevProgram/
├── README.md          # Project README (minimal)
├── CLAUDE.md          # This file - AI assistant guide
└── .git/              # Git version control
```

---

## Current Project State

### What Exists
- ✅ Git repository initialized
- ✅ Initial commit with basic README
- ✅ Branch: `claude/claude-md-mi2volgiqvozs4mt-01SkeNLd3e8zTac9YyjxD3tv`

### What's Missing (To Be Added)
- ⬜ Project configuration files (package.json, requirements.txt, etc.)
- ⬜ Source code directory structure
- ⬜ Testing framework setup
- ⬜ CI/CD configuration
- ⬜ .gitignore file
- ⬜ Build scripts
- ⬜ Documentation beyond README

### Next Steps for Development
1. **Determine project type** (web app, CLI tool, library, etc.)
2. **Choose technology stack** (Node.js, Python, Go, etc.)
3. **Set up project structure** (src/, tests/, docs/, etc.)
4. **Configure tooling** (linters, formatters, build tools)
5. **Establish testing framework**
6. **Create initial documentation**

---

## Development Guidelines

### General Principles

1. **Ask First, Code Second**
   - Since this is a new project, confirm project requirements before making assumptions
   - Clarify technology stack preferences before adding dependencies
   - Verify architectural decisions with the user

2. **Progressive Enhancement**
   - Start with minimal viable implementations
   - Build incrementally with clear commits
   - Avoid over-engineering in early stages

3. **Documentation-Driven**
   - Update this CLAUDE.md as the project evolves
   - Keep README.md current with setup instructions
   - Document architectural decisions in code comments

4. **Security First**
   - Never commit sensitive data (.env files, credentials, API keys)
   - Always create .gitignore before adding dependencies
   - Follow OWASP guidelines for web applications
   - Validate and sanitize all inputs

### File Creation Guidelines

When setting up the project:

1. **Configuration Files**
   - Create .gitignore before installing dependencies
   - Use industry-standard config templates
   - Include comments explaining non-obvious settings

2. **Directory Structure**
   - Follow language/framework conventions
   - Common structure suggestions:
     ```
     src/          # Source code
     tests/        # Test files
     docs/         # Documentation
     scripts/      # Build/deployment scripts
     config/       # Configuration files
     ```

3. **Documentation**
   - README.md: Project overview, setup, usage
   - CONTRIBUTING.md: Contribution guidelines (if needed)
   - API.md: API documentation (for libraries/services)
   - CHANGELOG.md: Version history

---

## Git Workflow

### Branch Strategy

- **Working Branch**: `claude/claude-md-mi2volgiqvozs4mt-01SkeNLd3e8zTac9YyjxD3tv`
- **Main Branch**: [To be determined]
- **Naming Convention**: `claude/<descriptive-name>-<session-id>`

### Commit Guidelines

1. **Commit Message Format**
   ```
   <type>: <short description>

   <detailed description if needed>

   <breaking changes if any>
   ```

2. **Commit Types**
   - `feat`: New feature
   - `fix`: Bug fix
   - `docs`: Documentation changes
   - `style`: Code style changes (formatting, etc.)
   - `refactor`: Code refactoring
   - `test`: Adding/updating tests
   - `chore`: Maintenance tasks
   - `init`: Initial setup/scaffolding

3. **Commit Best Practices**
   - Keep commits atomic (one logical change per commit)
   - Write clear, descriptive messages
   - Commit working code (all tests should pass)
   - Don't commit commented-out code or TODOs without context

### Push Protocol

```bash
# Always push to the designated branch
git push -u origin claude/claude-md-mi2volgiqvozs4mt-01SkeNLd3e8zTac9YyjxD3tv

# Retry on network failures (up to 4 times with exponential backoff)
# Wait: 2s, 4s, 8s, 16s between retries
```

**CRITICAL**: Branch names must start with `claude/` and end with matching session ID, otherwise push will fail with 403.

---

## Code Conventions

### Language-Specific Conventions

#### JavaScript/TypeScript (If Used)
- Use ES6+ features
- Prefer `const` over `let`, avoid `var`
- Use async/await over raw Promises
- 2-space indentation
- Semicolons: [To be determined]
- File naming: camelCase or kebab-case
- Tools: ESLint, Prettier

#### Python (If Used)
- Follow PEP 8 style guide
- 4-space indentation
- Use type hints (Python 3.6+)
- File naming: snake_case
- Tools: pylint, black, mypy

#### General
- Write self-documenting code
- Use meaningful variable/function names
- Keep functions small and focused
- Comment complex logic, not obvious code
- Avoid magic numbers (use named constants)

### Code Organization

```
# Function order (general guideline)
1. Imports/requires
2. Constants
3. Type definitions/interfaces
4. Main/exported functions
5. Helper/private functions
6. Exports
```

---

## Testing Strategy

### Test Framework (To Be Determined)

Recommended options based on language:
- **JavaScript/TypeScript**: Jest, Vitest, Mocha
- **Python**: pytest, unittest
- **Go**: Built-in testing package
- **Rust**: Built-in cargo test

### Testing Guidelines

1. **Coverage Goals**
   - Aim for >80% code coverage
   - 100% coverage for critical paths
   - Test edge cases and error conditions

2. **Test Structure**
   - Use AAA pattern: Arrange, Act, Assert
   - One assertion per test (when possible)
   - Clear test names describing what's being tested

3. **Test Types**
   - Unit tests: Individual functions/methods
   - Integration tests: Component interactions
   - E2E tests: Full user workflows (if applicable)

---

## Documentation Standards

### Code Documentation

1. **File Headers**
   ```
   /**
    * @file filename.ext
    * @description Brief description of file purpose
    * @author [Generated/Modified by AI]
    */
   ```

2. **Function Documentation**
   ```
   /**
    * Brief function description
    *
    * @param {Type} paramName - Parameter description
    * @returns {Type} Return value description
    * @throws {ErrorType} When error occurs
    */
   ```

3. **Inline Comments**
   - Explain WHY, not WHAT
   - Document non-obvious decisions
   - Include links to relevant issues/docs

### README.md Structure

Keep README current with these sections:
1. Project title and description
2. Features
3. Installation/Setup
4. Usage examples
5. Configuration
6. Development guide
7. Testing
8. Contributing
9. License

---

## Common Tasks

### Starting New Feature Development

1. Verify current branch: `git branch --show-current`
2. Check working tree: `git status`
3. Create feature plan using TodoWrite
4. Implement incrementally with frequent commits
5. Write tests alongside code
6. Update documentation
7. Push to remote when complete

### Adding Dependencies

1. **Before installation**: Create/update .gitignore
2. **Document**: Add dependency purpose in commit message
3. **Security**: Check for known vulnerabilities
4. **Version**: Pin major versions, allow minor/patch updates
5. **Review**: Ensure dependency is maintained and trustworthy

### Debugging Issues

1. Read error messages carefully
2. Check recent changes: `git diff`
3. Use logging/debugging tools
4. Search codebase for similar patterns
5. Consult documentation
6. Ask user for clarification if needed

---

## Important Reminders

### Security Checklist

- [ ] .gitignore configured before adding dependencies
- [ ] No hardcoded credentials or API keys
- [ ] Input validation on all user inputs
- [ ] No SQL injection vulnerabilities (use parameterized queries)
- [ ] No XSS vulnerabilities (escape output)
- [ ] HTTPS for external API calls
- [ ] Dependency vulnerability scanning

### Before Committing

- [ ] Code runs without errors
- [ ] Tests pass (if tests exist)
- [ ] No debugging console.log/print statements
- [ ] No commented-out code (unless documented why)
- [ ] Documentation updated if needed
- [ ] This CLAUDE.md updated if project structure changed

### Before Pushing

- [ ] All commits have clear messages
- [ ] Working tree is clean
- [ ] Pushing to correct branch
- [ ] No sensitive data in commits
- [ ] Branch name follows convention

### Communication with User

- [ ] Confirm unclear requirements before implementing
- [ ] Explain technical decisions when made
- [ ] Report blockers immediately
- [ ] Summarize changes after major work
- [ ] Ask for feedback on architectural choices

---

## Project Evolution

### When to Update This File

This CLAUDE.md should be updated when:
1. Technology stack is chosen
2. Project structure is established
3. Coding conventions are defined
4. New tools/frameworks are added
5. Testing strategy is implemented
6. Deployment process is defined
7. New patterns/practices are adopted

### Version History

| Date | Changes | Author |
|------|---------|--------|
| 2025-11-17 | Initial creation for new repository | Claude (AI Assistant) |

---

## Additional Resources

### Placeholder for Future Documentation

- Architecture decisions: [To be added]
- API documentation: [To be added]
- Deployment guide: [To be added]
- Troubleshooting guide: [To be added]

### External References

- [Git Best Practices](https://git-scm.com/book/en/v2)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

---

**Note to AI Assistants**: This is a brand new repository. Always confirm project direction and technology choices with the user before making significant decisions. This file should evolve as the project grows.
