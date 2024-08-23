
# Deploy Module for uaimodal Python Package

## Overview

The `Deploy` module is part of the `uaimodal` Python package and provides a suite of methods to assist with deploying and managing containerized applications. This module is designed to handle various tasks such as installing Python dependencies, copying files, downloading resources, and configuring containers.

## Installation

To install the `uaimodal` package, you can use pip:

```bash
pip install uaimodal
```

## Features

The `Deploy` module includes the following key methods:

### 1. `installPythonRequirementsLocal(localPath: str)`
Installs Python requirements from a local `requirements.txt` file.

**Arguments:**
- `localPath (str)`: The path to the local `requirements.txt` file.

**Returns:**
- Updated Docker image with installed requirements.

### 2. `installPythonRequirementsServer(serverPath: str = "/root/requirements.txt")`
Installs Python requirements from a server `requirements.txt` file.

**Arguments:**
- `serverPath (str, optional)`: The path to the `requirements.txt` file on the server.

**Returns:**
- Updated Docker image with installed requirements.

### 3. `copyLocalFileAndDirectories(items: list)`
Copies local files and directories to the image.

**Arguments:**
- `items (list)`: A list of directories to copy, each containing an input and output path.

**Returns:**
- Updated Docker image with copied files and directories.

### 4. `copyLocalFiles(files: list)`
Copies local files to the specified image.

**Arguments:**
- `files (list, optional)`: A list of files and directories to be copied.

**Returns:**
- Updated Docker image with copied files.

### 5. `downloadFile(url: str, destination: str)`
Downloads a file from a URL and saves it to the specified destination.

**Arguments:**
- `url (str)`: The URL of the file to download.
- `destination (str)`: The destination path where the file will be saved.

**Returns:**
- Updated Docker image with the downloaded file.

### 6. `unzipFile(source: str, destination: str)`
Unzips a file from a source path to a destination path.

**Arguments:**
- `source (str)`: The path to the zip file.
- `destination (str)`: The path where the files will be extracted.

**Returns:**
- Updated Docker image with the unzipped files.

### 7. `installGitModule(repo_url: str, destination: str)`
Clones and installs a Git module.

**Arguments:**
- `repo_url (str)`: The URL of the Git repository.
- `destination (str)`: The path where the module will be installed.

**Returns:**
- Updated Docker image with the installed Git module.

### 8. `initContainer(appName: str, ... various options ...)`
Initializes a container with the given parameters, including optional file downloads, unzipping, Git module installations, and Python requirements installations.

**Arguments:**
- `appName (str)`: The name of the application to deploy.
- `python_version (str, optional)`: The Python version to use in the container.
- `firebaseServiceJson (str, optional)`: Path to Firebase service JSON file.
- `cmake (bool, optional)`: Whether to install CMake.
- `cudaVersion (str, optional)`: CUDA version to install.
- `filesToDownload (list, optional)`: List of files to download.
- `filesToUnzip (list, optional)`: List of files to unzip.
- `gitModules (list, optional)`: List of Git modules to install.
- `requirementsLocal (str, optional)`: Path to local Python requirements file.
- `requirementsServer (str, optional)`: Path to server Python requirements file.
- `postFunctions (list, optional)`: List of functions to run post-initialization.
- `pytorchCustom (str, optional)`: Path to custom PyTorch installation.
- `ffmpeg (bool, optional)`: Whether to install FFmpeg.
- `newDirectories (list, optional)`: List of new directories to create in the container.

**Returns:**
- Initialized `UAIModal` object.

## Usage

To use the `Deploy` module, first import it and then initialize it with the desired configuration:


```python
import uaimodal

uModal = uaimodal.initUAIContainer("testToKill-01", python_version= "3.11",firebaseServiceJson= "user.json",cudaVersion=12.4, ffmpeg=True, newDirectories=["/root/datasets/input"])
uModal.installGitModule( "https://github.com/OpenTalker/video-retalking","/root")
uModal.downloadFile( "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4", "/root/BigBuckBunny.mp4" )
uModal.copyLocalFileAndDirectories([["checkpoints.zip", "/root/checkpoints.zip"]])
uModal.unzipFile( "/root/checkpoints.zip", "/root")
uModal.installCMake()
uModal.installPythonRequirementsServer( "/root/requirements.txt")
uModal.copyLocalFileAndDirectories( [
    ["usersilence.wav", "/root/usersilence.wav"],
    ["short.wav", "/root/short.wav"],
    ["testVideo.mp4", "/root/testVideo.mp4"]
    ["extract_kp_videos.py", "/root/third_part/face3d/extract_kp_videos.py"]
                                ])
# Always call this to apply the image to the application
uModal.applyAppImage()

# These are the modal objects ready to be consumed.
app = uModal.app
image = uModal.image

```

This will set up your container with the specified Python dependencies and files.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any questions or issues, please contact the maintainer at `support@uaimodal.io`.
