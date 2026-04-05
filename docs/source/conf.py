import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

project = "asm2dmodel"
author = "Taher Abunama"
copyright = "2026"
release = "0.1.0"

extensions = [
    "myst_parser",
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_title = "asm2dmodel"
html_short_title = "asm2dmodel"
html_static_path = ["_static"]
html_theme_options = {
    "titles_only": True,
    "navigation_depth": 2,
}
