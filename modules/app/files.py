# child classsed need to be in te same file
# super().method() calls parent class method. sort of extend the override
# able to extend init 
# nested classes in __init__
# : typedefs are hints not interperter sensitive. sadly

"""Contains logic for file handling"""

import os
from pathlib import Path

# sub class
class FileHandler:
    """This class will handle file processing"""

    path        : str       # this does nothing other then hints
    filename    : str       # this does nothing other then hints
    extension   : str       # this does nothing other then hints
    full_path   : str       # this does nothing other then hints
    valid_file  : bool      # this does nothing other then hints
    create      : bool      # this does nothing other then hints

    def __init__( self, filename: str, create_if_not : bool = False ):
        self.full_path = filename
        self.valid_file = False
        self.create = create_if_not;

        self.__handleFilename( )

    def __handleFilename( self ):
        """Process filename handed to self by splitting and change validity"""
        split_path = os.path.split( self.full_path )

        self.path = split_path[0]       # file path

        if not split_path[1]:   # no file name
            return

        split_filename = split_path[1].split( '.' )

        # no file extension found
        if ( len( split_filename ) <= 1 ):
            return

        # create file
        if self.create and not self.getPath():
            print( f"create: '{self.full_path}'")

            # create folder structure if non-existent
            os.makedirs( os.path.dirname(self.full_path), exist_ok=True )

            file = open(self.full_path, 'w')
            file.close()


        self.filename = split_filename[0]
        self.extension = split_filename[1]
        self.valid_file = True

    def printInvalid( self ):
        """Print on invalid file or exception"""
        print( f"file: '{self.full_path}' is invalid!")
        return False

    def getPath( self ) -> Path:
        """Return a valid pathlib.Path object"""
        usable: bool = True

        if not self.valid_file:
            usable = False

        path = Path( self.full_path )

        if not path.exists():
            usable = False

        if not usable:
            return self.printInvalid()

        return path

    def getContent( self ) -> str:
        """Return content of instanced file"""
        path = self.getPath();

        if not path:
            return False

        try:
            content = path.read_text().rstrip()
        except FileNotFoundError:
            return self.printInvalid()

        return path.read_text().rstrip()

    def getLines( self ) -> list:
        """Return list of lines of instanced file"""
        content = self.getContent()

        if not content:
            return []

        return content.splitlines()

    def setContent( self, content ) -> bool:
        """Store content in instanced file"""
        path = self.getPath();

        if not path:
            return False

        try:
            path.write_text( content )
        except FileNotFoundError:
            return self.printInvalid()
        else:
            return True
        
