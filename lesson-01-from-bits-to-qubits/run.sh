#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-python3}"

"$PYTHON" "$SCRIPT_DIR/lesson_01.py" | awk '
/^Start in \|0>$/ {
    print "============================================================"
    print "RESULT 1 OF 3 - DEFINITE ZERO"
    print "============================================================"
    print
    next
}
/^Apply X to prepare \|1>$/ {
    print "============================================================"
    print "RESULT 2 OF 3 - DEFINITE ONE"
    print "============================================================"
    print
    next
}
/^Apply H for superposition$/ {
    print "============================================================"
    print "RESULT 3 OF 3 - EQUAL SUPERPOSITION"
    print "============================================================"
    print
    next
}
{ print }
'
