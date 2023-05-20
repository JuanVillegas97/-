#include <stdio.h>
#include "vm_files/virtual_machine.h"

int main() {
    // Initialize the virtual machine
    VirtualMachine vm;
    initVirtualMachine(&vm);

    // Execute instructions
    executeInstruction(&vm, 0);
    executeInstruction(&vm, 1);
    // ...

    return 0;
}
