# -*- mode: python -*-
a = Analysis(['geodaspace/GeoDaSpace.py'],
             pathex=['v:\\Downloads\\spreg'],
             hiddenimports=['scipy.special._ufuncs_cxx', 'scipy.sparse.csgraph._validation', 'scipy.io.matlab.streams'],
             hookspath=None, runtime_hooks=None)
for d in a.datas:
    if 'pyconfig' in d[0]: 
        a.datas.remove(d)
        break
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='GeoDaSpace.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True, icon='geodaspace\\icons\\geodaspace.ico')
