MojoMut 🔥
==============
A CLI mutation testing tool for Mojo programming language.
Currently generates arithmetic/boolean/conditional/unary operator mutants and/or integer mutants,
runs with pytest, and outputs mutation kill score. Does not handle equivalent mutants, and will cause 
mutant syntax errors with string coercion.

To mojomut the first time (linux only, tested on ubuntu):

- Have [Mojo] environment set up in directory with Mojo files to test
- Install [pytest] and [pytest-mojo] 
- Install [tree-sitter]: put binary in default bin folder with proper permissions or use included binary in /bin
- If using included tree-sittter binary, setup $PATH for mojomut/bin/tree-sitter. Easiest way is to edit .bashrc
- Open this file with text editor: ```~/.bashrc```
- Add ```export PATH="<filepath to repo>/mojomut/bin:$PATH"``` to the end of .bashrc
- You may be able to use node instead to install/run tree-sitter, but you will need to change this line in mojomut.py:
- ```result = subprocess.run(["tree-sitter", "parse", filepath], stdout=subprocess.PIPE)```
- to ```result = subprocess.run(["npx, tree-sitter", "parse", filepath], stdout=subprocess.PIPE)```
- Run ```tree-sitter init-config```
- Edit the config.json file that was created so that the "parser-directories" includes path to mojomut folder
- Have tests in same folder as mojo file you want to mutate
- Run ```python3 mojomut.py <filepath> [mutant type...]```

Arguments
 - filepath: path to mojo file to mutate. Tests must be in same directory with test_ prefix added
 - mutant type: one or more of: ```all operator integer binary boolean comparison unary```
 - all: every operator type and integers. might take a while
 - operator: all operator types. no integers
 - binary: `````'+', '-', '*', '/', '%', '**', '//', '>>', '<<', '^', '&', '|'`````
 - boolean: ```'and', 'or'```
 - comparison: ```'<', '>', '<=', '>=', '==', '!=', 'is', 'is not'```
 - unary: ```'+', '-', 'not'```

[tree-sitter]: https://github.com/tree-sitter/tree-sitter
[tree-sitter-mojo]: https://github.com/b-price/tree-sitter-mojo
[pytest]: https://docs.pytest.org/en/8.2.x/
[pytest-mojo]: https://github.com/guidorice/mojo-pytest
[Mojo]: https://docs.modular.com/mojo/manual/get-started/


