# -*- mode: python -*-

block_cipher = None


a = Analysis(['geodaspace/GeoDaSpace.py'],
             pathex=['/Library/Python/2.7/site-packages', '/Library/Python/2.7/site-packages/PySAL-1.7.0-py2.7.egg/', '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/', '/Users/xun/Downloads/GeoDaSpace'],
             binaries=[],
             datas=[],
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
          [],
          exclude_binaries=True,
          name='GeoDaSpace',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='GeoDaSpace')
