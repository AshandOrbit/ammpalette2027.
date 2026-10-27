# The Living Palette

Static site for the Living Palette section of A Million Mosaics. No build step. Plain HTML, CSS, JavaScript and JSON.

## Deploy on GitHub Pages
1. Create a repository and upload the contents of this folder to the root of the main branch.
2. Settings, Pages, Source: Deploy from a branch, main, root.
3. Open the Pages URL. Routes use hash paths (#/worlds), so refresh never breaks and the repository base path does not matter.

To serve at /living-palette/ on the main site, put these files in a folder of that name.

## Run locally
`python3 -m http.server` then open http://localhost:8000. (fetch needs a server, not file://.)

## Edit content
Everything lives in data/. Run `python3 scripts/validate.py` after changes.

- Add a world: add an object to data/worlds.json (slug, name, palette, focus, hero, signature, note, accent, deck, status).
- Add a deck: add to data/decks.json.
- Add a card: put a webp at assets/decks/{deck}/cards/{id}.webp and add an object to data/cards.json. Fields follow the plan: id, deck_id, arcana, number, suit, rank, title, character_name, ecosystem, species_subject, upright, reversed, reflection, ecological_note, scientific_sources, image_front, alt_text, artwork_status. Set meanings_status to complete once the text is written.
- Add a product: add to data/products.json. status is concept, coming_soon, preorder, available or sold_out. A Buy button appears only when purchase_url is set.

## Rules built in
- Full deck draw unlocks only when a deck has 78 cards, all with meanings. Until then the reading page draws from demo cards and says so.
- Images in assets/decks are 360 px previews cropped from overview sheets. Replace them with approved individual card files. Keep masters elsewhere.
- Open items are in docs/RECONCILIATION.md. Card meanings are pending on purpose.
- Mailing list is a placeholder until an email provider is connected.
