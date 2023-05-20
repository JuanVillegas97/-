#ifndef VIRTUALMACHINE_H
#define VIRTUALMACHINE_H


typedef struct {
    int instructionPointer;
    int stackPointer;
    // ...
} VirtualMachine;

// Declaración de funciones de la máquina virtual
void initVirtualMachine(VirtualMachine* vm);
void executeInstruction(VirtualMachine* vm, int opcode);
// ...

#endif /* VIRTUALMACHINE_H */
