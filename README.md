# Calculator Application

## Introduction

This project houses a versatile calculator application capable of performing basic arithmetic operations and managing calculation history. Designed with extendability in mind, it utilizes a plugin-based architecture to facilitate easy addition of new functionalities.

## Setup Instructions

### Requirements
- Python 3.8 or newer
- Git (optional, for cloning the repository)

### Installation
1. Clone the repository or download the source code:
   ```sh
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```sh
   cd midterm-main
   ```
3. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application
Execute the main script to start the application:
```sh
python main.py
```

## Usage Examples

### Calculator Operations
- Add: `add 5 3` (Outputs `8`)
- Subtract: `subtract 10 4` (Outputs `6`)
- Multiply: `multiply 6 7` (Outputs `42`)
- Divide: `divide 8 2` (Outputs `4`)

### History Management
- Save Calculation: Automatically saved after each operation.
- Load History: `load_history`
- Delete Specific Entry: `delete_history <entry_id>`
- Clear History: `clear_history`

## Architectural Decisions

The application adopts a modular and plugin-based architecture, enabling seamless integration and management of calculator operations and history functionalities. This design promotes scalability and ease of maintenance.

## Design Patterns

- **Command Pattern**: Utilized for implementing calculator operations and history management commands, facilitating easy addition and modification of functionalities.
- **Plugin Pattern**: Employs a dynamic discovery and loading mechanism for plugins, supporting extensibility by allowing new calculator operations or history commands to be added without altering the core application logic.

## Logging Strategy

Logging is configured via `logging.conf`, offering a flexible and centralized approach to managing log messages generated by the application. This strategy is crucial for debugging, monitoring application behavior, and auditing usage patterns.

## Testing

Tests are written using pytest. Run the following command to execute all tests:
```sh
pytest
```

## Continuous Integration and Deployment

The `.github/workflows/python-app.yml` file configures the CI/CD pipeline, automating tests and deployment processes. This ensures code quality and facilitates smooth deployment to production environments.

## Conclusion

This calculator application exemplifies a clean, modular design that can easily accommodate future expansion. Its logging and testing practices further underscore a commitment to quality and maintainability.
