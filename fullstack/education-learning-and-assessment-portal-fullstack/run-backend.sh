#!/bin/sh
set -eu
cd "$(dirname "$0")/../shared-typescript"
pnpm start ../education-learning-and-assessment-portal-fullstack/project.json
