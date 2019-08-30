
## Build Installers


### Windows 64-bit

1. install Python 2.7 for amd64

Note: if you have Python 2.7 32-bit and 64-bit both installed.  Please change the environment %PATH% to make sure that the python.exe (64-bit) and pip is used.


```
where python
```

2. install pip

Download get_pip.py from https://bootstrap.pypa.io/get-pip.py
Note: please use the python 2.7 64-bit version to install pip: e.g.

```
c:\Python27_amd64\python.exe get-pip.py
```

3. pip install numpy-1.9.1-cp27-none-win_amd64.whl

Note: you can find the file  numpy-1.9.1-cp27-none-win_amd64.whl under requirements/ directory

4. pip install scipy-0.15.1-cp27-none-win_amd64.whl

Note: you can find the file  scipy-0.15.1-cp27-none-win_amd64.whl under requirements/ directory

5. pip install PySAL==1.7.0

6. install wxPython3.0-win64-3.0.2.0-py27

Note: you can find the wxPython3.0-win64-3.0.2.0-py27.exe installation file under requirements/ directory. When installing wxPython, please choose the directory of python (64bit).

7. install py2exe

Note: you can find the py2exe-0.6.9.win64-py2.7.amd64.exe installation file under requirement/ directory.

If py2exe complains python is not found in registry. Open `Registry Editor`, goto `HKEY_LOCAL_MACHINE -> SOFTWARE -> Python -> PythonCore -> 2.7 ->InstallPath` and change the value of "Default" string-value to "C:\Python27amd64" 

8. copy libopenblaspy.dll to c:\windows\system32

9. run python setup.py.win py2exe

10. run inno setup with build/64bit.iss

### Mac OSX (10.7)

1. numpy 1.5.1

2. scipy 0.14.0

3. pysal 1.7.0

4. py2app 0.18

5. wx 2.9.5.0
