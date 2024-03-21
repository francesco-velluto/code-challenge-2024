from input_parser.parser import Parser
def main():
    file_path = "input_file.txt"
    
    parsed_data = Parser.parse_file(file_path)
    
    print(parsed_data)
    

if __name__ == "__main__":
    main()