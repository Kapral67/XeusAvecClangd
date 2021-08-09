# for clangd
import shutil

# Jupyter root directory
c.NotebookApp.notebook_dir = '/home/jovyan/examples'

# Allow Hidden Files
c.ContentsManager.allow_hidden = True

#------------------------------------------------------------------------------
#   Language Server Implementations
#------------------------------------------------------------------------------

c.LanguageServerManager.language_servers = {
    "clangd": {
        # if installed as a binary
        "argv": [shutil.which("clangd", path="/home/jovyan/**CHANGE_THIS**/bin/"), "-pretty", "--clang-tidy", "--clang-tidy-checks='modernize*, readability*, performance*, bugprone*, cppcoreguidelines*'", "--completion-style=detailed", "--suggest-missing-includes", "--pch-storage=memory", "--log=verbose"],
        "languages": ["c++src", "csrc"],
        "version": 2
    }
}
