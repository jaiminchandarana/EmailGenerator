# Email Generator

This email generator is developed in python using langchain and designed to generate email for jobs based on job description.

## Prerequisites

1.  **Make sure you have Python installed on your system.**
  - Download Python from [Microsoft Store](https://www.microsoft.com/store/productId/9NCVDN91XZQP?ocid=pdpshare) or from the [official Python website](https://www.python.org/downloads/).

2.  **Add Python to System Path**:

- Ensure Python is added to your system path. By default, Python is usually located at:

```

C:\Users\[Your Username]\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts

```

- To add Python to your path:

- Open **Environment Variables** > **System Variables** > **Path** > **Edit**.

- Add the path to your Python directory containing `ipython.exe` (usually in the folder listed above).

- Click **OK** to save.

3.  **Create Groq cloud api key**:
- Download Python from [Groq cloud api key](https://www.microsoft.com/store/productId/9NCVDN91XZQP?ocid=pdpshare).
- Add that api key in Generator.py 
    


## Steps to Run the Project

1. **Open the Project Folder in Command Prompt (cmd)**:

- Open cmd and navigate to the folder using the cd command:
```
cd path/to/your/folder

```
- Open the folder, right-click, and select `Open with CMD`.

- Open the folder, type cmd in the address bar, and hit Enter.
  

2. **Install Dependencies**:

Run the following command in cmd to install the required dependencies:
```
pip install -r requirements.txt
```

3. **Run the Project**:

You can run `generate.py` in any IDE of your choice or execute it directly from cmd:
```
python generate.py
```
