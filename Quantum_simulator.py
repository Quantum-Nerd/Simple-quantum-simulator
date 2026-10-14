import numpy as np  # pyright: ignore[reportMissingImports]
import re
# ==========================================
# fuctions to apply gates
#==========================================
def create_initial_state( n ):
    Qubit = np.array([1,0j],dtype= complex)
    state = Qubit
    for _ in range (n - 1):
        state = np.kron(state, Qubit)   
    return state

def apply_CNOT(state , control, target, n ):
    total_states = 1 << n
    for i in range (total_states):
         if (i & (1 << control)) !=0  :
            j = i ^ (1 << target)
            if i<j :
                state[i], state[j] = state[j], state[i] 
    return state

def apply_X ( state, target,n):
    total_states = 1 << n
    for i in range (total_states):
         if (i & (1 << target)) ==0:
            j = i ^ (1 << target)
            if i<j :
                state[i], state[j] = state[j], state[i]
    return state

def apply_Hadamard ( state, target,n):
    total_states = 1 << n
    for i in range (total_states):
        if (i & (1 << target)) ==0  :
            j = i ^ (1 << target)
            if i<j :
                state[i], state[j] = (state[i]+state[j])/np.sqrt(2), (state[i]-state[j])/np.sqrt(2)
    return state

def apply_Z ( state, target ,n):
    total_states = 1 << n
    for i in range (total_states):
        if (i & (1 << target)) !=0:
             state[i] = -state[i]
    return state

def apply_S ( state, target,n):
    total_states = 1 << n
    for i in range (total_states):
        if (i & (1 << target)) !=0:
             state[i] = 1j*state[i] 
    return state      

def reading_gates(gates_applied,state,n) :
    commands = [ cmd.strip() for cmd in gates_applied.split(',')]
    for cmd in commands:
        if not cmd:
            continue
        match = re.match(r'^([A-Za-z]+)\s*([\d, \s]+)$', cmd)
        if not match:
            raise ValueError(f"Invalid gate format: {cmd}")
        gate_type = match.group(1).upper()
        qubits_string = match.group(2)
        qubits = [int(q) for q in re.findall(r'\d+' ,qubits_string)]
        for q in qubits:
            if q < 0 or q >= n:
                raise ValueError(
                    f"Invalid gate error: you chose {n} qubits, but qubit index {q} "
                    f"is outside the valid range 0 to {n - 1}."
                )
        if gate_type == 'H':
           if len(qubits)!= 1 :
               raise ValueError ("Hadmard gate requires 1 qubit , if you want to apply to more then qubit you can write it like this ( where 0,1,2 are the qubits you want to apply hadmard on) : H0,H1,H2...")
           state = apply_Hadamard ( state, qubits[0], n)
        elif gate_type == 'X':
           if len(qubits)!= 1 :
                  raise ValueError ("X gate requires 1 qubit , if you want to apply it to more then one qubit you can write it like this ( were 0,1,2 are the qubits you want to apply X on) : X0,X1,X2...")
           state = apply_X ( state, qubits[0], n)
        elif gate_type == 'Z':
           if len(qubits)!= 1 :
                  raise ValueError ("Z gate requires 1 qubit , if you want to apply it to more then one qubit you can write it like this ( were 0,1,2 are the qubits you want to apply Z on) : Z0,Z1,Z2...")
           state = apply_Z ( state, qubits[0], n)
        elif gate_type == 'S':
           if len(qubits)!= 1 :
                 raise ValueError ("S gate requires 1 qubit , if you want to apply it to more then one qubit you can write it like this ( were 0,1,2 are the qubits you want to apply S on) : S0,S1,S2...")
           state = apply_S( state, qubits[0], n)
        elif gate_type == 'CNOT':
            if len(qubits) !=2:
                raise ValueError(f"CNOT gate requires two qubits: {cmd}")
            if qubits[0] >= n or qubits[1]>= n :
                    raise ValueError("Control and target qubit indices must be less than the number of qubits.")   
            if qubits[0] == qubits[1] :
                    raise ValueError("Control and target qubits must be different for CNOT gate.")  
            else:
                state = apply_CNOT(state, qubits[0], qubits[1], n)
        else: 
            raise ValueError(f"Unknown gate : {gate_type}")  
    return state  

#def bra_ket_notation (state):
    ''' a function that rewrite the finall state in Bra-Ket notaion or Dirac notation'''
    
