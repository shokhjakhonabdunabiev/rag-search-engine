import argparse, json


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            results = serach(args.query)
            for i, res in enumerate(results, 1):
                print(f"{i}. {res["title"]}")
        case _:
            parser.print_help()

def serach(query: str) -> list[str]:
    res = []
    with open("data/movies.json") as file:
        data = json.load(file)
        for movie in data["movies"]:
            if len(res) == 5:
                break
            if query in movie["title"]:
                res.append(movie["title"])
    return res

if __name__ == "__main__":
    main()