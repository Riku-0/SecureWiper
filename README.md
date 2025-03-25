# 🛡️ SecureWiper  
*A safe and effective way to permanently erase sensitive data.*  

## 🔹 What is SecureWiper?  
SecureWiper is a **file and folder shredder** that permanently deletes data by overwriting it multiple times, ensuring it cannot be recovered. You can use it via a **drag-and-drop GUI** or through the **command line (CLI)** for flexible usage.  

✔ **Multiple overwrite passes** for security.  
✔ **Supports both files & folders.**  
✔ **Drag & Drop GUI for ease of use.**  
✔ **CLI mode for power users.**  

---

## 🚀 Installation  
### 1️⃣ Download & Install Python (if not installed)  
SecureWiper requires Python 3.6+. If you don’t have it, download it from [python.org](https://www.python.org/downloads/).  

### 2️⃣ Clone the Repository  
```sh
git clone https://github.com/Riku-0/SecureWiper.git
cd SecureWiper
```

### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

---

## 🖥️ Usage  
### 1️⃣ GUI Mode (Drag & Drop)  
Run the following command to open the GUI:  
```sh
python main.py
```
✅ A window will appear where you can **drag & drop** files or folders for secure deletion.  

### 2️⃣ CLI Mode (Command Line)  
```sh
python main.py cli <file/folder> [passes]
```
✅ Example:  
```sh
python main.py cli "C:\Users\Riku\Videos\secret.mp4" 5
```
💡 **Deletes the file with 5 overwrite passes.**  

---

## 🛠️ Features  
✔ **Overwrites files multiple times** before deletion.  
✔ **Renames files before removal** to make recovery harder.  
✔ **Securely deletes entire folders** (including subfiles).  
✔ **Cross-platform support** (Windows, Linux, MacOS).  
✔ **Easy-to-use GUI + Powerful CLI mode.**  

---

## ⚠️ WARNING  
SecureWiper **permanently deletes files** and **cannot recover them**. **Use with caution.**  

---

## 📜 License  
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.  

---

## 👨‍💻 Contributing  
Feel free to **fork** the repo and submit pull requests!  
