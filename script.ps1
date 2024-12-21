# This script retrieves the list of running processes

Get-Process | Select-Object -Property Name, Id, CPU
