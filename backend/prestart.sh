#! /usr/bin/env sh
set -e

# Start Uvicorn with live reload
echo "Start Poetry Install."
exec poetry install &
wait

# echo "Start Init DB."
# exec poetry run python /app/db/init_db.py &
# wait
