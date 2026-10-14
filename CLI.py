from Quantum_simulator import create_initial_state,reading_gates

#==========================================
# user interface & main execution
#==========================================
def CLI():
    print("=== Simple Quantum Simulator ===")

    while True:
        try:
            n = int (input("How many qubits do you want to use? (1-25): "))
            if 1 <= n <= 25:
                break
            else:
                print("Please enter a number between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 25.")
            
    state = create_initial_state( n )
    print ("the initial state of the system is: ", state)

    
    while True:
        try:
            gates_applied = str(input("enter the gates you want to apply (e.g.,H0,X1,...) with the qubit index ,from 0 to n-1 and separated by commas: ")).strip()
            final_state = reading_gates(gates_applied,state,n)
            print("the final state of the system is: ", final_state)
            break
        except Exception as error :
            print(f"Error :{error}")
            print("please try again.\n")
if __name__ == "__main__":
    CLI()  
    
    