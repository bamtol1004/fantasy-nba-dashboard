#!/usr/bin/env python3
"""Download current season CSV, validate, and retain last known good data on errors."""
import csv, io, os, pathlib, sys, urllib.request

URL=os.environ.get('NBA_STATS_CSV_URL','https://boxscorelab.com/downloads/2026-27-player-season-totals.csv')
OUT=pathlib.Path('data/2026-27-player-season-totals.csv')
try:
    req=urllib.request.Request(URL,headers={'User-Agent':'Mozilla/5.0 NBA-Fantasy-Stats-Updater/1.0'})
    with urllib.request.urlopen(req,timeout=35) as r:
        raw=r.read(8_000_000)
    text=raw.decode('utf-8-sig')
    reader=csv.DictReader(io.StringIO(text))
    fields=set(reader.fieldnames or [])
    required={'player_name','games_played','points'}
    if not required.issubset(fields):
        raise ValueError('Unexpected columns: '+repr(sorted(fields)))
    rows=list(reader)
    if len(rows)<100:raise ValueError('Too few player rows: '+str(len(rows)))
    for row in rows:
        gp=float(row['games_played'])
        if gp<0:raise ValueError('Negative GP')
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_bytes(raw)
    print('Updated CSV:',len(rows),'players,',len(raw),'bytes')
except Exception as exc:
    print('Download or validation failed; keeping bundled last-known-good CSV:',exc,file=sys.stderr)
    if not OUT.is_file():sys.exit(1)
