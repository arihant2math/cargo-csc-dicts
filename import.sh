rm -rf dicts/
mkdir dicts
# Downloads
curl -o common.txt https://raw.githubusercontent.com/fordsfords/moby_words_2/refs/heads/main/common.txt
# Patches
cp ../cspell-dicts/dictionaries/en_US/src/legacy/en_US.txt ../cspell-dicts/dictionaries/en_US/src/legacy_en_US.txt
cp en_US.txt ../cspell-dicts/dictionaries/en_US/src/en_US.txt
cp common.txt ../cspell-dicts/dictionaries/en_US/src/common.txt
rm common.txt
# Run
uv run import.py
# Remove Patches
rm ../cspell-dicts/dictionaries/en_US/src/en_US.txt
rm ../cspell-dicts/dictionaries/en_US/src/legacy_en_US.txt
rm ../cspell-dicts/dictionaries/en_US/src/common.txt
