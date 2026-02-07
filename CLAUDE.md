# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based Data Structures and Algorithms (DSA) practice repository for learning fundamental CS concepts through runnable examples.

## Running Code

Scripts are standalone and run directly:
```bash
python arrays/twoptrs.py
python linkedlists/fast_slow.py
python techniques/slidingwindow.py
```

No build system, external dependencies, or test framework—only Python standard library.

## Repository Structure

- **`/arrays/`** - Array/string algorithms: two-pointer technique, rotation, backtracking for balanced partitions
- **`/hash/`** - Hash-based problems, recursion exercises, tree traversal with frequency counting
- **`/linkedlists/`** - Linked list operations: fast/slow pointers, reversal, palindrome detection
- **`/techniques/`** - Python idiom references: sliding window, Counter, list/set comprehensions

## Key Patterns & Techniques

**Algorithms**: Two-pointer, sliding window, backtracking, DFS/tree traversal, recursion

**Data Structures**: Lists, linked lists (using `SimpleNamespace` for nodes), dicts/defaultdict/Counter, sets, deques

**Python Libraries**: `collections` (Counter, defaultdict, deque), `typing` for type hints

## Code Style

- Files contain inline problem descriptions in docstrings (explore/brainstorm/plan format)
- Test cases embedded as comments or print statements at module level
- Type hints used in newer files (linkedlists/, techniques/)
