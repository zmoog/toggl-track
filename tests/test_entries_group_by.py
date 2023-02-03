import pytest
from click.testing import CliRunner

from toggl_track.cli import cli


env = {
    "TOGGL_API_TOKEN": "1234567890abcdef1234567890abcdef", # fake token for testing
}


@pytest.mark.vcr
@pytest.mark.block_network
def test_group_by_tags():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            ["entries", "group-by", "--field", "tags", "--start-date", "2023-01-26", "--end-date", "2023-01-27"],
            env=env,
        )
        assert result.exit_code == 0
        assert (
            result.output
            == """       Time Entries        
                           
  tags           Duration  
 ───────────────────────── 
  type:support   5:44      
                 5:14      
  type:sync      3:00      
  type:meeting   2:04      
  type:goal      0:35      
                           

"""
        )
        
