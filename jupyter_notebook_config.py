# Configuration file for lab.
import shutil

c.NotebookApp.notebook_dir = '/home/jovyan/examples'

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
