#!/bin/bash

set -e

echo "⚙️ Starting the Setup..."

echo "🔓 Giving Permissions to entrypoint.sh & setup.sh.."
chmod +x ./entrypoint.sh

echo "⬆️ Upping the Docker Image..."

cd .. ; docker compose up --build -d

echo "✅ All done! Get fun."