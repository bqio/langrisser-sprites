from cram import pallete_4bpp_from_file
from vram import tiles_from_file, tile_apply_pallete, tile_to_buf
from os.path import join
from PIL import Image

CRAM_PATH = join("data", "cram.bin")
VRAM_PATH = join("data", "vram.bin")

if __name__ == "__main__":
  pallete = pallete_4bpp_from_file(CRAM_PATH)
  tiles = tiles_from_file(VRAM_PATH)
  tile = tiles[6]

  tile = tile_apply_pallete(tile, pallete)
  tile_buf = tile_to_buf(tile)
  
  image = Image.frombuffer(mode="RGB", size=[8, 8], data=tile_buf)
  image.show()