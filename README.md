# Language Translator

A simple language translation web application built with Django, Tailwind CSS, and Python's `translate` library. This project allows users to enter text, select a target language, and get translations. It includes a user-friendly interface with modern design elements.

## Features

- Text input and language selection
- Translation functionality using the `translate` library
- Responsive design with Tailwind CSS
- User feedback messages that appear during translation

## Technologies Used

- **Django**: Web framework for the backend
- **Tailwind CSS**: Utility-first CSS framework for styling
- **Python Translate Library**: For handling translations

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/Prokelly/language-translator.git
    cd language-translator
    ```

2. **Set Up a Virtual Environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Install Tailwind CSS**:

    Ensure that Tailwind CSS and its dependencies are properly set up. If you encounter issues, consult the Tailwind CSS documentation for the correct installation steps.

5. **Run Migrations**:

    ```bash
    python manage.py migrate
    ```

6. **Run the Development Server**:

    ```bash
    python manage.py runserver
    ```

7. **Access the Application**:

    Open your web browser and go to `http://127.0.0.1:8000/` to start using the application.

## Usage

1. **Enter Text**: In the input field, type the text you want to translate.
2. **Select Language**: Choose the target language from the dropdown menu.
3. **Click Translate**: Submit the form to see the translated text.
4. **View Translation**: The translated text will be displayed below the form.

## Project Structure

- `myapp/`: Contains the main Django application code.
  - `migrations/`: Database migrations.
  - `static/`: Static files including Tailwind CSS.
  - `templates/`: HTML templates.
  - `views.py`: Logic for handling requests and responses.
- `requirements.txt`: List of Python dependencies.
- `manage.py`: Django's command-line utility.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please follow these steps:

1. **Fork the Repository**: Click on the "Fork" button at the top right of this page.
2. **Create a Branch**:

    ```bash
    git checkout -b feature/your-feature
    ```

3. **Make Your Changes**.
4. **Commit Your Changes**:

    ```bash
    git add .
    git commit -m "Add your message here"
    ```

5. **Push to Your Fork**:

    ```bash
    git push origin feature/your-feature
    ```

6. **Create a Pull Request**: Go to the original repository and click on "New Pull Request."

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, you can reach me at [your.email@example.com](mailto:your.email@example.com).

