from wuyubot.utils.yaml import yaml_util as yaml
def load_config() -> dict:
    cfg = yaml('./data/config.yaml')
    return cfg