import wikipedia
import click

@click.command()

@click.option("--name", prompt="wikipedia page to scrape", help="Webpage you want to scrape")
#@click.option("--length", prompt="Number of sentences", help="Summary in lines")

def scrape(name):
    result= wikipedia.summary(name, sentences=1)
    click.echo(click.style(result,bg="yellow",fg="white"))

if __name__ == "__main__":
    scrape()