from mpi4py import MPI
import numpy as np
import time

def f(lam, phi, theta):
    """
    Compute the spectral radiance using Planck's law.

    Args:
        lam (float): Wavelength (meters).
        phi (float): Azimuthal angle (radians).
        theta (float): Polar angle (radians).

    Returns:
        float: Spectral radiance (W/m^2).
    """  
    c1 = 3.747e-16  # 2*pi*h*c*c [Wm^2]
    c2 = 1.4e-2   # h*c/k [mK] 
    Rsol = 6.96392e8  # Solar radius [m]
    Dsol = 1.496e11   # Distance Earth-Sun [m]
    T = 5782        # Surface temperature [K]
    f_t = np.cos(theta) * np.sin(phi)
    
    # Utilizar una versión segura de la exponencial para evitar desbordamientos
    Ed = f_t * (Rsol / Dsol) ** 2 * c1 / (lam ** 5 * (np.exp(c2 / (lam * T)) - 1.0))
    return Ed

def parallel(N):
    """
    Perform parallel Monte Carlo integration using MPI.

    Args:
        N (int): Total number of samples.

    Returns:
        None
    """
    
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    N_local = N // size  # Define the size of the local array 
    
    lam1, lam2 = 0.1e-9, 3000e-9
    the1, the2 = 0.0, np.pi / 2.0
    phi1, phi2 = 0.0, 2.0 * np.pi
    local_sum = 0.0

    wt = MPI.Wtime()

    # Estimate the local value of integrals
    for _ in range(N_local):
        lam = np.random.uniform(lam1, lam2)
        phi = np.random.uniform(phi1, phi2)
        theta = np.random.uniform(the1, the2)
        z = f(lam, phi, theta)
        local_sum += z

    # Reduce local sums to get the global sum
    global_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)
    wt = MPI.Wtime() - wt
    
    if rank == 0:
        integral_estimate = (t2 - t1) * (phi2 - phi1) * (lam2 - lam1) * global_sum / N
        return [N, integral_estimate, wt] 

# Total number of samples
N_values = [10000, 100000, 1000000, 10000000]
results = []
time_parallel = []  # Lista de tiempos en paralelo para los tres valores de N
time_serial = []  # Lista de tiempos en serie para los tres valores de N

# Calculate execution time for each N value
for N in N_values:
    t0 = time.time()
    results.append(parallel(N))
    time_parallel.append((time.time() - t0) / 60)  # Time in minutes

    # Calculate serial execution time
    t0_serial = time.time()
    for _ in range(3):   
        parallel(N)
    time_serial.append((time.time() - t0_serial) / 60)  # Time in minutes
    print(f"Execution times for N = {N}:")
    print(f"- Parallel: {time_parallel[-1]} minutes")
    print(f"- Serial: {time_serial[-1]} minutes")

    # Save the NumPy array to a file
    filename = f'serial_N_{N}.npy'
    np.save(filename, np.array(results[-1]))

# Convert the results list to a NumPy array
results_array = np.array(results)

# Save the NumPy array to a file
np.save('parallel_results.npy', results_array)