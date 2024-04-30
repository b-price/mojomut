MojoMut 🔥
==============
A mutation testing tool for Mojo programming language.
Currently generates arithmetic/boolean/conditional/unary operator mutants. 

To run:

- Install [tree-sitter]: ```npm install tree-sitter-cli```
- Clone [tree-sitter-mojo]
- Run ```npx tree-sitter init-config```
- Edit the config.json file you just created so that tree-sitter-mojo directory is in one of the directories listed
- Run operator-mutant-gen.py in terminal, with the arguments being the mojo file you want to mutate then the type of mutants you want.
- Valid mutant types are at least one of: binary, comparison, boolean, unary, all
- ```python operator-mutant-gen.py <filepath> [mutant type...]```
- I'd suggest making run configs in your IDE for the above command

[tree-sitter]: https://github.com/tree-sitter/tree-sitter
[tree-sitter-mojo]: https://github.com/b-price/tree-sitter-mojo


