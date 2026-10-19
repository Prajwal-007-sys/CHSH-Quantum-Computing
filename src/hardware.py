from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager


# ---------------------------------------------------------
# IBM Quantum account setup
# ---------------------------------------------------------

# Replace "API_token" with your IBM Quantum API token.
# Replace "CRN_num" with your IBM Quantum instance CRN.
#
# Run this ONCE on your machine to save the credentials locally.
#
# token = "API_token"
#
# QiskitRuntimeService.save_account(
#     channel='ibm_quantum_platform',
#     instance='CRN_num',
#     token=token,
#     overwrite=True,
#     set_as_default=True
# )
#
# After running save_account() once, you do not need to
# provide the token again on this machine.

def connect_to_ibm():
    return QiskitRuntimeService(
        channel='ibm_quantum_platform'
    )


def get_backend(service, backend_name="ibm_fez"):
    return service.backend(backend_name)


def create_sampler(backend):
    return Sampler(mode=backend)


def transpile_for_backend(circuits, backend, optimization_level=3):
    pass_manager = generate_preset_pass_manager(
        target=backend.target,
        optimization_level=optimization_level
    )
    return [pass_manager.run(circuit) for circuit in circuits]


def run_on_hardware(sampler, circuits, shots=1000):
    return sampler.run(circuits, shots=shots)


def get_job_result(job):
    return job.result()


def get_counts_from_result(result):
    all_counts = []

    for pub_result in result:
        counts = pub_result.data.c.get_counts()
        all_counts.append(counts)

    return all_counts