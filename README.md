# NOC Project

This is an outwardly propagating network on a chip that uses sequence encoding to arbitrate packets from various child nodes up a tree towards the root along with addressing information. This repository contains `.act` files designed to simulate asynchronous functionality for testing and experimentation purposes. The simulations leverage the `actsim` tool to execute predefined scenarios.

## Project Structure

- `.act` files: These files contain the simulation logic.
- `[module]test.rc`: Configuration file for running simulations.
- `[module]test.act`: Main simulation file.

## Requirements

To run the simulations, you will need to install `actsim` (the tool responsible for handling `.act` files).

### Installation

If you do not have actsim installed, you can visit the [actsim documentation]([https://example.com](https://avlsi.csl.yale.edu/act/doku.php?id=start)) to follow the detailed installation guide.

## Running a Simulation

To run the simulation, follow these steps:

1. Navigate to the directory containing your `.act` file.
2. Use the following command to run the simulation:

   ```bash
   echo "source [module]test.rc" | actsim [module]test.act test | tee [module]test.log
   ```

This will execute the simulation specified in `[module]test.act`, source the necessary environment variables from `[module]test.rc`, and log the output to `[module]test.log`.

## Logging

All simulation output will be logged into `[module]test.log`. You can examine this log to understand the step-by-step execution of the simulation and troubleshoot any potential issues.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests. All contributions are welcome!

## License

This project has no license.
