# soundsafe

To run the graphical user interface install Python:

https://www.python.org/downloads/

When you launch the installer, ENSURE THAT THE BOX RELATED TO ‘Add Python 3.7 to PATH’ IS CHECKED. Proceed with the standard installation (not the custom one).

You are suggested to set up a Virtual Environment where all the required libraries are installed. To do so, create a folder and open the command prompt:

    run: python -m pip install virtualenv
    if a warning comes up run: python -m pip install --upgrade pip
    then run: python -m virtualenv pyqt5_venv
    run, to install the required libraries: python -m pip install pyqt5 pyqtgraph pyserial
    run, to install the required libraries: python -m pip install pandas
    run, to install the required libraries: python -m pip install openpyxl

Link the virtual environment to Visual Studio Code, to use it as an IDE. Instructions at the link:

https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment
