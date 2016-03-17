(cd $1 && tar -cvzf - `find . -name "*.go"`) | tar xvzf -
find . -name "*.go" -exec rename -f 's/\.go$/.go.html/' '{}' \;
