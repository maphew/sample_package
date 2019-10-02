import click
import sys


@click.group()
def main():
    """
    Console script
    """
    pass


@main.command()
def test():
    print("Sample Package")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
