#! Python 3.6.4
# Author: Alejandro Bautista Ramos

from openpyxl.styles import Font

def openpyxl_styles():
    font_headers = Font(name='Arial',
                        size = 14,
                        bold=True,
                        italic=False,
                        vertAlign=None,
                        underline=None,
                        color='FF000000',
                        )
    return font_headers
