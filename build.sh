rm -rf dependencies
rm artifact.zip
pip install -r requirements.txt --platform manylinux2014_x86_64 --target dependencies --only-binary=:all:
(cd dependencies; zip ../artifact.zip -r .)
zip artifact.zip -u main.py