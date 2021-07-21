# XeusAvecClangd
Xeus-Cling jupyter kernel with llvm-project clangd running in jupyter-lsp extension to support language server protocol functions.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Kapral67/XeusAvecClangd.git/HEAD?urlpath=lab)

## Jump
- Under `Conventional`, open `main.cpp` go to line 49 and try jump on `substr` ([alt or option] + left_click)
- Jump also works on the functions defined by the `.h` files in the `Conventional` folder.

## Updates (5/14/2021)
 - Adding a `command_flags.txt` file should allow clangd to work for xeus-cling `.ipynb` files without a custom compiled clang-tools-extra as described below
  - Put the compile flag `-xc++`
  - Example file:
  ```
  -xc++
  -Weverything
  ```

## Updates (4/3/2021)
 - LSP is working in binder now
 - Go to `examples/conventional`
 - open a `.cpp` file and familiar jupyterlab-lsp functions will work (hover, jump, rename, etc.)
 - this only works with native files and does not work in this binder with `.ipynb` files yet. **See Below for more details**

~~### Notebooks not working
~- clangd does not recognize `.ipynb` files as C++ files
~- [this](https://github.com/Kapral67/llvm-project/commit/c972f366a8a7fa61b56b3045f15c25d3ff353e1d) hack can be used to fix this issue
~- The problem is that this means the source code must be compiled manually into a binary.
~- For binder as of date, it opens an Ubuntu 18.04 LTS image that uses glibc version 2.27.
~- [The repository](https://github.com/Kapral67/llvm-project/tree/c972f366a8a7fa61b56b3045f15c25d3ff353e1d) is using a later version of clangd than 11.0.0 and the binary I have compiled from it does not work in binder since I am running Ubuntu 20.04 LTS and compiled it with glibc version 2.29 (glibc-2.29 could also be a dependent of clangd-12+, but I'm not sure)
~- The hack (first link) could easily be migrated to a fork of the [clangd stable release 11.0.0](https://github.com/llvm/llvm-project/tree/176249bd6732a8044d457092ed932768724a6f06) and an appropriate binary for Ubuntu 18.04 LTS compiled from source; however, I am too lazy at least for the time being.
