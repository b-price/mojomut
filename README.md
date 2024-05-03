MojoMut 🔥
==============
A mutation testing tool for Mojo programming language.
Currently generates arithmetic/boolean/conditional/unary operator mutants, runs with pytest, and outputs mutation kill score.

To run mojomut (ubuntu only):

- Run ```tree-sitter init-config```
- Open the config.json file that was created in any editor
- Edit parser directories so that it points to "tree-sitter-parsers"
- Install [pytest] and [pytest-mojo] 
- Setup $PATH for mojomut/bin/tree-sitter. Easiest way is to edit .bashrc
- Open this file with text editor: ```~/.bashrc```
- Add ```export PATH="<filepath to repo>/mojomut/bin:$PATH"```
- Have tests in same folder as mojo file you want to mutate
- Probably need to edit the last line in mojomut.py if you're not in a vscode ubuntu devcontainer. Mojomut will still work but won't delete all the mutants
- Run ```python3 mojomut.py <filepath> [mutant type...]```

[tree-sitter]: https://github.com/tree-sitter/tree-sitter
[tree-sitter-mojo]: https://github.com/b-price/tree-sitter-mojo
[pytest]: https://docs.pytest.org/en/8.2.x/
[pytest-mojo]: https://github.com/guidorice/mojo-pytest


