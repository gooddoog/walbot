import os
import subprocess

import yaml

from src.log import log
from src.message import Msg


class Util:
    @staticmethod
    async def check_args_count(message, command, silent, min=None, max=None):
        if min and len(command) < min:
            await Msg.response(message, f"Too few arguments for command '{command[0]}'", silent)
            return False
        if max and len(command) > max:
            await Msg.response(message, f"Too many arguments for command '{command[0]}'", silent)
            return False
        return True

    @staticmethod
    async def parse_int(message, string, error_message, silent):
        try:
            return int(string)
        except ValueError:
            await Msg.response(message, error_message, silent)
            return

    @staticmethod
    async def parse_float(message, string, error_message, silent):
        try:
            return float(string)
        except ValueError:
            await Msg.response(message, error_message, silent)
            return

    @staticmethod
    def check_version(name, actual, expected, solutions=None):
        if (actual != expected):
            log.error(f"{name} versions mismatch. Expected: {expected}, but actual: {actual}")
            if solutions:
                log.info("Possible solutions:")
                for solution in solutions:
                    log.info(f" - {solution}")
            return False
        return True

    @staticmethod
    async def run_external_command(message, cmd_line, silent=False):
        result = ""
        try:
            log.debug(f"Processing external command: '{cmd_line}'")
            process = subprocess.run(cmd_line, shell=True, check=True,
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            log.debug(f"External command '{cmd_line}' finished execution with return code: {process.returncode}")
            result = process.stdout.decode("utf-8")
            await Msg.response(message, result, silent)
        except subprocess.CalledProcessError as e:
            await Msg.response(message, f"<Command failed with error code {e.returncode}>", silent)
        return result

    @staticmethod
    def read_config_file(path):
        yaml_loader, _ = Util.get_yaml()
        if os.path.isfile(path):
            with open(path, 'r') as f:
                try:
                    return yaml.load(f.read(), Loader=yaml_loader)
                except Exception:
                    log.error(f"File '{path}' can not be read!", exc_info=True)
        return None

    @staticmethod
    def get_yaml(verbose=False):
        try:
            loader = yaml.CLoader
            if verbose:
                log.debug("Using fast YAML Loader")
        except AttributeError:
            loader = yaml.Loader
            if verbose:
                log.debug("Using slow YAML Loader")
        try:
            dumper = yaml.CDumper
            if verbose:
                log.debug("Using fast YAML Dumper")
        except AttributeError:
            dumper = yaml.Dumper
            if verbose:
                log.debug("Using slow YAML Dumper")
        return loader, dumper
