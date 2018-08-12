# coding=utf-8

import ConfigParser
from DBConnect import OracleConn


def write_config(conf_file_name, section, option_dict):
    cf = ConfigParser.ConfigParser()
    cf.read(conf_file_name)
    for option, value in option_dict.items():
        cf.set(section, option, value)
    with open(conf_file_name, 'wb') as f:
        cf.write(f)


def read_config(conf_file_name, section_list):
    """

    :param conf_file_name:
    :param section_list: section_list
    :return:
    """
    cf = ConfigParser.ConfigParser()
    cf.read(conf_file_name)
    config_dict = {}
    for sec in section_list:
        config_dict[sec] = _read_section(cf, sec)

    return config_dict


def _read_section(cf, section):
    option_dict = {}
    try:
        kvs = cf.items(section)
        for option in kvs:
            if option[1] == "True" or option[1] == "true":
                option_dict[option[0]] = True
            elif option[1] == "False" or option[1] == "false":
                option_dict[option[0]] = False
            else:
                option_dict[option[0]] = option[1]

    except Exception, e:
        print Exception, e
        print "no section " + section

    return option_dict


def create_db_conf(conf1, conf2):
    return create_oracle_conn(conf1), conf2


def create_oracle_conn(conf):
    conn = OracleConn(conf["user"], conf["password"], conf["host"] + ":" + conf["port"], conf["db_name"])
    return conn
