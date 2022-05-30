from src.app.sigma import SigmaConverter
import sys
sys.path.append("../")



if __name__ == "__main__":
    sigmaconverter = SigmaConverter()
    sigmaconverter.read_from_file()
    sigmaconverter.write_to_excel()
