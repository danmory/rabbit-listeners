import re
import yaml


REGEXP = r'(?<=\"err\").*'


def read_config():
  with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
  return config


def main():
  config = read_config()
  files = list(map(lambda q: q["out"], config["queues"]))
  for f in files:
    print("reading %s" % f)
    with open(f, "r") as file:
      with open("parsed.txt", "a") as file_parsed:
        for line in file.readlines():
          match = re.search(REGEXP, line)
          if match is not None:
            file_parsed.write("%s \n" % match.group())


if __name__ == "__main__":
  main()
