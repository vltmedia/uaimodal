set UAI_PATH_=M:\Projects\Apps\UAP_AI\01-Working\01-_User\99-Code\UAI\uaiInnoSetup\UAICore
rmdir /s /q dist

call %UAI_PATH_%\python.exe setup.py bdist_wheel --universal

rmdir /s /q build

call %UAI_PATH_%\Scripts\pip.exe install dist\uaimodal-1.1.5.9-py2.py3-none-any.whl --force-reinstall
call installWheelBrain.bat
call installWheelProgramData.bat