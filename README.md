
# CHSH Game Implementation Using Quantum Computing

## Team Details

| Name             | Roll No.     |
| ---------------- | ------------ |
| Prajwal Gundala  | S20240010079 |
| Nikitha Budaraju | S20240010163 |
| Siri Hasini      | S20240010124 |

---

# 1. Project Overview

The **CHSH (Clauser-Horne-Shimony-Holt) game** is a fundamental example used to demonstrate the difference between classical and quantum correlations.

In this project, the CHSH game is implemented using **Qiskit** and executed on an **IBM Quantum Hardware through cloud instances in free tier.**

The project follows the complete workflow from:

- Understanding the classical CHSH strategy
- Implementing the game using Python
- Preparing an entangled quantum state
- Constructing the quantum circuits
- Simulating the circuits
- Connecting Qiskit to IBM Quantum
- Executing the circuits on real quantum hardware
- Analysing the resulting measurements

***The main objective is to demonstrate how quantum entanglement can produce correlations that exceed the classical CHSH limit.***

---

# 2. CHSH Game

The CHSH game involves two players, **Alice** and **Bob**.

Alice receives a binary input

$$
x \in \{0,1\}
$$

and Bob receives a binary input

$$
y \in \{0,1\}.
$$

Each player produces a binary output:

$$
a,b \in \{0,1\}.
$$

The players win the game when

$$
a \oplus b = x \land y.
$$

Therefore, the winning conditions are:

| \(x\) | \(y\) | Winning condition |
| ----: | ----: | ----------------- |
|     0 |     0 | \(a=b\)           |
|     0 |     1 | \(a=b\)           |
|     1 |     0 | \(a=b\)           |
|     1 |     1 | \(a\neq b\)       |

The important idea is that Alice and Bob cannot communicate after receiving their inputs.

A classical strategy can achieve a maximum winning probability of **75%**, ***whereas a quantum strategy using entanglement can exceed this limit.***

---

# 3. IBM Quantum Setup

The quantum circuits in this project are executed using IBM Quantum's cloud-based quantum computing infrastructure.

The setup consists of the following steps:

1. Create an IBM Quantum account. ([quantum.cloud.ibm.com](https://quantum.cloud.ibm.com/))
2. Create or access an IBM Quantum instance.
3. Obtain an API key from the IBM Quantum platform.
4. Install the required Qiskit packages.
5. Save the IBM Quantum credentials locally.
6. Connect the Python environment to the IBM Quantum service.
7. Select an available quantum backend.
8. Submit the quantum circuits for execution.

The IBM Quantum platform provides access to real quantum processors as well as simulator backends.

---

# 4. IBM Quantum Account and Instance

An IBM Quantum account is required to access IBM's quantum computing services.

After signing in to the IBM Quantum platform:

- An IBM Quantum instance is selected or created.
- The instance provides access to IBM Quantum Runtime services.
- An API key is generated for authentication.
- The selected instance and API key are then used by Qiskit to establish the connection.

The API key should be kept private and should **not be directly exposed in the notebook or shared publicly**.
