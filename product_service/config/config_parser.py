import os
import configargparse
import sys

default_config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              'default.yaml'
                              )

parser = configargparse.ArgParser(config_file_parser_class=configargparse.YAMLConfigFileParser,
                                  default_config_files=[default_config_path],
                                  auto_env_var_prefix=""
                                  )

parser.add("--port", help="PORT")
parser.add("--mode", help="MODE")


docker_args = parser.parse_known_args(sys.argv)[0]