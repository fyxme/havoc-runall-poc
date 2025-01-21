#include <stdio.h>
#include <windows.h>

#include "beacon.h"

WINBASEAPI WINBOOL WINAPI KERNEL32$GetComputerNameExA(COMPUTER_NAME_FORMAT NameType, LPSTR lpBuffer, LPDWORD nSize);
WINBASEAPI WINBOOL WINAPI ADVAPI32$GetUserNameA(LPSTR lpBuffer, LPDWORD pcbBuffer);
DECLSPEC_IMPORT DWORD WINAPI KERNEL32$GetLastError(void);

