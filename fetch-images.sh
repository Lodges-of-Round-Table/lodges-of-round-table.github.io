#!/bin/bash
# Run ONCE, before the old Drupal server is switched off, from inside this folder:
#   bash fetch-images.sh
# Downloads the original images from the live site into ./images and
# resizes the big Unsplash photos to 2000px wide (macOS 'sips').
set -e
cd "$(dirname "$0")"
mkdir -p images
BASE="https://www.lodgesofroundtable.uk/sites/default/files"

get() { echo "-> images/$2"; curl -fsSL "$BASE/$1" -o "images/$2"; }

get "Lodges%20of%20Round%20Table%20Banner%202_1.png"                         logo.png
get "2025-08/nick-fewings-IDU1v-rDmQ4-unsplash.jpg"                           cardiff-bay-sunset.jpg
get "2025-08/shengpengpeng-cai-qmZUcdwY5bE-unsplash.jpg"                      cardiff-castle.jpg
get "2025-08/grooveland-designs-apekIDd6sT0-unsplash.jpg"                     principality-stadium.jpg
get "2025-09/callum-blacoe-GcH7a4VTvEQ-unsplash.jpg"                          cardiff-by-air.jpg
get "2026-03/123499166_1809017145941187_2636471032564424288_n.jpg"            cardiff-masonic-hall.jpg
get "2026-03/holiday-inn-cardiff-8831071795-4x3.jpeg"                         holiday-inn-dining-room.jpg
get "2026-03/Times-Prices-1900x800-1.jpg"                                     cardiff-castle-tour.jpg
get "2026-03/The-Pierhead-3.jpg"                                              cardiff-bay-pierhead.jpg
get "2026-03/CORNERSTONE-SPIROS-19102016-023.jpg"                             cornerstone-cardiff.jpg
get "2026-03/7db50522cad2f4f4a1fb4a156ebf6e82a66bbbd2.jpeg"                   farewell-breakfast.jpg
get "2026-03/27b2a32caa9ba990950258204fde7ff9f69ba160.jpeg"                   holiday-inn-night.jpg
get "2026-03/bc304d6ed9ea04d9f12eb34da06028bc13004c8e.jpeg"                   holiday-inn-stadium-view.jpg
get "2026-03/5a85295d52367a8f4dd03d609669133940112ea3.jpeg"                   holiday-inn-location.jpg
get "2026-03/e2b14e32dae54309400a286fd46f228648820196.jpeg"                   room-with-a-view.jpg
curl -fsSL "https://www.lodgesofroundtable.uk/themes/contrib/vartheme_bs5/favicon.ico" -o favicon.ico

# The four Unsplash originals are 4000-6000px wide; shrink them for the web.
if command -v sips >/dev/null; then
  for f in cardiff-bay-sunset cardiff-castle principality-stadium cardiff-by-air cardiff-masonic-hall; do
    sips -Z 2000 -s formatOptions 80 "images/$f.jpg" >/dev/null
  done
fi
echo "Done. $(ls images | wc -l | tr -d ' ') files in images/"
