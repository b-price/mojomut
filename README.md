MojoMut 🔥
==============
A mutation testing tool for Mojo programming language.
Currently generates arithmetic mutants. 

To run:

- Install [tree-sitter] 
- Clone [tree-sitter-mojo]
- Run ```npx tree-sitter init-config```
- Edit the config.json file you just created so that tree-sitter-mojo directory is in one of the directories listed
- Run mojo-parse in terminal, with the argument being the mojo file you want to mutate.
- ```python mojo-parse.py <filepath>```

[tree-sitter]: https://github.com/tree-sitter/tree-sitter
[tree-sitter-mojo]: https://github.com/b-price/tree-sitter-mojo


