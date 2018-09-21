$ErrorActionPreference = 'Stop'

$packagename  = 'pypy3'
$toolsdir     = "$(Split-Path -parent $MyInvocation.MyCommand.Definition)"
$url          = 'https://bitbucket.org/pypy/pypy/downloads/pypy3-v6.0.0-win32.zip'
$checksum     = '72dddb3746a51f7672c77d619c818e27efe899e08ae82762448e50dbfdc2f5f3'
$checksumType = 'sha256'

$packageargs = @{
  packagename   = $packagename
  unzipLocation = $toolsdir
  url           = $url
}

Install-ChocolateyZipPackage @packageargs

$files = Get-ChildItem $toolsdir -include *.exe -recurse

foreach ($file in $files) {
    if ($file.Name.Contains("wininst")) {
      New-Item "$file.ignore" -type file -force | Out-Null
    }
}
