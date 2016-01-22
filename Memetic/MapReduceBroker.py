#!/usr/bin/env python2
"""Angela RML Interpreter - Core Server Module (abstract)
Created by the project angela team
    http://sourceforge.net/projects/projectangela/
    http://www.projectangela.org"""
from functools import reduce
    
__license__ = "GPL"
__version__ = "$Revision: 0.1 $"
__author__ = 'David Stocker'


# ***** BEGIN GPL LICENSE BLOCK *****
#
# Module copyright (C) David Stocker 
#
# This module is part of the Angela RML Engine.

# Angela is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Angela is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Angela.  If not, see <http://www.gnu.org/licenses/>.
#
# ***** END GPL LICENCE BLOCK *****
# --------------------------------------------------------------------------


class MapBroker(object):
        
    def execute(self, mapFunction, paramSet, argumentMap = []):

        #we're going to pass argumentMap in a map() and don't need it broken up.  Hence this little hack
        argumentMapParams = []
        for unused in paramSet:
            argumentMapParams.append(argumentMap)

        mappedValues = list(map(mapFunction, paramSet, argumentMapParams))
        return mappedValues 
    
    
    
class ReduceBroker(object):
            
    def execute(self, reduceFunction, paramSet):  
        returnResult = reduce(reduceFunction, paramSet)
        return returnResult 
            