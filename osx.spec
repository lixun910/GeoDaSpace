# -*- mode: python -*-
a = Analysis(['geodaspace/GeoDaSpace.py'],
             pathex=['/Volumes/SharedFolders/Home/Downloads/spreg'],
             hiddenimports=['pysal','pysal.core','pysal.core.FileIO','pysal.core.IOHandlers','pysal.core.IOHandlers.csvWrapper','scipy._lib.messagestream','scipy.special._ufuncs_cxx', 'scipy.sparse.csgraph._validation', 'scipy.io.matlab.streams'],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='GeoDaSpace',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='geodaspace/icons/geodaspace.icns')
app = BUNDLE(exe,
             name='GeoDaSpace.app',
             icon='geodaspace/icons/geodaspace.icns')
