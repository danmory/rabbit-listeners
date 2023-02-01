import re
import yaml
import conf


REGEXP = r'(?<=\"err\").*'


def main():
  config = conf.read()
  files = list(map(lambda q: q["out"], config["queues"]))
  for f in files:
    print("reading %s" % f)
    with open(f, "r") as file:
      with open(config["parsed"], "a") as file_parsed:
        for line in file.readlines():
          match = re.search(REGEXP, line)
          if match is not None:
            file_parsed.write("%s \n" % match.group())


if __name__ == "__main__":
  main()
