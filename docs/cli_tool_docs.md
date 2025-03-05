# **CLI Documentation**

## **Commands**

- **Convert an array to a NumPy array**
  ```bash
  tex "how to convert an array into a NumPy array"
  ```

- **Manage API keys for models**
  - Add a model and its API key:
    ```bash
    tex --config <model-name> <api-key>
    ```
  - Remove a model:
    ```bash
    tex --remove <model-name>
    ```
  - List all saved models and their API keys:
    ```bash
    tex --list
    ```
  - Select a model to use:
    ```bash
    tex --select
    ```
  - Show available commands:
    ```bash
    tex --help
    ```

## **Debugging (Beta Feature)**

To check for issues in the last two commands, use:
```bash
tex --debug
```

To debug a specific number of recent commands, add a number after `--debug`. For example, to check the last five commands:
```bash
tex --debug --5
```

You can also add a custom message to explain your assumptions or observations:
```bash
tex "I think this issue might be related to environment variables" --debug
```

---
