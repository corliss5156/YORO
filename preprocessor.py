import re
import json
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="input filename with extension")
    parser.add_argument("--output", help="output filename with json extension")
    args = parser.parse_args()

    with open(args.input) as f:
        raw_data = f.read()

    text = re.split("[=]+", raw_data)[1:-1]
    final = {}
    for block in text:
      block = block.replace("\n", "")
      block = re.split("[.?!]", block, 1)
      first_sentence, rmd_block = block[0], block[1]
      final[first_sentence] = rmd_block

    with open(args.output, 'w') as file:
      json.dump(final, file)

if __name__ == "__main__":
    main()
