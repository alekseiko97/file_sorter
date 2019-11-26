# File sorter
Python script that groups files in Downloads folder by their extension and removes them (puts into trash bin) if their total size exceeds a certain value

# Installation and usage

* Install Python >= 3.5
* pip install send2trash
* git clone https://github.com/alekseiko97/file_sorter
* cd file_sorter
* python3 main.py <file_extension_goes_here> or python3 main.py (.dng by default)

# TODO
* Let the user decide whether to move the entire folder to the trash bin or remove immediately
* Let the user set the treshold after which the files should be removed (flag in args)
* Let the user set a desired directory where the files should be scanned (instead of default 'Downloads')
* Schedule the script execution
* (optional) User-friendly interface
