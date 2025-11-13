# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a competitive programming practice repository containing 250+ algorithmic problem solutions, primarily from Chinese programming contests (蓝桥杯/Blue Bridge Cup, NOIP, USACO, GESP) and LeetCode-style problems.

## Project Structure

### File Naming Conventions
- **Contest Problems**: `[ContestName Year Level] ProblemName.py` (e.g., `[蓝桥杯 2024 省 B] 好数.py`)
- **Regular Problems**: Descriptive Chinese names (e.g., `数组的三角和.py`)
- **Mathematical Problems**: Function-style names (e.g., `x 的平方根.py`)

### Code Patterns
- **LeetCode Style**: 94 files use `class Solution:` with method implementations
- **Direct Implementation**: Some files use direct procedural code with input/output
- **Test Functions**: 41 files include `def test():` with assertion-based testing
- **Common Imports**: `functools.lru_cache`, `sortedcontainers`, `math`, `collections`

## Development Commands

### Environment Setup
```bash
# Create virtual environment with uv
uv venv

# Install dependencies
uv pip install -e .
```

### Running Solutions
```bash
# Run individual solution files
python "filename.py"

# Run with test cases (if test() function exists)
python "filename.py"  # Will automatically run test() if __name__ == "__main__"
```

## Algorithm Categories and Patterns

### Dynamic Programming
- Heavy use of `@lru_cache` and `@cache` for memoization
- State machines and digit DP patterns
- Grid-based DP for pathfinding problems

### Graph Theory
- Tree problems with DFS/BFS traversal
- Connectivity and shortest path algorithms
- Graph representation using adjacency lists

### Number Theory
- Modular arithmetic with `MOD = 1_000_000_007`
- Prime number generation and factorization
- Combinatorics and permutation calculations

### String Processing
- Pattern matching and manipulation
- Chinese character processing
- String parsing and transformation

### Data Structures
- Custom implementations for contest problems
- `SortedList` from sortedcontainers for efficient operations
- Binary search implementations

## Key Implementation Details

### Common Constants
- `MOD = 1_000_000_007` for modular arithmetic
- `INF = float('inf')` for infinity representations
- Direction arrays for grid traversal: `dirs = [(0,1), (1,0), (0,-1), (-1,0)]`

### Testing Approach
- Assertion-based testing within individual files
- Test cases stored in dictionaries with 'case' and 'expected' keys
- Manual verification through print statements

### Performance Considerations
- Solutions optimized for competitive programming constraints
- Time complexity analysis critical for acceptance
- Space optimization for memory constraints

## Language and Cultural Context

### Chinese Problem Names
- Problem names are in Chinese characters, reflecting contest origins
- Mathematical terms use standard Chinese notation
- Contest-specific terminology preserved

### Code Comments and Documentation
- Minimal inline documentation (competitive programming style)
- Problem understanding embedded in variable names and logic
- Solutions focus on correctness and efficiency over readability

## Dependencies

- **Python 3.12+** required
- **sortedcontainers>=2.4.0** for efficient sorted data structures
- **Standard library only** for most solutions