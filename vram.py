from io import BytesIO
from struct import pack as pk

def tiles_from_file(file_path: str) -> list:
  with open(file_path, "rb") as fp:
    fp.seek(0, 2)
    file_size = fp.tell()
    fp.seek(0, 0)
    chunk_count = file_size // 0x20
    chunks = []
    for _ in range(chunk_count):
      chunks.append(list(fp.read(0x20)))
    return chunks

def tile_apply_pallete(tile: list, pallete: list):
  _tile = []
  for pal_idx in tile:
    _tile.append(pallete[pal_idx >> 4 & 0xF])
    _tile.append(pallete[pal_idx & 0xF])
  return _tile

def tile_to_buf(tile: list) -> list:
  _tile = BytesIO()
  for pixel in tile:
    _tile.write(pk("<B", pixel[0]))
    _tile.write(pk("<B", pixel[1]))
    _tile.write(pk("<B", pixel[2]))
  return _tile.getvalue()