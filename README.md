# XeusAvecClangd
Xeus-Cling jupyter kernel with llvm-project clangd running in jupyter-lsp extension to support language server protocol functions.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Kapral67/XeusAvecClangd.git/HEAD?urlpath=lab)

## Jump
- Under `Conventional`, open `main.cpp` go to line 49 and try jump on `substr` ([alt or option] + left_click)
- Jump also works on the functions defined by the `.h` files in the `Conventional` folder.

## Updates (5/14/2021)
 - Adding a `compile_flags.txt` file should allow clangd to work for xeus-cling `.ipynb` files without a custom compiled clang-tools-extra as described below
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

### Notebooks Working! Update (8/9/2021)
- 
