#!/usr/bin/env python

import PyInstaller.__main__

PyInstaller.__main__.run([
    'skip.spec',
    '--onefile',
    '--noconfirm',
    '--clean',
])