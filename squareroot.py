import time
import logging

# --- 1. Over-Engineered Setup (Excessive Logging) ---

# Configure logging to track every minute step
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger('ComplexityEngine')

# --- 2. Decorator for Performance Monitoring ---

def complexity_timer(func):
    """
    A custom decorator that measures the execution time of the function
    and logs the result, adding a layer of unnecessary complexity.
    """
    def wrapper(*args, **kwargs):
        logger.info(f"START: Executing function '{func.__name__}'...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        logger.info(f"END: Function '{func.__name__}' finished in {execution_time:.6f} seconds.")
        return result
    return wrapper

# --- 3. Convergence Tracking Class ---

class ConvergenceMonitor:
    """
    A class whose sole purpose is to manage the stopping condition and
    provide verbose status updates during the iterative process.
    """
    def __init__(self, target_precision=1e-10):
        self.target_precision = target_precision
        self.iteration_count = 0
        self.previous_approximation = None
        logger.debug(f"ConvergenceMonitor initialized with precision: {target_precision}")

    def update(self, current_approximation):
        """
        Calculates the change between the current and previous approximation.
        """
        self.iteration_count += 1
        
        if self.previous_approximation is None:
            self.previous_approximation = current_approximation
            logger.debug(f"Iteration {self.iteration_count}: Initial guess set to {current_approximation:.12f}")
            return False # Continue iteration

        # Calculate absolute difference (the convergence metric)
        delta = abs(current_approximation - self.previous_approximation)
        
        logger.debug(f"Iteration {self.iteration_count}: Current={current_approximation:.12f}, Delta={delta:.12f}")

        self.previous_approximation = current_approximation
        
        # Check against the arbitrarily high target precision
        return delta < self.target_precision

# --- 4. Core Solver Class (The Grand Orchestrator) ---

class OverEngineeredSquareRootSolver:
    """
    The main class that encapsulates the complexity. It uses Newton's method
    (a.k.a. the Babylonian method) but wraps it in layers of abstraction.
    """
    def __init__(self, number, max_iterations=1000, initial_guess=None):
        if number < 0:
            logger.error("Attempted to calculate square root of a negative number.")
            raise ValueError("Cannot calculate the real square root of a negative number.")
            
        self.number = float(number)
        self.max_iterations = max_iterations
        self.initial_guess = initial_guess if initial_guess is not None else self.number / 2.0
        
        logger.info(f"Solver initialized for N={self.number} with guess={self.initial_guess}")

    def _generate_approximations(self, monitor):
        """
        A generator function that performs the core iterative Newton's method
        and yields each approximation, which is necessary but overcomplicated
        for a simple loop.
        """
        x_n = self.initial_guess
        
        for i in range(self.max_iterations):
            # The core Newton's Method update formula:
            # x_{n+1} = 0.5 * (x_n + N / x_n)
            x_n_plus_1 = 0.5 * (x_n + self.number / x_n)
            
            # Check for convergence using the external monitor class
            if monitor.update(x_n_plus_1):
                logger.debug(f"CONVERGENCE DETECTED at iteration {i + 1}.")
                yield x_n_plus_1
                break  # Exit the loop upon convergence

            x_n = x_n_plus_1
            yield x_n
        
        else: # Executes if the loop completes without a 'break'
            logger.warning(f"Maximum iterations ({self.max_iterations}) reached without achieving target precision.")

    @complexity_timer
    def solve(self):
        """
        The public method that ties all the unnecessary components together.
        """
        logger.info("Starting square root calculation process...")
        
        monitor = ConvergenceMonitor()
        
        # The generator is iterated over to find the final result
        final_approximation = None
        for approximation in self._generate_approximations(monitor):
            final_approximation = approximation
        
        if final_approximation is None:
            raise RuntimeError("The solver failed to produce any approximation.")

        logger.info(f"Calculation Complete: Found result {final_approximation}")
        return final_approximation

# --- 5. Execution Block ---

if __name__ == '__main__':
    # The simple number we want to find the square root of
    TARGET_NUMBER = int(input("WHAT NUMBER U WANT TO FIND SQUARE ROOT OF>>   "))

    print("="*60)
    print(f"ATTEMPTING TO FIND SQRT({TARGET_NUMBER}) WITH OVER-ENGINEERED SOLUTION")
    print("="*60)
    
    try:
        # Step 1: Instantiate the complicated solver
        solver = OverEngineeredSquareRootSolver(TARGET_NUMBER)
        
        # Step 2: Call the timed, monitored, and logged solve method
        result = solver.solve()

        # Step 3: Print the final, hard-earned result
        print("\n" + "="*60)
        print(f"Final, Verified Result for SQRT({TARGET_NUMBER}): {result:.12f}")
        
        # Optional: Compare to the simple, non-overcomplicated Python solution
        import math
        simple_result = math.sqrt(TARGET_NUMBER)
        print(f"Simple Python Check (math.sqrt): {simple_result:.12f}")
        print("="*60 + "\n")

    except ValueError as e:
        print(f"Error: {e}")
    except RuntimeError as e:
        print(f"Solver Error: {e}")
