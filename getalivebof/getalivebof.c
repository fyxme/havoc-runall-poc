#include "getalivebof.h"

#define UNK_VAL "<unk>"

int go() {
    char hostname[256] = UNK_VAL;
    DWORD hostnameSize = sizeof(hostname);

    char username[256] = UNK_VAL;
    DWORD usernameSize = sizeof(username);

    if (!KERNEL32$GetComputerNameExA(ComputerNameDnsHostname, hostname, &hostnameSize)) {
        BeaconPrintf(CALLBACK_ERROR, "Failed to get hostname. Error code: %ld\n", KERNEL32$GetLastError());
    }

    if (!ADVAPI32$GetUserNameA(username, &usernameSize)) {
        BeaconPrintf(CALLBACK_ERROR, "Failed to get username. Error code: %ld\n", KERNEL32$GetLastError());
    }

    BeaconPrintf(CALLBACK_OUTPUT, "%s | %s\n", hostname, username);

    return 0;
}

