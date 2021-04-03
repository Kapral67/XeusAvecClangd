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
        "argv": [shutil.which("clangd", path="/home/jovyan/clangd_11.0.0/bin/"), "-pretty"],
        "languages": ["c++src", "csrc"],
        "version": 2
    }
}
