# Hello World API (Python)

This project from **API Workshop** demonstrates how to implement a simple API in Python. It is designed as a starting point for learning and practicing API development. The project also includes **unit tests** and **integration tests**.

---

## 🔧 Requirements

- Python **3.8+** (recommended 3.10 or later)
  If you don’t have Python installed, please refer to the document below to install it:

  [https://realpython.com/installing-python/](https://realpython.com/installing-python/)

---

## 🚀 How to Run

Make sure you have Git installed. If not, please refer to the document below to install it:

[https://github.com/git-guides/install-git](https://github.com/git-guides/install-git)

### 1. Open your terminal

On Windows, you can use **Command Prompt** or **PowerShell**.
On Mac or Linux, use the built-in **Terminal** app.

### 2. Get the source code

Clone this repository:
```bash
git clone https://github.com/apiworkshop-labs/apiworkshop-helloworld-api-python.git
cd apiworkshop-helloworld-api-python
```

### 3. Start the program

Run the main file with Python:
```bash
python src/app.py
```

You should see a message like:
```bash
Hello World API is serving on port 8000
```

### 4. Verify in browser

Launch your browser.

- Visit the base URL

  Open your web browser and go to:
  ```
  http://localhost:8000
  ```
  You will see:
  ```
  Hello, World!
  ```

- Visit the base URL with a **name** parameter, for example:
  ```
  http://localhost:8000/?name=Alice
  ```
  You will see:
  ```
  Hi Alice,
  How are you?
  ```

### 5. Stop the program

Press **CTRL+C** in the terminal to stop the server.

### 6. Run Unit Tests

```bash
python -m unittest tests/unit/test_helloworld.py
```

### 7. Run Integration Tests

Please stop the application before starting the integration tests to avoid conflicts.

```bash
python -m unittest tests/integration/test_helloworld_endpoints.py
```

---

## 📄 License

This project is for learning and demo purposes. Feel free to use, modify, or share it。
