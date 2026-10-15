
# Educational Quantum Simulator

An educational quantum simulator capable of simulating up to 25 qubits. It utilizes statevector simulation, eliminating the need to generate a massive system matrix to manipulate qubits. It supports essential quantum gates, such as Pauli and Hadamard gates, and is designed to be simple to use, allowing students to explore quantum circuits easily.

## Problem It Solves

Many quantum simulators require programming skills and specialized libraries, while simpler graphical tools often support only a limited number of qubits (typically 4-15). This simulator allows users to manipulate qubits through a simple interface, currently supporting up to 25 qubits, with potential for future expansion.

## Key Features

* **1. Qubit Capacity:** Supports circuits with up to 25 qubits.
* **2. Supported Quantum Gates:** Supports Hadamard (H), Pauli gates (X and Z), the phase gate (S), and Controlled-NOT (CNOT).
* **3. Automatic Output:** Automatically prints the statevector (amplitudes for every possible quantum state).
* **4. Simple Interaction:** Allows users to specify gate symbols and qubit indices without writing conventional code or performing the underlying linear algebra by hand.
* **5. Offline:** Runs locally without requiring an internet connection.

## Requirements

- Python 3.9 or higher
- NumPy
- pytest (for testing)

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Quantum-Nerd/Simple-quantum-simulator.git
cd Simple-quantum-simulator
```

2. **Install the libraries:**

```bash
pip install numpy pytest
```

## How to Use

**Run the project using the following command:**

```bash
python CLI.py
```

* **1. Choose the Number of Qubits.**

The program will first display:

```text
===Simple Quantum Simulator===
How many qubits do you want to use? (1-25):
```

Enter the number of qubits you want to work with.

Example:

`2`

* **2. Enter the Quantum Operations.**

The program will display the initial state of the system, then ask you to enter the operations you want to apply.

```text
the initial state of the system is: [1.+0.j 0.+0.j 0.+0.j 0.+0.j]
enter the gates you want to apply (e.g., H0, X1, ...) with the qubit index, from 0 to n-1, and separated by commas:
```

Supported gates: H, X, Z, S, and CNOT.

For single-qubit gates, write the gate symbol followed by the target qubit index. Separate multiple operations with commas.

Example:

```text
H0,CNOT 0 1
```

(Qubit indices start at 0 and end at n-1, where n is the number of qubits you selected.)

* **3. View the Result.**

After processing the operations, the program displays the resulting statevector, containing the amplitudes of the computational basis states.

```text
the final state of the system is: [0.70710678+0.j 0.        +0.j 0.        +0.j 0.70710678+0.j]
```

### Notes

* **Note 1: Using CNOT**

For a CNOT gate, write the control qubit index followed by a space and then the target qubit index.

Correct:

`CNOT 0 1`

Incorrect:

`CNOT 01`

`CNOT 0,1`

* **Note 2: Applying a Gate to Multiple Qubits**

To apply the Hadamard gate to three qubits, enter:

`H0,H1,H2`

Do not write `H012`, as each gate operation must specify its target qubit separately.

* **Note 3: Spaces and Lowercase Letters**

You can use spaces freely between the commas and use lowercase letters.

Correct:

`H0,Z0,CNOT 0 1`

`h0, Z0, cnOT 0   1`

* **Note 4: Performance**

The program may take minute or two minutes to run if the circuit includes 15 or more qubits because of Python loops. I will try to improve its performance in the coming weeks.

## Testing

The test file is `test_QS.py`.

Run the tests using:

```bash
pytest
```
