from yoyo import step

step(
    "CREATE TABLE pokestop_log (pokestop text, exp text, items text, dated datetime DEFAULT CURRENT_TIMESTAMP)"
)
