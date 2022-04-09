before() {
    echo "BEFORE - - - (should be nothing) - - -"
    py -m pip list | grep numpy
    echo "- - -"
}

after() {
    echo "AFTER - - - (should say numpy) - - -"
    py -m pip list | grep numpy
    echo "- - -"
}

pip install .

py -m pip uninstall numpy
before
touch TEST_OUTPUT.txt
py test.py > TEST_OUTPUT.txt 2>&1
after
