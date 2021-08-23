# XeusAvecClangd

Xeus-Cling jupyter kernel with llvm-project clangd running in jupyter-lsp extension to support language server protocol functions. This project allows for Language Server Protocol functions not only to operate in `.cpp` files, but also `.ipynb` files when loaded with the **xeus-cling C++ kernel**.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Kapral67/XeusAvecClangd.git/HEAD?urlpath=lab)

*<sub>Note: Commits/Tags/Pushes/Etc. must be signed starting 8/22/2021. Verified status may not be indefinite as certificates expire.</sub>*

## Usage
  - Adding a `compile_flags.txt` file allows further configuration of clangd.
  
  - Example file:

```
  -xc++
  -Weverything
```

  - Refer [here](https://clangd.llvm.org/design/compile-commands) for more detailed usage on `compile_flags.txt` & `compile_commands.json` files.
  
  - Clangd also accepts flags when executed as a binary. Refer to the **Language Server Implementations** section of `jupyter_notebook_config.py` to see which arguments are passed in this project.
  
## The Clangd Executable
  - Clangd must be recompiled for it to work properly with `.ipynb` files
  
  - A compiled binary built on **Ubuntu:Bionic_x86-64 (amd64)** can be found [here](https://github.com/Kapral67/Cling-Clangd.git).
