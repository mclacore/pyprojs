#!/bin/bash

read -p "Enter the first app name: " app1Name
read -p "Enter the second app name: " app2Name
read -p "Enter the tag: " tag

echo -n "Enter the Artifact ID for app authentication: "
IFS= read -rs artifactId
echo

mass image push mclacore/rps -r westus -a "$artifactId" -t "$tag"

mass app patch "$app1Name" --set=".image.tag=\"$tag\""
mass app deploy "$app1Name"

mass app patch "$app2Name" --set=".image.tag=\"$tag\""
mass app deploy "$app2Name"
