=== python - Advent of Code rules ===

### Directory Structure
- `modules/` contains modules to help with common tasks like grid, list functions. Use them as needed. If you see a possibility to add a function to a module, please do so.
- `20xx/xx.py` files are the actual solutions.
- `input/20xx/xx.txt` contains the input for the solution.
- `input/20xx/xx.yaml` contains the test input for the solution.

### Create stub files
- Use `create_stub.py` to create stub files. It has 3 parameters: --year, --day, and --test.
- `--year` creates a directory for the year.
- `--day` creates a solution file in `20xx/xx.py`.
- `--test` creates a test file in `input/20xx/xx.yaml`.

### Puzzle structure
- `parse()` is the function that parses the input and returns a data structure.
- `part_one()` and `part_two()` are the functions that solve the puzzle, it has the parameter `data` which is the result of `parse()`.
- `part_one()` and `part_two()` return the result of the puzzle.
- `solve()` is the function that calls `part_one()` and `part_two()` and prints the result. If there is a test file, it will also run the test before the actual solution.
