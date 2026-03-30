Adventure Game Technical Documentation

Project Title:
Erevos-9: Mystery Adventure

1. Where the code is hosted
The code for this project is hosted on GitHub.
Repository link: [https://github.com/7zfx24m448-source/adventure-game-final.]

2. External services
This project uses the following external services:
- GitHub for code hosting
- PythonAnywhere for launching and sharing the game

3. Languages and technologies
This project was developed using:
- Python 3
- Text-based console interface
- Multiple Python files for modular design
- Object-oriented programming using a class object

4. System requirements and supported applications
System requirements:
- Python 3.7 or higher
- A computer running Windows, macOS, or Linux

Supported applications:
- PyCharm
- Terminal / Command Prompt
- PythonAnywhere console

5. Coding and naming conventions
- Each chapter is saved in a separate Python file
- File names are short and descriptive
- Function names use lowercase with underscores
- Class names use PascalCase
- Variables use clear names for readability

6. How to run, build, and deploy the program
To run the program locally:
1. Save all Python files in the same folder
2. Open the folder in PyCharm or terminal
3. Run main.py

To deploy the program:
1. Upload all files to GitHub
2. Upload all Python files to PythonAnywhere
3. Run main.py in a PythonAnywhere console

7. Overview of the architecture
The program is organized into multiple files:
- main.py starts the game and controls the flow
- player.py contains the Player class
- Chapter1.py to Chapter5.py contain the game chapters

The player moves through the story by making choices. Some chapters return values that affect the ending of the game.

8. How to start the program
Start the program by running:

python main.py

The game begins in the console and asks the player for input to continue through the story.

9. Maintenance and troubleshooting
If the program does not work correctly:
- Make sure all files are in the same folder
- Make sure Python 3 is installed
- Make sure the import statements match the file names exactly
- Check for typing or indentation errors in the code

10. Final version summary
The final version of this project includes:
- a working adventure game
- five separate chapter files
- a Player class object
- technical documentation in readme.txt
- deployment through PythonAnywhere
- code hosting through GitHub