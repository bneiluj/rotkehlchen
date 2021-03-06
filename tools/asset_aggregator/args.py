import argparse


def aggregator_args() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog='Asset aggregator',
        description=(
            'A tool to help cross-check, maintain and populate the '
            'Rotkehlchen assets list',
        ),
    )
    p.add_argument(
        '--cmc-api-key',
        help='If given we are trying to use coinmarketcap in the aggregator',
    )
    p.add_argument(
        '--always-keep-our-time',
        action='store_true',
        help=(
            'If given then we always keep our started times if they exist  '
            'and we do not compare to other APIs',
        ),
    )
    p.add_argument(
        '--input-file',
        help=(
            'A path to a secondary file for new assets to be added. If given, then '
            'only the assets of that file are checked. Used for faster addition '
            'of new assets to the assets list. Can not be combined with --process-eth-tokens',
        ),
    )
    p.add_argument(
        '--process-eth-tokens',
        action='store_true',
        help=(
            'If given then instead of looking at all_assets or an input file the '
            'script will iterate over the eth_tokens.json file and try to convert '
            'the assets in there and add them to all_assets.json. Can not be '
            'combined with --input-file',
        ),
    )
    return p
