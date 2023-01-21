# The original idea here was to scrape the Tesco website,
# however due to problems with getting requests I have gone
# for a hard coded approach by reading in options from a text
# file.

def getOptions():
    mains = []
    snacks = []
    drinks = []
    print("Importing mains...")
    with open('data/mains.txt', 'r') as file:
        mains = [line.rstrip() for line in file.readlines()]
    print("Done!")

    print("\nImporting snacks...")
    with open('data/snacks.txt', 'r') as file:
        snacks = [line.rstrip() for line in file.readlines()]
    print("Done!")

    print("\nImporting drinks...")
    with open('data/drinks.txt', 'r') as file:
        drinks = [line.rstrip() for line in file.readlines()]
    print("Done!")

    return mains, snacks, drinks