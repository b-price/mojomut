MojoMut 🔥
==============
A mutation testing tool for Mojo programming language.
Currently generates arithmetic/boolean/conditional/unary operator mutants, runs with pytest, and outputs mutation kill score. Does not handle equivalent mutants.

To run mojomut (ubuntu only):

- Install [pytest] and [pytest-mojo] 
- Install [tree-sitter]: put binary in default bin folder with proper permissions/use included binary in /bin
- If using included tree-sittter binary, setup $PATH for mojomut/bin/tree-sitter. Easiest way is to edit .bashrc
- Open this file with text editor: ```~/.bashrc```
- Add ```export PATH="<filepath to repo>/mojomut/bin:$PATH"``` to the end of .bashrc
- Have tests in same folder as mojo file you want to mutate
- Run ```python3 mojomut.py <filepath> [mutant type...]```

[tree-sitter]: https://github.com/tree-sitter/tree-sitter
[tree-sitter-mojo]: https://github.com/b-price/tree-sitter-mojo
[pytest]: https://docs.pytest.org/en/8.2.x/
[pytest-mojo]: https://github.com/guidorice/mojo-pytest


