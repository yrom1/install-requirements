py -m pip uninstall numpy
echo "BEFORE - - -"
py -m pip list | grep numpy # should be nothing
echo "- - -"
py install_requirements.py
echo "AFTER - - -"
py -m pip list | grep numpy # should be nothing
echo "- - -"
