MojoMut 🔥
==============
A mutation testing tool for Mojo programming language.
Currently generates arithmetic/boolean/conditional/unary operator mutants. 

To run the mutant generator:

- Install [tree-sitter]: ```npm install tree-sitter-cli```
- Clone [tree-sitter-mojo]
- Run ```npx tree-sitter init-config```
- Edit the config.json file you just created so that tree-sitter-mojo directory is in one of the directories listed
- Run operator-mutant-gen.py in terminal, with the arguments being the mojo file you want to mutate then the type of mutants you want.
- Valid mutant types are at least one of: binary, comparison, boolean, unary, all
- ```python operator-mutant-gen.py <filepath> [mutant type...]```
- I'd suggest making run configs in your IDE for the above command

To run mojomut (ubuntu only):

- Have the above dependencies set up
- Have [pytest] and [pytest-mojo] installed
- Download tree-sitter compiled binary, setup $PATH for /bin/tree-sitter 
- Or edit mojomut.py to run tree-sitter via npm/npx/etc
- Have tests in same folder as mojo file you want to mutate
- Probably need to edit the last line in mojomut.py if you're not in a vscode ubuntu devcontainer
- Run ```python3 mojomut.py <filepath> [mutant type...]```

[tree-sitter]: https://github.com/tree-sitter/tree-sitter
[tree-sitter-mojo]: https://github.com/b-price/tree-sitter-mojo
[pytest]: https://docs.pytest.org/en/8.2.x/
[pytest-mojo]: https://github.com/guidorice/mojo-pytest


