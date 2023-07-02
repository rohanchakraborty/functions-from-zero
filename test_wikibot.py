from wikibot import scrape

#def test_scrape():
#   assert "Microsoft" in scrape("Microsoft")

from click.testing import CliRunner

def test_wikibot():
    runner = CliRunner()
    result = runner.invoke(scrape, ["--name", "Microsoft"])
    assert result.exit_code == 0
    assert "Microsoft" in result.output