if ! hash python; then
    echo "python is not installed"
    exit 1
fi

ver=$(python -V 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')
if [ "$ver" -lt "30" ]; then
    echo "This script requires python 3 or greater"
    exit 1
fi

if ! hash cargo; then
    echo "cargo is not installed"
    exit 1
fi
echo "Running stuff"
exec python3 runner.py
echo "All done"
