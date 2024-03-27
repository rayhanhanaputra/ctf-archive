#!/bin/bash

FILE=${1?File to be decompiled}

if ! [[ $FILE =~ ^.*.ml$ ]]; then
    echo "Error: File must end in an .ml extension."
    exit 1
fi
if ! [ -f "$FILE" ]; then
    echo "Error: File must exist."
    exit 1
fi



BASENAME=$(basename "${FILE%.*}")
DIRNAME=$(dirname "${FILE%.*}")
TARGETNAME="${DIRNAME}/${BASENAME}.s"

# run dune with verbose and copy last output
BUILD_COMMAND=$(dune clean && dune build --verbose 2>&1 | tail -n1)

# retrieve build directory from output
BUILD_DIR=$(echo $BUILD_COMMAND | grep ocamlopt | sed 's/.*(cd \(.*\) && .*/\1/')

if ! [ $? -eq 0 ]; then
    echo "Error: Failed to compile. Please make sure the project compiles before decompiling."
    exit 1
fi


ML_FILES=$(find . -type f -name '*.ml' | grep -v _build/default)
SORTED_ML_FILES=$(ocamldep -sort $ML_FILES)

# run ocamlopt with flags from dune, but set it up to output assembly file and only compile selected file
COMPILE_COMMAND=$(echo $BUILD_COMMAND | sed "s/.*:\(.*\))/\1 -S /")
eval "$COMPILE_COMMAND ${SORTED_ML_FILES})"

if ! [ $? -eq 0 ]; then
    echo "Error: Failed to compile. Please make sure the project compiles before decompiling."
    exit 1
fi

OUTPUT_FILE="$BUILD_DIR/$TARGETNAME"

if [ -f "$OUTPUT_FILE" ]; then
    cat  "$OUTPUT_FILE"
else
    echo "Error: Build failed to output assembly file."
    exit 1
fi


