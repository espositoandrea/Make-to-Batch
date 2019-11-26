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

from typing import List, Any
import re


class Makefile:
    def __init__(self):
        self.__rules = {}
        self.__variables = {}

    def parse_file(self, file_content: str) -> None:
        file_content = re.sub(r'''\s*?\\\n\s*''', ' ', file_content)
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
        string = string.strip()
        string = re.sub(r'''^(?:\|\s*)''', '', string)
        prerequisites = string.split(" ")
        return prerequisites if prerequisites != [""] else []

    @staticmethod
    def __recipe_from_string(string: str) -> List[str]:
        recipe = string.strip().split('\n')
        return recipe if recipe != [""] else []

    def add_rule(self, target: str, prerequisites: List[str], recipe: List[str]) -> None:
        self.__rules[target] = {
            'prerequisites': prerequisites,
            'recipe': recipe
        }

    def remove_rule(self, target: str) -> None:
        if target in self.__rules:
            del self.__rules[target]

    def remove_variable(self, variable: str) -> None:
        if variable in self.__rules:
            del self.__variables[variable]

    def add_variable(self, name: str, value: Any) -> None:
        self.__variables[name] = value

    @staticmethod
    def __convert_command_to_batch(old_command: str) -> str:
        lookup = {
            re.compile(r'''^cp (.*?)\s+?(.*?)$'''): r'''XCOPY /Q /F \1''',
            re.compile(r'''^rm\s+?(?:-f\s+?)?(.*?)$'''): r'''DEL /Q /F \1'''
        }
        commands_list = old_command.strip().split("&&")
        batch_commands = []

        number_of_dir_changed = 0
        for command in commands_list:
            command = command.strip()
            match = re.match(r"^cd (.*?)$", command)
            if match:
                number_of_dir_changed += 1
                batch_commands.append(f"PUSHD {match.group(1)}")
                continue
            for key in lookup:
                match = key.match(command)
                if match:
                    batch_commands.append(key.sub(lookup[key], command))
                    break
            batch_commands.append(command)

        for i in range(number_of_dir_changed):
            batch_commands.append("POPD")

        return re.sub(r"\$[({](.*?)[)}]", r"%\1%", " && ".join(batch_commands))

    def to_batch(self) -> str:
        batch_content = "@echo off\n\n"
        for var in self.__variables:
            batch_content += f"SET {var}={self.__variables[var]}\n"

        batch_content += "\n"

        for rule in self.__rules:
            batch_content += f'''IF /I "%1"=="{rule}" GOTO {rule}\n'''
        if "all" in self.__rules:
            batch_content += f'''IF /I "%1"=="" GOTO all\n'''
        batch_content += f'''GOTO error\n'''

        batch_content += "\n"

        for rule in self.__rules:
            batch_content += f":{rule}\n"
            for prerequisite in self.__rules[rule]["prerequisites"]:
                batch_content += f"\tCALL make.bat {prerequisite}\n"
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
