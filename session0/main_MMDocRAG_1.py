from pathlib import Path


def search_pattern():
    base_path = Path("data/MMDocRAG")

    for file in base_path.rglob("*.md"):
        
        print(file)
        
        #content = file.read_text(encoding="utf-8")
        #print(content)

        break

# Crea un fichero CSV que guarde la relación de documento (path) y aparición de año 2021 o 2020 ?


if __name__ == "__main__":
    search_pattern()
