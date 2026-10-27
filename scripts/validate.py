#!/usr/bin/env python3
"""Checks data files: unique ids, image paths exist, deck completeness. Run from repo root."""
import json,os,sys
c=json.load(open('data/cards.json'));d={x['id'] for x in json.load(open('data/decks.json'))};e=[];ids=set()
need=['id','deck_id','arcana','number','title','image_front','alt_text','artwork_status']
for x in c:
    for k in need:
        if x.get(k) in (None,''):e.append(f"{x.get('id')}: missing {k}")
    if x['id'] in ids:e.append(f"duplicate id {x['id']}")
    ids.add(x['id'])
    if x['deck_id'] not in d:e.append(f"{x['id']}: unknown deck")
    if not os.path.exists(x['image_front']):e.append(f"{x['id']}: image missing")
for dk in d:
    cs=[x for x in c if x['deck_id']==dk];nums=[x['number'] for x in cs if x['arcana']=='major']
    if len(nums)!=len(set(nums)):e.append(f"{dk}: duplicate major numbers")
    print(f"{dk}: {len(cs)}/78 cards")
for p in json.load(open('data/products.json')):
    if p['status']=='concept' and p.get('purchase_url'):e.append(f"{p['slug']}: concept product has purchase_url")
print('\n'.join(e) or 'OK');sys.exit(1 if e else 0)
