from hashlib import sha256
from datetime import datetime

USER_DB = {
  "bitya": sha256("1".encode()).hexdigest(),
  "alina": sha256("69420228".encode()).hexdigest(),
  "amir":  sha256("amir_lox".encode()).hexdigest(),
  "beks":  sha256("lox_amir".encode()).hexdigest(),
}

BALANCE_DB = {
  "bitya": 700,
  "alina": 500,
  "amir":  300,
  "beks":  100
}

OLYMPIADS_DB = {
  1: ["Robotics Senior 1", datetime(2024, 12, 15, 15, 00)],
  2: ["Robotics Junior 1", datetime(2024, 12, 15, 15, 00)]
}