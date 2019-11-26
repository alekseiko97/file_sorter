# File sorter
Python script that groups files in Downloads folder by their extension and removes them (puts into trash bin) if their total size exceeds a certain amount

# Installation and usage
1. Install Python >= 3.5
2. pip install send2trash
3. git clone https://github.com/alekseiko97/file_sorter
4. cd file_sorter
5. python3 main.py <file_extension_goes_here> or python3 main.py (.dng by default)

# TODO
1. Let the user decide whether to move the entire folder to the trash bin or remove immediately
2. Let the user set the treshold after which the files should be removed (flag in args)
3. Let the user set a desired directory where the files should be scanned
4. Schedule the script execution
