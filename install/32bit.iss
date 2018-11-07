[Setup]
AppName=GeoDaSpace                                                      
AppPublisher=GeoDa Center
AppPublisherURL=https://spatial.uchiago.edu/
AppSupportURL=https://spatial.uchiago.edu/
AppUpdatesURL=https://spatial.uchiago.edu/
AppSupportPhone=(480)965-7533
AppVersion=1.1
DefaultDirName={pf}\GeoDa Software
DefaultGroupName=GeoDa Software
; Since no icons will be created in "{group}", we don't need the wizard
; to ask for a Start Menu folder name:
;DisableProgramGroupPage=yes
UninstallDisplayIcon={app}\GeoDaSpace.exe
Compression=lzma2
SolidCompression=yes
OutputDir=..\..
OutputBaseFilename=GeoDaSpace_setup_32bit
;OutputDir=userdocs:Inno Setup Examples Output

ChangesAssociations=yes

[dirs]
Name: "{app}";  Permissions: everyone-full; Check: InitializeSetup
Name: "{app}\GeoDaSpace";  Permissions: everyone-full; Check: InitializeSetup

[Files]
Source: "..\dist\*"; DestDir: "{app}\GeoDaSpace";
Source: "..\GeoDaSpace.ico"; DestDir: "{app}\GeoDaSpace"

[Icons]
Name: "{group}\GeoDaSpace"; Filename: "{app}\GeoDaSpace\GeoDaSpace.exe"
Name: "{group}\Uninstall GeoDaSpace"; Filename: "{uninstallexe}"
Name: "{commondesktop}\GeoDaSpace"; Filename: "{app}\GeoDaSpace\GeoDaSpace.exe"

[Registry]

[Code]
function IsX64: Boolean;
begin
  Result := Is64BitInstallMode and (ProcessorArchitecture = paX64);
end;

function IsIA64: Boolean;
begin
  Result := Is64BitInstallMode and (ProcessorArchitecture = paIA64);
end;

function IsOtherArch: Boolean;
begin
  Result := not IsX64 and not IsIA64;
end;

function VCRedistNeedsInstall: Boolean;
begin
  Result := not RegKeyExists(HKLM,'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{F0C3E5D1-1ADE-321E-8167-68EF0DE699A5}');
end;

function GetUninstallString: string;
var
  sUnInstPath: string;
  sUnInstallString: String;
begin
  Result := '';
  sUnInstPath := ExpandConstant('Software\Microsoft\Windows\CurrentVersion\Uninstall\GeoDaSpace_is1'); //Your App GUID/ID
  sUnInstallString := '';
  if not RegQueryStringValue(HKLM, sUnInstPath, 'UninstallString', sUnInstallString) then
    RegQueryStringValue(HKCU, sUnInstPath, 'UninstallString', sUnInstallString);
  Result := sUnInstallString;
end;

function IsUpgrade: Boolean;
begin
  Result := (GetUninstallString() <> '');
end;

function InitializeSetup: Boolean;
var
  V: Integer;
  iResultCode: Integer;
  sUnInstallString: string;
begin
  Result := True; // in case when no previous version is found
  if RegValueExists(HKEY_LOCAL_MACHINE,'Software\Microsoft\Windows\CurrentVersion\Uninstall\GeoDaSpace_is1', 'UninstallString') then  //Your App GUID/ID
  begin
    V := MsgBox(ExpandConstant('An old version of GeoDaSpace was detected. Please uninstall it before continuing.'), mbInformation, MB_YESNO); //Custom Message if App installed
    if V = IDYES then
    begin
      sUnInstallString := GetUninstallString();
      sUnInstallString :=  RemoveQuotes(sUnInstallString);
      Exec(ExpandConstant(sUnInstallString), '', '', SW_SHOW, ewWaitUntilTerminated, iResultCode);
      Result := True; //if you want to proceed after uninstall
      //Exit; //if you want to quit after uninstall
    end
    else
      Result := False; //when older version present and not uninstalled
  end;
end;