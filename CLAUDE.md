# CLAUDE.md - AI Assistant Guide for DevProgram

**Last Updated**: 2025-11-17
**Repository Status**: Active Java Development - 100 Programs Collection

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
**Purpose**: Collection of 100 independent, practical Java programs for real-world use
**Primary Language**: Java
**Status**: Active development with complete program collection

### Current Structure

```
DevProgram/
├── README.md                   # Project README
├── CLAUDE.md                   # This file - AI assistant guide
├── .gitignore                  # Java project gitignore
├── 01_Calculator/              # Basic arithmetic calculator
├── 02_TodoList/                # Task management system
├── 03_PasswordGenerator/       # Secure password generator
├── ...                         # (Programs 04-99)
└── 100_SystemMonitor/          # System resource monitor

Total: 100 independent Java programs across categories:
- Programs 01-20: Utilities (calculators, file readers, validators)
- Programs 21-40: Math & Calculators (converters, geometric calculators)
- Programs 41-60: Data Structures & Algorithms (sorting, searching, graphs)
- Programs 61-80: Games & Entertainment (TicTacToe, Sudoku, Snake)
- Programs 81-100: Advanced Tools (parsers, network tools, monitors)
```

---

## Current Project State

### What Exists
- ✅ Git repository initialized
- ✅ Initial commit with basic README
- ✅ Branch: `claude/claude-md-mi2volgiqvozs4mt-01SkeNLd3e8zTac9YyjxD3tv`
- ✅ .gitignore file configured for Java
- ✅ 100 independent Java programs organized in directories
- ✅ Complete CLAUDE.md documentation

### Program Categories
- ✅ **01-20**: Utilities & Basic Tools
- ✅ **21-40**: Calculators & Math Tools
- ✅ **41-60**: Data Structures & Algorithms
- ✅ **61-80**: Games & Entertainment
- ✅ **81-100**: Advanced Tools & Utilities

### Each Program Includes
- Standalone Java file (*.java)
- Independent execution (no dependencies between programs)
- Practical real-world functionality
- Clear comments and documentation

### How to Use Programs
1. **Navigate to program directory**: `cd XX_ProgramName/`
2. **Compile**: `javac ProgramName.java`
3. **Run**: `java ProgramName`
4. **Each program is completely independent** - no shared dependencies

### Example
```bash
cd 01_Calculator/
javac Calculator.java
java Calculator
```

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

### Java Conventions (Current Project)
- **Follow Oracle Java Code Conventions**
- **Class names**: PascalCase (e.g., `Calculator`, `TodoList`)
- **Method/variable names**: camelCase (e.g., `calculateTotal`, `userName`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `MAX_VALUE`, `DEFAULT_SIZE`)
- **Indentation**: 4 spaces
- **Bracing**: Opening brace on same line
- **Comments**: JavaDoc for classes and public methods
- **Scanner**: Always close Scanner objects to prevent resource leaks
- **File structure**: One public class per file, filename matches class name

#### General Best Practices
- Write self-documenting code
- Use meaningful variable/function names
- Keep methods small and focused (< 50 lines preferred)
- Comment WHY, not WHAT
- Avoid magic numbers (use named constants)
- Handle exceptions appropriately
- Validate user input

### Java Code Organization

```java
// Recommended order for Java classes:
1. Package declaration
2. Import statements
3. Class JavaDoc comment
4. Class declaration
5. Static constants
6. Instance variables
7. Constructors
8. Public methods (including main)
9. Private helper methods
```

---

## Testing Strategy

### Test Framework

**Recommended for Java**:
- **JUnit 5** (Jupiter) - Modern unit testing framework
- **JUnit 4** - Legacy but widely used
- **TestNG** - Alternative testing framework
- **Mockito** - Mocking framework for unit tests

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
| 2025-11-17 | Added 100 Java programs, updated for Java project | Claude (AI Assistant) |

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
