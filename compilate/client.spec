# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['../main.py'],  # Reference main.py in client/
    pathex=['..'],   # Add client/ to path
    binaries=[],
    datas=[('../.env', '.')],  # Include .env in client/
    hiddenimports=['PySide6', 'PySide6.QtCore', 'PySide6.QtWidgets', 'requests', 'pydantic', 'pydantic_settings', 'python_dotenv'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='client',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console for GUI
    disable_windowed_traceback=False,
    argv_emulation=False,
)