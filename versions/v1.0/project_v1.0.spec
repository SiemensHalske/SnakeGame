# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['C:\\Users\\Hendrik\\Documents\\Github\\SnakeGame\\src\\main.py'],
             pathex=['C:\\Users\\Hendrik\\Documents\\Github\\SnakeGame'],
             binaries=[],
             datas=[('C:\\Users\\Hendrik\\Documents\\Github\\SnakeGame\\assets\\', 'assets'), ('C:\\Users\\Hendrik\\Documents\\Github\\SnakeGame\\docs\\', 'docs')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SnakeGame',
          description='Snake Game',
          copyright='Copyright © 2024, SiemensHalske',
          company_name='SiemensHalske',
          product_name='Snake Game',
          internal_name='HaihappenUhaha',
          original_filename='SnakeGame.exe',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon='C:\\Users\\Hendrik\\Documents\\Github\\SnakeGame\\icon.ico')  

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='C:\\Users\\Hendrik\\Documents\\Github\\SnakeGame\\versions\\v1.0\\SnakeGame')
