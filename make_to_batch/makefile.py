#  MIT License
# 
#  Copyright (c) 2019 Andrea Esposito
# 
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
# 
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

"""The makefile module.

This module contains a series of definition that are used to represent a
Makefile.
"""

from typing import List, Any
import make_to_batch.look_up_table as look_up_table
import make_to_batch.parser as parser
import re
import logging


class Makefile:
    """The representation of a Makefile.

    It is composed of rules and variables. A Makefile starts with no rules and
    no variables.

    Attributes
    ----------
    __rules : Dict[str, Dict[List[str], List[str]]
        The rules of the Makefile.
    __variables : Dict[str, Any]
        The variables of the Makefile.
    """

    def __init__(self):
        """Create an empty Makefile
        """
        self.__rules = {}
        self.__variables = {}

    def parse_file(self, file_content: str) -> None:
        """Parse an existing Makefile.

        Parameters
        ----------
        file_content : str
            The content of an existing Makefile.
        """
        file_content = re.sub(r'''(?<!\\)\#.*?$''', '', file_content, flags=re.M) # Remove comments
        file_content = re.sub(r'''\s*?\\\s*?\n\s*''', ' ', file_content) # Transform all the multiline commands to single-line
        variable_pattern = re.compile(r'''^([^:#= ]*?) *?= *(?:\\?\n\s*|)("\s*?.*?\s*?"|.*?)$''', re.MULTILINE)
        target_pattern = re.compile(r'''^(.*?):\s*?(.*?)\s*?\n((?:(?:\t| {4}).*?\n)*)''', re.MULTILINE)
        matches = variable_pattern.findall(file_content)

        for match in matches:
            self.add_variable(match[0], re.sub(r'/', r'\\', match[1]))

        matches = target_pattern.findall(file_content)
        for match in matches:
            target_name = match[0]
            if target_name == ".PHONY":
                continue
            prerequisites = match[1]
            recipe = match[2]
            self.add_rule(
                target_name,
                Makefile.__prerequisites_from_string(prerequisites),
                Makefile.__recipe_from_string(recipe)
            )

    @staticmethod
    def __prerequisites_from_string(string: str) -> List[str]:
        """
        Get a rule's prerequisites from a string.

        Parameters
        ----------
        string : str
            A string containing the prerequisites.

        Returns
        -------
        List[str]
            A list of prerequisites.
        """
        string = string.strip()
        string = re.sub(r'''^(?:\|\s*)''', '', string)
        prerequisites = string.split(" ")
        return prerequisites if prerequisites != [""] else []

    @staticmethod
    def __recipe_from_string(string: str) -> List[str]:
        """Get a rule's recipe from a string.

        Parameters
        ----------
        string : str
            A string containing the rule's recipe.

        Returns
        -------
        List[str]
            A list of commands forming the recipe.
        """
        recipe = string.strip().split('\n')
        return recipe if recipe != [""] else []

    def add_rule(self, target: str, prerequisites: List[str], recipe: List[str]) -> None:
        """Add a rule to the Makefile.

        Parameters
        ----------
        target : str
            The new target's name.
        prerequisites : List[str]
            The new target's prerequisites.
        recipe : List[str]
            The new target's recipe.
        """
        self.__rules[target] = {
            'prerequisites': prerequisites,
            'recipe': recipe
        }

    def remove_rule(self, target: str) -> None:
        """Remove a rule from the Makefile.

        If the rule is not in the Makefile, do nothing.

        Parameters
        ----------
        target : str
            The target to be removed.
        """
        if target in self.__rules:
            del self.__rules[target]

    def remove_variable(self, variable: str) -> None:
        """Remove a variable from the Makefile.

        If the variable is not in the Makefile, do nothing.

        Parameters
        ----------
        variable : str
            The variable to be removed.
        """
        if variable in self.__rules:
            del self.__variables[variable]

    def add_variable(self, name: str, value: Any) -> None:
        """Add a variable to the Makefile.

        Parameters
        ----------
        name : str
            The new variable's name.
        value : Any
            The new variable's value.
        """
        self.__variables[name] = value

    @staticmethod
    def __convert_command_to_batch(old_command: str) -> str:
        """Convert a Makefile command to a batch command.

        Parameters
        ----------
        old_command : str
            The command to be converted.

        Returns
        -------
        str
            The equivalent command in batch. If no equivalent command is found, return the starting command.
        """
        commands_list = old_command.strip().split("&&")
        batch_commands = []

        number_of_dir_changed = 0
        for command in commands_list:
            command = command.strip()
            parsed_command = parser.Parser(command)

            logging.info("FOUND COMMAND: {}\n".format(parsed_command.program) +
                         "\tOPTIONS: {}\n".format(parsed_command.options) +
                         "\tPARAMETERS: {}".format(parsed_command.parameters))

            match = re.match(r"^cd (.*?)$", command)
            if match:
                number_of_dir_changed += 1
                batch_commands.append("PUSHD " + str(match.group(1)))
                continue
            if parsed_command.program in look_up_table.linux_to_dos:
                current_command = look_up_table.linux_to_dos[parsed_command.program]
                options = [current_command['options'][opt] if opt in current_command['options'] else opt for opt in parsed_command.options]
                batch_commands.append(current_command['command'] + " " + ' '.join(parsed_command.parameters) + ' ' + ' '.join(options))
            else:
                batch_commands.append(command)

        for _ in range(number_of_dir_changed):
            batch_commands.append("POPD")

        batch_commands = re.sub(r"\$[({](.*?)[)}]", r"%\1%", " && ".join(batch_commands))
        batch_commands = re.sub(r"%MAKE%", r"CALL make.bat", batch_commands)
        return batch_commands

    def to_batch(self) -> str:
        """Convert the Makefile to a Batch file.

        Returns
        -------
        str
            The batch file's content.
        """
        batch_content = "@echo off\n\n"
        for var in self.__variables:
            batch_content += "SET {var}={val}\n".format(var=var, val=self.__variables[var])

        batch_content += "\n"

        for rule in self.__rules:
            batch_content += '''IF /I "%1"=="{rule}" GOTO {rule}\n'''.format(rule=rule)
        if "all" in self.__rules:
            batch_content += '''IF /I "%1"=="" GOTO all\n'''
        batch_content += '''GOTO error\n'''

        batch_content += "\n"

        for rule in self.__rules:
            batch_content += ":{}\n".format(rule)
            for prerequisite in self.__rules[rule]["prerequisites"]:
                batch_content += "\tCALL make.bat {}\n".format(prerequisite)
            for command in self.__rules[rule]["recipe"]:
                batch_content += "\t" + Makefile.__convert_command_to_batch(command) + "\n"
            batch_content += "\tGOTO :EOF\n\n"

        batch_content += ''':error
    IF "%1"=="" (
        ECHO make: *** No targets specified and no makefile found.  Stop.
    ) ELSE (
        ECHO make: *** No rule to make target '%1%'. Stop.
    )
    GOTO :EOF'''

        batch_content += "\n"

        return batch_content
