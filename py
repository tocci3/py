#!/usr/bin/env bash
for python in python3.11 python3.10 python3.9 python3.8 python3.7 python3.6 python;do
  if type $python >/dev/null 2>&1 ;then
    $python "$@"
    break
  fi
done
