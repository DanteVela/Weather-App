# Python: Weather App

<p align="center">
  <img src="https://logos-world.net/wp-content/uploads/2021/10/Python-Symbol.png" width="600" height="300" alt="Python Logo">
</p>

> A Python Weather App that provides real-time forecasts without an API key, leveraging weather.py for data fetching, ui.py for the interface, and icons.py for intuitive weather symbols.

This cross-platform Python application delivers current weather information for any city without needing an API key. It leverages weather.py to interface with an open weather data source, ui.py to render a clean terminal or GUI interface, and icons.py to translate conditions into intuitive emoji icons. Easy to install and customize, it’s perfect for developers seeking a no-frills weather tool built entirely in Python.

- Major Disclaimer: 
  - This uses public data without an API key and is provided “as is” with no guarantees on accuracy or service reliability.
  - As stated within the License, you must obtain permission by the Author of this project.

## Installing / Getting Started

A quick introduction of the minimal setup you need to get a Hello World up & running in VS Code.

```shell
Install "VS Code" and "Python"
Ensure the "Environment Variable" is included in "the Path" within Python ("Click the Checkbox")
Install the needed "Extensions for VS Code" ["Python by Microsoft, Python Debugger by Microsoft, etc"]
Other Extensions may include ["GitHub, Markdown, Elint/lint, etc"] to utilize GitHub Version Control and other language syntax
Start coding Python
You can run the code by using the following: ["python filename.py"]
```

Congrats! You just created your first Python file and there's so much more you can do so experiment to your hearts content!

### Initial Configuration

Requirements:
  
- Ensure that the project file/folder and other dependencies you plan to make is within the range for code execution.
  
- Ensure you have a GitHub account to make project repos and save changes to prevent loss of progress with your code in the future.

## Developing

In order to start developing the project further:

```shell
git clone https://github.com/username/project-name.git
cd project-name/
```

After setting up GitHub and the GitHub repo, you should be able to clone/commit/publish your progress as you make changes to the project.

### Building

To build the project after some code changes:

```shell
commit changes by using the GitHub extensions from VS Code or by using the terminal via commands
stash/push the changes into the main/master branch of the project or in another branch if needed
```

After commiting and pushing the changes into GitHub, you should see the project repo change to reflect the most recent code.

### Deploying / Publishing

In case you want to publish your project to a server:

```shell
Ensure that the project is fully functional and give appropiate credit to all contributors/authors.
Provide a step-by-step process of how you managed to complete the project.
Check the project and live server before finalizing the project status.
```

If you want to use GitHub or any other 3rd party platform for your server, you can but it may prove to be difficult with the lack of updated tutorials for all sorts of software services. 
[You can checkout the masterPortfolio repo to see how to use GitHub pages]

## Features

This project repo has the following:

- No API Key Required: Fetches weather data from public sources using weather.py without any authentication hurdles.
- Modular Codebase:
  - weather.py: handles data retrieval and parsing.
  - ui.py: manages the user interface (CLI/GUI).
  - icons.py: maps weather conditions to intuitive symbols.
- Cross-Platform Compatibility: Works seamlessly on Windows, macOS, and Linux.
- Error Handling & Offline Mode:
  - Gracefully handles network errors and invalid city names.
  - Caches the latest successful response for quick offline access.
- Clear Documentation:
  - Step-by-step installation guide.
  - Usage examples for advanced configurations.
- (To be continued) ...

## Links

Helpful links that you can use with your project:

- GitHub Commands Cheat Sheet: [https://github.com/tiimgreen/github-cheat-sheet]
- In case of sensitive bugs like security vulnerabilities, please use the issue tracker or contact me directly. 
  We value your effort to improve the security and privacy of this project!

## References

"Give Credit where its Due": Credit goes to all the original repo owners, contributors, and author into making this project.
(If possible, please provide the GitHub URLs and names to all that contributed including the project owner)

<!-- - "Title" by Author [Social Media/Location] -->

## Licensing

[![License](https://img.shields.io/static/v1?label=License&message=All%20Rights%20Reserved&color=lightgrey&style=for-the-badge)](LICENSE)

"The project is licensed under Custom Proprietary License ("All Rights Reserved") v1.0"