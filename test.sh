#!/bin/bash

echo "⏳ Waiting for the app to start..."

# Try up to 10 times with 2 seconds between
for i in {1..10}; do
  if curl --fail http://localhost:8000 > /dev/null 2>&1; then
    echo "✅ App is up and responding!"
    exit 0
  fi
  echo "❌ Attempt $i: App not responding yet. Retrying in 2s..."
  sleep 2
done

echo "🚨 App failed to start after multiple attempts."
exit 1
