# Calculator Application - _Midterm Project_

## Introduction

This Python project is a robust application with a calculator and history management, geared for flexibility. It uses design patterns for scalable command execution and plugin-based activities to demonstrate best practices in coding, logging, and error handling. Configurable logging and cautiously exception handling tactics assure its durability and ease of maintenance, making it an excellent example of modern, adaptive software engineering.

## Setup Instructions

### Requirements

- Python 3.8 or newer
- Git (optional, for cloning the repository)

### Installation

1. Clone the repository or download the source code:
   ```sh
   git clone https://github.com/NidhishVyas/midterm
   ```
2. Navigate to the project directory:
   ```sh
   cd midterm
   ```
3. Activate virtual environment
   ```sh
   source venv/bin/activate
   ```
4. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. The calulator application stores the history of operations that are performed. The file directory where the history is stored should be specified in `.env` file:
   ```sh
   HIST_DIREC = "data/history.csv"
   ```

### Running the Application

Execute the main script to start the application:

```sh
python main.py
```

## Video Demonstration

### [Demo](https://drive.google.com/file/d/1DdTduJL9-FE7oSXyzc5VerbAyp2Ln3du/view?usp=sharing)

## Usage Examples

Upon launching the application, you'll be presented with the Main Menu. Here's how to navigate through its features:

### Main Menu

- To access the calculator, type `1` or `calculator`.
- To manage your calculation history, type `2` or `history`.

### Performing Calculator Operations

##### Addition:

1. From the Main Menu, enter `1` or `calculator`.
2. Choose `1` or `add`.
3. Enter the first number, then the second number. The result will be displayed.

##### Subtraction, Multiplication, Division:

- Follow similar steps as for Addition, but choose the corresponding operation.

### History Management

##### Clearing History:

1. From the Main Menu, enter `2` or `history`.
2. In the History Menu, choose `1` to remove all history entries.

##### Deleting a Specific Entry:

- Choose `2`, then follow the prompt to enter the index of the entry you wish to delete.

#### Viewing History:

- Choose `3` to view all past calculations.

## Architectural Decisions

The application's architecture is modular and plugin-driven, making it easy to integrate and manage calculator functions and history features. This technique promotes scalability while simplifying maintenance tasks.

## Design Patterns

In this project, command and plugin patterns seem to be implemented, as indicated by the structure within the `app/commands` and `app/plugins` directories. These patterns are useful for extending the application with new commands or plugins without modifying the core application logic.

- **Command Pattern**: Used to implement calculator operations and history management instructions, allowing for simple expansion and adjustment of functions. Implemented in `app/commands` to manage history-related operations. Commands encapsulate all the information needed to perform an action or trigger an event.
- **Plugin Pattern**: Offers a dynamic discovery and loading framework for plugins, which supports extensibility by allowing additional calculator operations or history commands to be added without changing the basic application logic. Implemented in `app/plugins/calculator` and `app/plugins/history`, allowing for the addition of calculator operations and history management features as plugins.

## Environment Variables

Environment variables are used to manage application settings and configurations external to the application code, which makes it easier to adapt to different environments without changing the code.

- **Usage** : It is used in `main.py` for configuration settings like directory of history file.

## Exception Handling

Exception handling in Python is managed through try/except blocks, commonly using two strategies: Look Before You Leap (LBYL) and Easier to Ask for Forgiveness than Permission (EAFP).

- **LBYL** : This approach involves checking for conditions before performing an operation to prevent exceptions from being raised.
- **EAFP** : This approach prefers to attempt the operation and catch exceptions if they occur, which is more aligned with Python's philosophy.
- **Usage** : Exception handling can be observed in operational scripts like those in `app/plugins/calculator` for handling division by zero or invalid inputs. While specific examples would require examining the code in detail, files like `app/plugins/calculator/add/__init__.py` or `app/plugins/calculator/divide/__init__.py` likely contain try/except blocks to handle potential calculation errors.

## Logging Strategy

The `logging.conf` file centralizes your application's logging configurations, allowing for easy modification and consistent logging across modules without requiring code changes. This configuration streamlines logging management by forwarding log entries to `logs/calculator.log`, allowing for detailed monitoring and efficient debugging, which aids in finding errors and understanding application behavior.

This strategy also improves security and compliance by consistently gathering log data, which allows for easier audits of system access and operations. A centralized logging configuration's flexibility and structure improve application stability, security, and maintenance, while also conforming with software development best practices.

## Testing

Tests are written using pytest. Run the following command to execute all tests:

```sh
pytest --pylint --cov
```

## Continuous Integration and Deployment

The `.github/workflows/python-app.yml` file sets up the CI/CD pipeline, automation test and deployment operations. This assures code quality and enables an effortless deployment to production settings.

## Conclusion

The calculator app's architecture is streamlined and modular, allowing for easy scalability and future improvements. This framework provides the smooth incorporation of new features without requiring substantial overhauls, guaranteeing that the program can easily adapt to changing needs. Rigorous testing and logging techniques improve its dependability and ease of maintenance by quickly identifying and resolving possible issues. This emphasis on modularity and quality assurance demonstrates the app's commitment to providing a long-lasting, high-performance platform that satisfies user expectations and enables efficient development.
