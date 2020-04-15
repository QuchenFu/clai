#
# Copyright (C) 2020 IBM. All Rights Reserved.
#
# See LICENSE.txt file in the root directory
# of this source tree for licensing information.
#

import abc
import os

class Provider:
    
    # Define instance data members
    baseURI:str = ""
    excludes:list = []
    
    def __init__(self, section:dict):
        self.baseURI = section.get('api')
        
        # Get the platform exclusion list, in lowercase if possible
        if 'exclude' in section.keys():
            self.excludes = [excludeTarget.lower() for excludeTarget in section.get('exclude').split()]
        else:
            self.excludes = []
    
    def getExcludes(self) -> list:
        return self.excludes
    
    def canRunOnThisOS(self) -> bool:
        """Returns True if this search provider can be used on the client OS
        """
        
        # If our exclusion list is empty, then this provider can work on any OS
        if len(self.excludes) == 0:
            return True
        
        os_name:str = os.uname().sysname.lower()
        return (os_name not in self.excludes)
    
    @abc.abstractmethod
    def call(self, query: str, limit: int = 1):
        pass
    
    def __str__(self) -> str:
        return self.baseURI
