# Vertex CLI

Vertex CLI is a powerful command-line tool designed to streamline your workflows and integrate AI capabilities seamlessly. With just a few commands, you can set up and start using advanced features like querying models and generating insights.

---

## Installation

Follow these steps to get started:

1. Clone the repository:
   ```bash
   git clone https://github.com/Prtm2110/Vertex-CLI
   cd Vertex-CLI
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Setup

1. Run the initial setup script to install the package:
   ```bash
   pip install .
   ```

2. After the installation, execute the setup command:
   ```bash
   tex --setup
   ```

3. Configure the CLI with your model details:
   ```bash
   tex --config gemini-1.5-flash <model-api-key>
   ```
   Replace `gemini-1.5-flash` with your model name and `<model-api-key>` with your API key.

You're now ready to use Vertex CLI!

---

## Usage

To start using Vertex CLI, simply type the following command:

```bash
tex "tell me about solar system"
```
![alt text](docs/eg_matplotlib.gif)

Replace `"tell me about solar system"` with any query you'd like. Vertex CLI will process your input and provide accurate, AI-generated insights.

---

### Debugging Mode (Beta Feature)

Debugging functionality is currently under development but can already be utilized to analyze issues with recent commands. Here’s how to use it:

Debug the Last Two Commands

To identify potential issues with the last two executed commands, use:

```bash
tex --debug
```

### Customize the Number of Commands to Analyze

You can specify the number of recent commands to debug by adding the `--5` flag (or replace `5` with your desired number):

```bash
tex --debug --5
```

### Add a Custom Debugging Message

When debugging, you can include a custom message to specify your assumptions or observations. For example:

```bash
tex "I believe this can be solved by changing the environment variable" --debug
```

This helps provide context and ensures more targeted debugging insights.



## Contributing

Contributions are welcome! If you'd like to improve Vertex CLI or add new features:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Support

If you encounter any issues, feel free to open an issue on the [GitHub repository](https://github.com/Prtm2110/Vertex-CLI/issues).

---

### Enjoy using Vertex CLI to power your workflows with AI!
