import argparse


parser = argparse.ArgumentParser()

if __name__ == "__main__":
    # display help and version
    parser.add_argument(
        "--secrets", required=True
    )
    
    # parsing arguments from user
    args = parser.parse_args()
    
    secrets = args.secrets

    print(secrets)