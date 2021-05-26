import sys
sys.path.append("../")

from src.app.sigma import SigmaConverter

if __name__ == "__main__":
    sigmaconverter = SigmaConverter()
    sigmaconverter.read_from_file()
    sigmaconverter.write_to_excel()
