# Diagram Generator

## Introduction
This Python application leverages the `diagrams` library to generate architecture diagrams programmatically. It's designed to help developers and architects visualize cloud infrastructure and system architectures directly from code, making documentation more dynamic and maintainable.

## Features
- Generate architecture diagrams as images without the complexities of prerequisites of `diagrams` package based on different operating systems. 
- Easy to extend and integrate with CI/CD pipelines for automatic documentation updates.

## Prerequisites
- Docker
- Docker Compose (optional)

## Installation

### Using Docker (Recommended)
1. Clone this repository: `git clone https://github.com/mii9000/diagram-generator.git`

2. Navigate to the project directory: `cd diagram-generator`

3. To run the application do one of the following:
    ```
    chmod +x run.sh
    ./run.sh
    ```
    OR
    ```
    docker-compose up --build -d
    ```

## NOTE
Ensure you're in the project's root directory. The generated diagrams will be saved to the `./output` directory.

## Customizing Diagrams
To customize the diagrams, edit the `index.py` file and adjust the diagram components and connections as needed. Refer to the [Diagrams documentation](https://diagrams.mingrammer.com/docs) for more details on supported nodes and attributes.

## Contributing
Contributions are welcome! Please feel free to submit a pull request with your improvements or new features.

## License
This project is licensed under the MIT License.