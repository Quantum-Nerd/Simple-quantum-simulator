import pytest # pyright: ignore[reportMissingImports]
import numpy as np  # pyright: ignore[reportMissingImports]
from Quantum_simulator import create_initial_state,apply_Hadamard,apply_X,apply_S,apply_Z,apply_CNOT
n=int

@pytest.mark.parametrize ("n,expected_n" ,[(1, np.array([1+0j,0j],dtype=complex)),(2,np.array([1+0j,0j,0j,0j],dtype=complex)),(3,np.array([1+0j,0j,0j,0j,0j,0j,0j,0j]))
])
def test_creat(n,expected_n):
    result = create_initial_state(n)
    assert np.allclose(result,expected_n)

@pytest.mark.parametrize(
    "state, qubit_index, n_qubits, expected",
    [
        (
            np.array([1 + 0j, 0 + 0j], dtype=complex),
            0,
            1,
            np.array([0.70710678 + 0j, 0.70710678 + 0j], dtype=complex),
        ),
        (
            np.array([0 + 0j, 1 + 0j], dtype=complex),
            0,
            1,
            np.array([0.70710678 + 0j, -0.70710678 + 0j], dtype=complex),
        ),
        (
            np.array([0.70710678 + 0j, 0.70710678 + 0j], dtype=complex),
            0,
            1,
            np.array([1 + 0j, 0 + 0j], dtype=complex),
        ),
    ],
)
def test_hadamard(state, qubit_index, n_qubits, expected):
    result = apply_Hadamard(state, qubit_index, n_qubits)
    assert np.allclose(result, expected)


@pytest.mark.parametrize(
    "state, qubit_index, n_qubits, expected",
    [
        (
            np.array([1 + 0j, 0 + 0j], dtype=complex),
            0,
            1,
            np.array([0 + 0j, 1 + 0j], dtype=complex),
        ),
        (
            np.array([0 + 0j, 1 + 0j], dtype=complex),
            0,
            1,
            np.array([1 + 0j, 0 + 0j], dtype=complex),
        ),
        (
            np.array([0.70710678 + 0j, 0.70710678 + 0j], dtype=complex),
            0,
            1,
            np.array([0.70710678 + 0j, 0.70710678 + 0j], dtype=complex),
        ),
        (
            np.array([0.70710678 + 0j, -0.70710678 +0j],dtype=complex)
            ,0
            ,1
            ,np.array([-0.70710678 + 0j, 0.70710678 + 0j],dtype=complex)
        )
    
    
    ],
)
def test_X(state, qubit_index, n_qubits, expected):
    result = apply_X(state, qubit_index, n_qubits)
    assert np.allclose(result, expected)

@pytest.mark.parametrize(
    "state, qubit_index, n_qubits, expected",
    [
        (
            np.array([1 + 0j, 0 + 0j], dtype=complex),
            0,
            1,
            np.array([1 + 0j, 0 + 0j], dtype=complex),
        ),
        (
            np.array([0 + 0j, 1 + 0j], dtype=complex),
            0,
            1,
            np.array([0 + 0j, 0 + 1j], dtype=complex),
        ),
    ],
)
def test_S(state, qubit_index, n_qubits, expected):
    result = apply_S(state, qubit_index, n_qubits)
    assert np.allclose(result, expected)


