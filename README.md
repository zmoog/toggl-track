# toggl-track

[![PyPI](https://img.shields.io/pypi/v/toggl-track.svg)](https://pypi.org/project/toggl-track/)
[![Changelog](https://img.shields.io/github/v/release/zmoog/toggl-track?include_prereleases&label=changelog)](https://github.com/zmoog/toggl-track/releases)
[![Tests](https://github.com/zmoog/toggl-track/workflows/Test/badge.svg)](https://github.com/zmoog/toggl-track/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/zmoog/toggl-track/blob/master/LICENSE)

CLI tool and Python library to access Toggl Track https://toggl.com/track/

## Installation

Install this tool using `pip`:

    pip install toggl-track

## Usage

For listing the time entries in the last 24 hours, run:

    $ tgl entries list
                                                                Time Entries

    At           Description                                                                  Start      Stop       Duration   Tags
    ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    2023-02-04   toggl-track: insights                                                        05:37 AM              -
    2023-02-03   Community: Allow parsing of IPv6 addresses in ingest pipeline                08:18 PM   10:09 PM   1:51       type:support
    2023-02-03   🍲 Dinner                                                                    07:19 PM   08:18 PM   0:58
    2023-02-03   sync                                                                         06:19 PM   06:55 PM   0:35       type:sync
    2023-02-03   🚌 Shuttling kids between home and whatever                                  04:46 PM   06:19 PM   1:33
    2023-02-03   App Service logs integration: troubleshootign lucianpy issues                04:40 PM   04:46 PM   0:06       type:goal
    2023-02-03   Community: Allow parsing of IPv6 addresses in ingest pipeline                04:21 PM   04:40 PM   0:18       type:support
    2023-02-03   Community: Fix parsing error client port is blank and adjust for timeStamp   03:15 PM   04:21 PM   1:05       type:support
    2023-02-03   Community: Azure Signin Module authentication_processing_details Issue       02:37 PM   03:15 PM   0:38       type:support
    2023-02-03   Rosanna                                                                      11:06 AM   02:37 PM   3:31
    2023-02-03   Community: Azure Signin Module authentication_processing_details Issue       09:25 AM   11:06 AM   1:41       type:support
    2023-02-03   sync                                                                         08:37 AM   09:25 AM   0:48       type:sync
    ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                                                                        Total      13:08

Now you can also filter time entries by project ID:

    $ tgl entries --project-id 178435728 list
                                                                Time Entries

    At           Description                                                                  Start      Stop       Duration   Tags
    ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    2023-02-03   Community: Allow parsing of IPv6 addresses in ingest pipeline                08:18 PM   10:09 PM   1:51       type:support
    2023-02-03   sync                                                                         06:19 PM   06:55 PM   0:35       type:sync
    2023-02-03   App Service logs integration: troubleshootign lucianpy issues                04:40 PM   04:46 PM   0:06       type:goal
    2023-02-03   Community: Allow parsing of IPv6 addresses in ingest pipeline                04:21 PM   04:40 PM   0:18       type:support
    2023-02-03   Community: Fix parsing error client port is blank and adjust for timeStamp   03:15 PM   04:21 PM   1:05       type:support
    2023-02-03   Community: Azure Signin Module authentication_processing_details Issue       02:37 PM   03:15 PM   0:38       type:support
    2023-02-03   Community: Azure Signin Module authentication_processing_details Issue       09:25 AM   11:06 AM   1:41       type:support
    2023-02-03   sync                                                                         08:37 AM   09:25 AM   0:48       type:sync
    ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                                                                        Total      7:05

For grouping time entries by tags and sum up the totals, run:

    $ tgl entries --project-id 178435728 group-by --field tags --start-date 2023-02-01
        Time Entries

    tags           Duration
    ─────────────────────────
    type:support   7:13
    type:goal      5:10
    type:meeting   4:29
    type:sync      3:38
    type:hr        0:09
    ─────────────────────────
    Total          20:40

For help, run:

    toggl-track --help

You can also use:

    python -m toggl_track --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd toggl-track
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest

If you need to send other requests to Toggl API, you can capture responses using:

   pytest --record-mode=once
