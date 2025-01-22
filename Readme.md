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

1. Run the initial setup script:
   ```bash
   python3 cli/prompt.py --setup
   ```

2. Configure the CLI with your model details:
   ```bash
   tex -s --config <gemini-model> <model-api-key>
   ```
   Replace `<gemini-model>` with your model name and `<model-api-key>` with your API key.

You're now ready to use Vertex CLI!

---

## Usage

To start using Vertex CLI, simply type the following command:

```bash
tex "tell me about solar system"
```
![alt text](docs/readme_eg.png)

Replace `"tell me about solar system"` with any query you'd like. Vertex CLI will process your input and provide accurate, AI-generated insights.

---

## Features

- **Seamless Setup:** Quickly configure the CLI with minimal effort.
- **Flexible Queries:** Ask anything, and Vertex CLI will provide precise responses.
- **Powerful Integration:** Leverage advanced models with API key support.

---

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
